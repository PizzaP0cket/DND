from chat_gpt import send_prompt, wait_for_response
from tts import parse_script, register_character, generate_audio_segments, cleanup
import asyncio
import pygame
import time

# ──────────────────────────────────────────────────────────────────────────────
# Audio Playback
# ──────────────────────────────────────────────────────────────────────────────


# Initialise audio player
def initialize_audio_player():
    pygame.mixer.init()


# Play Background tack
def play_background_music(track_path):
    try:
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.set_volume(0.2)  # adjust volume
        pygame.mixer.music.play(-1)  # loop forever
        print(f"{track_path} music started.")
    except Exception as e:
        print(f"[Error] Could not play background music: {e}")


# Play sound audio (characters, noises)
def play_audio_files(files):
    for file in files:
        try:
            sound = pygame.mixer.Sound(file)
            channel = sound.play()
            while channel.get_busy():
                time.sleep(0.1)
        except Exception as e:
            print(f"[Error] Failed to play audio file '{file}': {e}")


# ──────────────────────────────────────────────────────────────────────────────
# pip3 install pychrome pygame
# To run, you first need to launch google chrome in development mode
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/ChromeDebug"
# ──────────────────────────────────────────────────────────────────────────────


init_prompt = """ You are the Dungeon Master for a Dungeons & Dragons 5e adventure. I'm a player in a prison cell with two NPCs: Mathew (male rogue) and Zelda (female sorcerer). We got caught on our last job. 
CRITICAL RULES:
- ANY AND ALL dialogue MUST use format: [Name,Gender]"dialogue" - e.g. [Mathew, Male]"Where is my sword"
- Use D&D 5e mechanics
Begin with me gaining conciousness. Then prompt me to act.
"""

# ──────────────────────────────────────────────────────────────────────────────
# Main Conversation Loop
# ──────────────────────────────────────────────────────────────────────────────


async def main():
    initialize_audio_player()
    play_background_music("background_music.mp3")
    print("\n")  # For distance that pygame creates

    send_prompt(init_prompt)
    response = wait_for_response()

    print("\n\nGenerating...")
    segments, character_registry = parse_script(response)
    print("Registered characters:")
    voices = character_registry  # no need to load
    for name, attrs in voices.items():
        print(f"{name} - {attrs['voice']} - {attrs['pitch']}")

    audio_files = await generate_audio_segments(segments, character_registry)
    print("Initializing audio player...")
    initialize_audio_player()
    print("Playing audio...")
    play_audio_files(audio_files)

    print("🤖 ChatGPT:", response)

    while True:
        user_input = input("\nYou: ")

        print("\n")
        if user_input.lower() in {"exit", "quit", "clear"}:
            print("Goodbye!")
            break
        send_prompt(user_input)
        response = wait_for_response()

        print("\n\nGenerating...")
        segments, _ = parse_script(response, character_registry)
        # segments, character_registry = parse_script(assistant_response)
        print("Registered characters:")
        voices = character_registry  # no need to load
        for name, attrs in voices.items():
            print(f"{name} - {attrs['voice']}: {attrs['pitch']}")

        audio_files = await generate_audio_segments(segments, character_registry)
        print("Initializing audio player...")
        print("Playing audio...")
        play_audio_files(audio_files)
        cleanup("audio_segments")

        print("🤖 ChatGPT:", response)


if __name__ == "__main__":
    asyncio.run(main())
    cleanup("audio_segments")


# Add sound effects
# Improve voice
# Add catch interuption


# API get reddit
# Feed to GPT
# Get Audio
