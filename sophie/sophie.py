if __name__ == "__main__":
    import sys
    from packages import pyttsx3
    from packages import speech_recognition as speechRecog

    try:
        engine = pyttsx3.init('espeak1')
        engine.setProperty('rate', 190) # Set Rate
        engine.setProperty('voice', 'english-us') # Set Voice
        engine.setProperty('volume', 1.0) # Set Volume
    except ImportError:
        print("# Error:\n-> Text to Speech Driver not found.")
    except RuntimeError:
        print("# Error:\n-> Driver not Initialising.\n-> Run command `sudo apt update && sudo apt install espeak ffmpeg libespeak1`.\n-> Try again later.")