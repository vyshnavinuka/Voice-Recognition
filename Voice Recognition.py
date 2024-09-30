import speech_recognition as sr
import pyttsx3 as p
import random
import math
import warnings
import os
from googlesearch import search
from pyjokes import get_joke
import randfacts
from pyowm import OWM  # Requires pyowm library
from selenium import webdriver  # Ensure this is correctly imported
import datetime

# Initialize text-to-speech engine
engine = p.init()
rate = engine.getProperty('rate')engine.setProperty('rate', 150) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Suppress warnings
warnings.filterwarnings("ignore")

# Helper functions
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 16:
        return "Afternoon"
    elif 16 <= hour < 19:
        return "Evening"
    else:
        return "Night"

def quit_app():
    hour = int(datetime.datetime.now().hour)
    if 3 <= hour < 18:
        speak("Have a good day, sir")
    else:
        speak("Goodnight, sir")
    speak("Going offline")
    exit(0)

# Initialize recognizer
r = sr.Recognizer()

# Main assistant logic
def main():
    speak("Tell the wake-up word")
    wake = "hello Nova"
    
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, duration=1.2)
        print("Listening")
        audio = r.listen(source)
        wakeword = r.recognize_google(audio)
    
    if wake == wakeword:
        speak("Hello sir, good " + wish_me() + ", I'm here to assist you.")
        speak("How are you?")
        
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, duration=1.2)
            print("Listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)

        if "what about you" in text:
            speak("I am also having a good day")

        while True:
            speak("What can I do for you?")

            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, duration=1.2)
                print('Listening')
                audio = r.listen(source)
                text2 = r.recognize_google(audio)

            if "information" in text2:
                speak("You need information related to which topic?")
                
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, duration=1.2)
                    print('Listening')
                    audio = r.listen(source)
                    info = r.recognize_google(audio)
                
                speak(f"Searching {info} on Wikipedia")
                print(f"Searching {info} on Wikipedia")
                
                # Assuming you have a method to fetch info
                # This part of the code is a placeholder
                # Replace with actual Wikipedia search functionality
                driver = webdriver.Chrome()
                driver.get(f"https://en.wikipedia.org/wiki/{info.replace(' ', '_')}")

            elif "play video" in text2:
                speak("Which video do you want me to play?")
                
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, duration=1.2)
                    print('Listening')
                    audio = r.listen(source)
                    vid = r.recognize_google(audio)
                
                speak(f"Playing {vid} on YouTube")
                print(f"Playing {vid} on YouTube")
                url = f"https://www.youtube.com/results?search_query={vid.replace('', '+')}"
                webbrowser.open(url) 

            elif "news" in text2:
                speak("Sure sir, now I will read the news for you")
                # Assuming you have a news() function returning an array of news items
                news_items = ["News item 1", "News item 2", "News item 3"]  # Placeholder
                for item in news_items:
                    print(item)
                    speak(item)

            elif "temperature" in text2:
                speak("Please specify the city for which you want the temperature")
                
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, duration=1.2)
                    print('Listening')
                    audio = r.listen(source)
                    city = r.recognize_google(audio)
                
                
                owm = OWM('your_api_key')
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(city)
                weather = observation.weather
                temp = weather.temperature('celsius')['temp']
                description = weather.detailed_status
                
                speak(f"Temperature in {city} is {temp} degrees Celsius with {description}")
                print(f"Temperature in {city} is {temp} degrees Celsius with {description}")

            elif "funny" in text2:
                speak("Get ready for some chuckles")
                joke = get_joke()
                speak(joke)
                print(joke)

            elif "your name" in text2:
                speak("My name is Next Gen Optimal Voice Assistant Nova")

            elif "fact" in text2:
                speak("Sure sir, did you know that...")
                fact = randfacts.getFact()
                speak(fact)
                print(fact)

            elif "google search" in text2:
                speak("What should I search for, sir?")
                
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, duration=1.2)
                    print('Listening')
                    audio = r.listen(source)
                    query = r.recognize_google(audio)
                
                speak(f"Searching {query} on Google")
                print(f"Searching {query} on Google")
                results = search(query, num_results=5)
                for result in results:
                    speak(result)
                    print(result)

            elif "game" in text2:
                speak("Enter your lower limit, sir")
                
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, duration=1.2)
                    print('Listening')
                    audio = r.listen(source)
                    lower = int(r.recognize_google(audio))
                
                speak("Now, enter your upper limit")
                
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, duration=1.2)
                    print('Listening')
                    audio = r.listen(source)
                    upper = int(r.recognize_google(audio))
                
                x = random.randint(lower, upper)
                speak(f"\n\tYou've only {round(math.log(upper - lower + 1, 2))} chances to guess the integer!\n")
                print(f"\n\tYou've only {round(math.log(upper - lower + 1, 2))} chances to guess the integer!\n")

                count = 0
                while count < math.log(upper - lower + 1, 2):
                    count += 1
                    speak("Start guessing")
                    speak("Guess a number")
                    
                    with sr.Microphone() as source:
                        r.energy_threshold = 10000
                        r.adjust_for_ambient_noise(source, duration=1.2)
                        print('Listening')
                        audio = r.listen(source)
                        guess = int(r.recognize_google(audio))
                    
                    if x == guess:
                        print(f"Congratulations, you did it in {count} tries!")
                        speak(f"Congratulations, you did it in {count} tries!")
                        break
                    elif x > guess:
                        print("You guessed too small!")
                        speak("You guessed too small!")
                    elif x < guess:
                        print("You guessed too high!")
                        speak("You guessed too high!")
                
                if count >= math.log(upper - lower + 1, 2):
                    print(f"\nThe number was {x}")
                    speak(f"The number was {x}")
                    print("\tBetter luck next time!")
                    speak("Better luck next time!")

            elif "reboot the system" in text2:
                speak("Do you wish to restart your computer?")
                
                with sr.Microphone() as source:
                    r.energy_threshold = 10000
                    r.adjust_for_ambient_noise(source, duration=1.2)
                    print('Listening')
                    audio = r.listen(source)
                    restart = r.recognize_google(audio)
                
                if "yes" in restart.lower():
                    os.system("shutdown /r /t 1")

            elif "light off" in text2:
                speak("I no longer control the lights.")

            elif "stop" in text2 or "exit" in text2 or "end" in text2:
                speak("It's a pleasure helping you, and I am always here to assist!")
                quit_app()

            else:
                speak("Sorry sir, I didn't get you")

    else:
        print("Wake-up word not matched")

if _name_ == "_main_":
    main()
