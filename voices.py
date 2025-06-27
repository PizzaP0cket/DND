default_voices = {
    "male": [
        # News, Novel - Lively
        {
            "name": "en-US-RogerNeural",
            "pitch": ["+0Hz", "-5Hz", "-10Hz", "-15Hz", "-20Hz", "-25Hz", "-30Hz"],
        },
        # Conversation, Copilot - Warm, Confident, Authentic, Honest
        {
            "name": "en-US-AndrewNeural",
            "pitch": [
                "+5Hz",
                "+0Hz",
                "-5Hz",
                "-10Hz",
                # "-15Hz",
                # "-20Hz",
                # "-25Hz",
                # "-30Hz",
            ],
        },
        # Conversation, Copilot - Warm, Confident, Authentic, Honest
        {
            "name": "en-US-AndrewMultilingualNeural",
            "pitch": [
                "+5Hz",
                "+0Hz",
                "-5Hz",
                "-10Hz",
                # "-15Hz",
                # "-20Hz",
                # "-25Hz",
                # "-30Hz",
            ],
        },
        # General - Friendly, Positive
        # {
        #     "name": "en-NG-AbeoNeural",
        #     "pitch": [
        #         "+10Hz",
        #         "+5Hz",
        #         "+0Hz",
        #         "-5Hz",
        #         # "-10Hz",
        #         # "-15Hz",
        #         # "-20Hz",
        #         # "-25Hz",
        #         # "-30Hz",
        #     ],
        # },
        # General - Friendly, Positive
        {
            "name": "en-KE-ChilembaNeural",
            "pitch": [
                "+10Hz",
                "+5Hz",
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
                # "-25Hz",
                # "-30Hz",
            ],
        },
        # Conversation, Copilot - Approachable, Casual, Sincere
        {
            "name": "en-US-BrianNeural",
            "pitch": [
                "+10Hz",
                "+5Hz",
                "+0Hz",
                "-5Hz",
                "-10Hz",
                "-15Hz",
                "-20Hz",
                "-25Hz",
                "-30Hz",
            ],
        },
        # General - Friendly, Positive
        # {
        #     "name": "en-TZ-ElimuNeural",
        #     "pitch": [
        #         "+10Hz",
        #         "+5Hz",
        #         "+0Hz",
        #         # "-5Hz",
        #         # "-10Hz",
        #         # "-15Hz",
        #         # "-20Hz",
        #         # "-25Hz",
        #         # "-30Hz",
        #     ],
        # },
        ###
        # {"name": "en-US-GuyNeural"},
        # {"name": "en-IN-PrabhatNeural"},
        # {"name": "en-CA-LiamNeural"},
        # {"name": "en-GB-ThomasNeural"},
        # {"name": "en-US-BrianMultilingualNeural"},
    ],
    "female": [
        # General - Friendly, Positive
        {
            "name": "en-KE-AsiliaNeural",
            "pitch": [
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
            ],
        },
        # Conversation, Copilot - Expressive, Caring, Pleasant, Friendly
        {
            "name": "en-US-AvaNeural",
            "pitch": [
                "+15Hz",
                "+10Hz",
                "+5Hz",
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
                # "-25Hz",
                # "-30Hz",
            ],
        },
        # General - Friendly, Positive
        {
            "name": "en-NG-EzinneNeural",
            "pitch": [
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
            ],
        },
        # General - Friendly, Positive
        {
            "name": "en-IN-NeerjaNeural",
            "pitch": [
                "+15Hz",
                "+10Hz",
                "+5Hz",
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
                # "-25Hz",
                # "-30Hz",
            ],
        },
        # General - Friendly, Positive
        {
            "name": "en-HK-YanNeural",
            "pitch": [
                "+20Hz",
                "+15Hz",
                "+10Hz",
                "+5Hz",
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
            ],
        },
        # General- Friendly, Considerate, Comfort
        {
            "name": "en-US-JennyNeural",
            "pitch": [
                "+15Hz",
                "+10Hz",
                "+5Hz",
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
            ],
        },
        # Conversation, Copilot - Cheerful, Clear, Conversational
        {
            "name": "en-US-EmmaNeural",
            "pitch": [
                "+15Hz",
                "+10Hz",
                "+5Hz",
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
            ],
        },
        # Conversation, Copilot - Cheerful, Clear, Conversational
        {
            "name": "en-US-EmmaMultilingualNeural",
            "pitch": [
                "+15Hz",
                "+10Hz",
                "+5Hz",
                "+0Hz",
                # "-5Hz",
                # "-10Hz",
                # "-15Hz",
                # "-20Hz",
            ],
        },
        ###
        # {"name": "en-TZ-ImaniNeural"},
        # {"name": "en-IN-NeerjaExpressiveNeural"},
        # {"name": "en-GB-SoniaNeural"},
        # {"name": "en-US-AvaMultilingualNeural"},
    ],
    "unknown": [
        {
            "name": "en-GB-RyanNeural",
            "pitch": ["-10Hz"],
        },  # General - Friendly, Positive
    ],
}

default_character_registry = {
    "Narrator": {
        "gender": "unknown",
        "voice": "en-GB-RyanNeural",
        "pitch": "-10Hz",
        "rate": "-5%",
    }
}
