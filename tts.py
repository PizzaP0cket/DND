from edge_tts import Communicate
from voices import default_voices, default_character_registry
import asyncio
import random
import os
import re

# ──────────────────────────────────────────────────────────────────────────────
# Script Parsing and Character Registration
# ──────────────────────────────────────────────────────────────────────────────


def parse_script(script: str, character_registry=None):
    """
    Parses a script into segments of (character, dialogue).
    Supports:
      - [Name, Gender] "Dialogue"
      - "Dialogue" (assumed from last speaker)
      - Narration in between
    """
    if character_registry is None:
        character_registry = default_character_registry.copy()

    # Pattern to match either:
    # 1. [Name, Gender] "Dialogue"
    # 2. Just "Dialogue"
    pattern = r"""
    (                                   # Group 1: Optional character tag
        \[\s*([\w\s\d]+?)\s*,\s*(\w+)\s*\]  # Group 2: Name (with spaces), Group 3: Gender
    )?                                  # Whole tag is optional
    \s*                                 # Optional whitespace
    [“"]([^”"]+)[”"]                    # Group 4: Dialogue
    """
    regex = re.compile(pattern, re.VERBOSE)
    segments = []
    last_index = 0
    last_speaker = "Narrator"

    for match in regex.finditer(script):
        start, end = match.span()
        tag, name, gender, dialogue = match.groups()

        # Add narration between matches
        if start > last_index:
            narration = script[last_index:start].strip()
            if narration:
                segments.append(("Narrator", narration))

        if name and gender:
            normalized_name = name.strip()
            gender_lower = gender.lower()
            register_character(normalized_name, gender_lower, character_registry)
            last_speaker = normalized_name
        # Use last known speaker
        segments.append((last_speaker, dialogue.strip()))
        last_index = end

    # Any remaining narration
    if last_index < len(script):
        narration = script[last_index:].strip()
        if narration:
            segments.append(("Narrator", narration))

    return segments, character_registry


def register_character(name: str, gender: str, registry: dict) -> None:
    normalized_name = name.strip()
    if normalized_name in registry:
        return  # Already registered — keep the existing pitch and voice

    gender_lower = gender.lower()
    voice_entry = random.choice(
        default_voices.get(gender_lower, default_voices["unknown"])
    )

    registry[normalized_name] = {
        "gender": gender_lower,
        "voice": voice_entry["name"],
        "pitch": random.choice(voice_entry["pitch"]),
        "rate": "0%",
    }


# ──────────────────────────────────────────────────────────────────────────────
# Audio Generation
# ──────────────────────────────────────────────────────────────────────────────


async def generate_audio_segments(
    segments, character_registry, output_dir="audio_segments"
):
    os.makedirs(output_dir, exist_ok=True)

    async def process_segment(i, speaker, line):
        text = line.replace("*", "")
        voice = character_registry[speaker]["voice"]
        pitch = character_registry[speaker]["pitch"]
        filename = os.path.join(output_dir, f"segment_{i}.mp3")

        try:
            communicate = Communicate(text=text, voice=voice, pitch=pitch)
            await communicate.save(filename)
            return filename
        except Exception as e:
            print(f"[Error] Failed to generate audio for '{speaker}': {e}")
            return None

    tasks = [
        process_segment(i, speaker, line) for i, (speaker, line) in enumerate(segments)
    ]
    audio_files = await asyncio.gather(*tasks)
    return [f for f in audio_files if f is not None]


# ──────────────────────────────────────────────────────────────────────────────
# Utility: Clean up audio directory
# ──────────────────────────────────────────────────────────────────────────────


def cleanup(directory):
    if not os.path.exists(directory):
        print(f"[Warning] Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        try:
            if os.path.isfile(path):
                os.remove(path)
        except Exception as e:
            print(f"[Warning] Could not delete file '{path}': {e}")
