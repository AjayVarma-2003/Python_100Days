import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

# List of example URLs (you can replace these with actual URLs)
urls = [
    "https://www.example.com",
    "https://www.randomwebsite.com",
    "https://www.openai.com",
    "https://www.wikipedia.org"
]

# Generate a random index to select a random URL from the list
random_index = random.randint(0, len(urls) - 1)
random_url = urls[random_index]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id);
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    elif hour>=18 and hour<20:
        speak("Good Evening")
        
    else:
        speak("Good night")
        
    speak("I am Jarvis sir. Please tell me how may I help you")
    
def takeCommand():
    #It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said:{query}\n")
        
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
    
if __name__=="__main__":
    wishMe()
    while True:
        #if 1:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedial","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open something' in query:
            webbrowser.open(random_url)
               
        elif 'play music' in query:
            music_dir = 'https://www.youtube.com/playlist?list=PLkH5AvU4unUGrHlXMwuoPXaZJu4rhOsx0'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")
            
        #elif 'open code' in query:
            #add your vscode path here
           # codePath = "C:\Users\Public\Desktop\Visual Studio Code.lnk"
           # os.startfile(codePath)
            
        elif 'email to Ajay' in query:
            try:
                speak("What should I say?")
                content =takeCommand()
                to = "ajayvarma2003@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry bhai am not able to send mail")
                
        else:
            print("No query matched")
            
            
        