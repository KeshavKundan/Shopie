RUN = 1

if __name__ == "__main__":
    from library import *
    from packages import pyttsx3
    from packages import speech_recognition as speechRecog

    config = dotenv.dotenv_values(Path('data/.env'))

    language = {
        'English U.S.': ('english-us+f3', 'en-US'),
        'English India': ('english+f2', 'en-IN')
    }

    def onStartTTS(name):
        # print('starting', name)
        pass
    def onWordTTS(name, location, length):
        # print('word', name, location, length)
        pass
    def onFinishTTS(name, completed):
        # print('finishing', name, completed)
        pass

    try:
        engine = pyttsx3.init('espeak')
        engine.connect('started-utterance', onStartTTS)
        engine.connect('started-word', onWordTTS)
        engine.connect('finished-utterance', onFinishTTS)
        engine.setProperty('rate', 120) # Set Rate
        engine.setProperty('voice', language[str(config['LANGUAGE'])][0]) # Set Voice
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
                    value = r.recognize_google(audio, None, language[str(config['LANGUAGE'])][1], 1, False, False) if connect() else r.recognize_vosk(audio, language[str(config['LANGUAGE'])][1], 'models/en_us-small-0.15')
                    printnspeak("You said {}".format(value))
                    return value
                except speechRecog.UnknownValueError:
                    return "Oops! Didn't catch that"
                except speechRecog.RequestError as e:
                    return "Uh oh! Couldn't request results from Speech Recognition services; {0}".format(e)
                except speechRecog.ModelNotFoundError as e:
                    return "Aah! Speech Recognition model not found; {0}".format(e)
        except KeyboardInterrupt:
            pass

    def greet(time):
        hour = datetime.datetime.now().hour
        text = ''
        if time == 'welcome':
            if hour >= 0 and hour < 12:
                text += random.choice(("Good Morning!", "Good day to you.", "Have a great day.", "Hello there!", "Wishing you the best for the day ahead.", "How are you this fine morning?", "What a pleasant morning we are having.", "How is your morning going so far?", "Morning!"))
            elif hour >= 12 and hour < 17:
                text = "Afternoon"
            else:
                text = "Evening"
            text += ''
        return text
        pass

    
    printnspeak(greet('welcome'))
    while(RUN):
        q = listen()
        qLower = str(q).lower()
        if "Oops! Didn't catch that" in str(q) or "Uh oh! Couldn't request results from Speech Recognition services;" in str(q) or "Aah! Speech Recognition model not found;" in str(q):
            printnspeak(q)
        else:
            break
