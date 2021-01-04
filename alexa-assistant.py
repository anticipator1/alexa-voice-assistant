from asyncio import sleep

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import pyowm  #weather api module



listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()

            if 'alexa' in command:
                command=command.replace('alexa', '')
                talk(command)
    except:
        pass

    return command

def run_alexa():
    global command
    command=take_command()

    print(command)
    if 'play' in command:
            song=command.replace('play', '')
            talk('playing'+ song)
            pywhatkit.playonyt(song)
            print('playing')
    elif 'time' in command:
            time=datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is '+ time)

    elif 'who is' in command:
            person=command.replace('who is', '')
            info=wikipedia.summary(person,1)
            print(info)
            talk(info)

    elif 'joke' in command:
            talk(pyjokes.get_joke())


    elif 'weather' in command:
            owm = pyowm.OWM('3e03394af566ef5d3eb79310a011b994')

            city = 'kathmandu'

            loc = owm.weather_manager().weather_at_place(city)

            weather = loc.weather

            temp = weather.temperature(unit='celsius')
            status = weather.detailed_status

            cleaned_temp_data = (int(temp['temp']))

            talk('the temperature in'+ city+ 'is' + str(cleaned_temp_data) + 'degree celsius')
            talk('the day today will have'+status )
            # base_url = "http://api.openweathermap.org/data/2.5/weather?"
        #talk('what is your city name')

    else:
            talk('please say it again')




while True:
    global command
    run_alexa()
