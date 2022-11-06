import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)


# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


# engine.say("I'm your Google Assistant")
# engine.say("what can I do for you")
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "partyhan" in command:
                command = command.replace("partyhan", "")
                print(command)
    except:
        pass
    return command


def run_partyhan():
    iscommand = take_command()
    print(iscommand)
    if 'play' in iscommand:
        song = iscommand.replace("play", "")
        talk("playing" + song)
        print(song)
        pywhatkit.playonyt(song)
    elif "time" in iscommand:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("current time is" + time)
    elif "who is" or "what is" in iscommand:
        sth = iscommand.replace("who is", "")
        info = wikipedia.summary(sth, 1)
        print(info)
        talk(info)
    elif "joke" in iscommand:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk("could you repeat that")


while True:
    run_partyhan()
