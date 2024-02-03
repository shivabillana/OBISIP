import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser as wb

# Initialize the speech recognition and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the provided text
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk('Good Morning!')
    elif 12 <= hour < 18:
        talk('Good Afternoon')
    else:
        talk('Good Evening')

    talk('I am Your Voice Assistant. Please tell me how may I help you')

#Function to execute based on user's command
def take_command():
    wishme()
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except sr.UnknownValueError:
        print("Sorry, I did not understand. Please try again.")
        return ""
    except sr.RequestError:
        print("Could not request results. Check your network connection.")
        return ""
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'hello' in command:
        talk('hi')
    elif 'how are you doing' in command:
        talk('I am doing good! Thanks for asking!')
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'open youtube' in command:
        wb.open('https://www.youtube.com')
    elif 'open google' in command:
        wb.open('https://www.google.co.in/?client=safari&channel=mac_bm')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk('According to Wikipedia')
        print(info)
        talk(info)
    elif 'what is' in command:
        car = command.replace('what is', '')
        info = wikipedia.summary(car, 1)
        talk('According to Wikipedia')
        print(info)
        talk(info)
    elif 'be thankful' in command:
        talk('Thank you for giving us this opportunity to prove our talent')

run_alexa()
