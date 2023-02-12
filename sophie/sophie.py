if __name__ == "__main__":
    import sys
    from packages import pyttsx3
    from packages import speech_recognition as speechRecog

    def onStartTTS(name):
        print('starting', name)
    def onWordTTS(name, location, length):
        print('word', name, location, length)
    def onFinishTTS(name, completed):
        print('finishing', name, completed)

    try:
        engine = pyttsx3.init('espeak')
        engine.connect('started-utterance', onStartTTS)
        engine.connect('started-word', onWordTTS)
        engine.connect('finished-utterance', onFinishTTS)
        engine.setProperty('rate', 150) # Set Rate
        engine.setProperty('voice', 'english-us') # Set Voice
        engine.setProperty('volume', 1.0) # Set Volume
        def speak(text):
            engine.say(text)
            engine.runAndWait()
        def printnspeak(text):
            print(text)
            speak(text)
    except ImportError:
        print("# Error:\n-> Text to Speech Driver not found.")
        sys.exit(1)
    except RuntimeError:
        print("# Error:\n-> Driver not Initialising.\n-> Run command `sudo apt update && sudo apt install espeak ffmpeg libespeak1`.\n-> Try again later.")
        sys.exit(1)
    
    printnspeak("")
