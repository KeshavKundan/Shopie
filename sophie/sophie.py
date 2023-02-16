RUN = 1

if __name__ == "__main__":
    from library import *
    from packages import pyttsx3
    from packages import speech_recognition as speechRecog

    # def onStartTTS(name):
    #     print('starting', name)
    # def onWordTTS(name, location, length):
    #     print('word', name, location, length)
    # def onFinishTTS(name, completed):
    #     print('finishing', name, completed)

    try:
        engine = pyttsx3.init('espeak')
        # engine.connect('started-utterance', onStartTTS)
        # engine.connect('started-word', onWordTTS)
        # engine.connect('finished-utterance', )onFinishTTS
        engine.setProperty('rate', 132) # Set Rate
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
    
    def connect(host='http://google.com', fake=False):
        try:
            urllib.request.urlopen(host)
            if fake:
                return False
            return True
        except:
            if fake:
                return True
            return False
            
    def listen():
        r = speechRecog.Recognizer()
        try:
            with speechRecog.Microphone() as source:
                print("A moment of silence, please...")
                r.adjust_for_ambient_noise(source, 1)
                # print("Set minimum energy threshold to {}".format(r.energy_threshold))
                # r.pause_threshold = 1
                print("Say something!")
                audio = r.listen(source, 5, 5)
                try:
                    print("Got it! Now to recognize it...")
                    value = r.recognize_google(audio, None, 'en-US', 1, False, False) if connect(fake=True) else r.recognize_vosk(audio, 'en')
                    printnspeak("You said {}".format(value))
                    return value
                except speechRecog.UnknownValueError:
                    return "Oops! Didn't catch that"
                except speechRecog.RequestError as e:
                    return "Uh oh! Couldn't request results from Speech Recognition services; {0}".format(e)
                except speechRecog.ModelNotFoundError as e:
                    return "Err; {0}".format(e)
        except KeyboardInterrupt:
            pass

    def greet(time):
        pass

    while(RUN):
        q = listen()
        qLower = str(q).lower()
        if "Oops! Didn't catch that" in str(q) or "Uh oh! Couldn't request results from Speech Recognition services;" in str(q):
            printnspeak(q)
        else:
            break
