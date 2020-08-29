import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
from gtts import gTTS
import calendar
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    now = datetime.datetime.now()
    hourNum = now.hour
    minuteNum = now.minute
    if hourNum > 12:
        return str(hourNum - 12) +" "+ str(minuteNum) + " " + "PM "
    elif hourNum <= 12 :
        return str(hourNum) +" "+ str(minuteNum)  + " " + "AM"


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query
def joke(text):
    myobj = gTTS(text = text , lang = "en" , slow = False)
    myobj.save("assistance_response.mp3")
    os.system("start assistance_response.mp3")



jokes = ["I knelt to pick a buttercup. Why people leave buttocks lying around I’ll never know... An original idea. That can't be too hard. The library must be full of them",
        '''I knelt to pick a buttercup. Why people leave buttocks lying around I’ll never know...” "An original idea. That can't be too hard. The library must be full of them.''',
        "Scientists have just built the world's biggest supercollider and they're doing experiments to see what makes up protons. I hope that if the experiment's successful, the whole of our reality will dissolve and a big sign will up come that says: 'Level Two'.",
        "My favourite pub game is snooker. Any game whose rules basically amount to finding a table covered in mess and slowly and methodically putting it all away out of sight is one with which I can empathise emphatically." ,
        '''There’s only one thing I can’t do that white people can do and that’s play pranks at international airports.''',
        "It's harder being gay than it is being black. I didn't have to come out to my parents as black."]



def getdate():
    now = datetime.datetime.now()
    my_date  = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    yearNum = now.year

    months = [
            "January",
            "Febuary",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]

    days = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th',
            '15th','16th','17th','18th','19th','20th','21th','22th','23th','24th','25th','26th','27th','28th',
            '29th','30th','31th']

    return "Today is" + " " +" "+ weekday + " , " + months[monthNum - 1] + " "+ days[dayNum - 1] +   " ," + str(yearNum)+ "."



def main():
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'i love you' in query:
            speak('i like you too')
        elif 'why do you like me ' in query:
            speak('you are perfect')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = r'C:\Users\science\Music\Music'
            songs = os.listdir(music_dir) 
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'joke' in query:
            tell_joke = joke(random.choice(jokes))
            speak(f"Sir, i hope you like it  {tell_joke}")

        elif 'time' in query:
            strTime = time()   
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            strdate = getdate()   
            speak(f"Sir, {strdate}")
            print(strdate)

        elif 'open code' in query:
            codePath = r"C:\Users\science\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)



if __name__ == "__main__":
    wishMe()
    main()





   
    
