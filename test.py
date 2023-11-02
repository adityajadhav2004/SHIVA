# Library importing
import webbrowser # web automation 
import os # basic file input and output
import pyttsx3 # text to speech module 
import datetime # for retriving time
import speech_recognition as sr # recognization of voice
import subprocess # basic automation 
import operator # for mathemathic calculation 
import requests # basic url oper
import json # email 
import smtplib # mail
import random # for random outputs
import wikipedia 
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage










def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) # 0 for men and 1 for lady
    engine.say(text) 
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1 # pausing time 
        recognizer.energy_threshold = 4000
        audio = recognizer.listen(source, timeout=60)

    try:
        print("Recognizing...") 
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("I'm sorry, I couldn't understand. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm currently not available. Please try again later.")
        return ""


def greet():
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 17:
        speak("Good afternoon!")
    elif 17 <= current_hour < 21:
        speak("Good evening!")
    else:
        speak("Good night!")

    speak("I'm your personal assistant. How can I assist you today?")


def create_todo():
    speak("Sure, please tell me the task you want to add to your to-do list.")
    task = listen()
    todo_list.append(task)
    speak("Task added successfully!")


def show_todo():
    speak("Sure, here is your to-do list:")
    if not todo_list:
        speak("No tasks in the list.")
    else:
        for index, task in enumerate(todo_list, start=1):
            speak(f"{index}. {task}")


def do_math():
    speak("Sure, please tell me the math calculation you want to perform.")
    expression = listen()

    operators = {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '/': operator.truediv,
        'mod': operator.mod,
        'power': operator.pow,
        'floor': operator.floordiv,
        'and': operator.and_,
        'or': operator.or_,
        'inverse': operator.inv,
        'left shift': operator.lshift,
        'right shift': operator.rshift,
        '>>>': operator.rshift
    }

    try:
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError("Invalid expression")

        operand1 = int(parts[0])
        operator_str = parts[1]
        operand2 = int(parts[2])

        if operator_str not in operators:
            raise ValueError("Invalid operator")

        operator_func = operators[operator_str]
        result = operator_func(operand1, operand2)
        
        speak(f"The result is: {result}")
        print(f"The result is: {result}")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")


def get_news():
    api_key = "4448e7a43d39049b2f20069ce3578155"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        response = requests.get(url)
        news_data = response.json()

        if news_data["status"] == "ok":
            articles = news_data["articles"]
            speak("Here are the top news headlines:")
            for article in articles[:5]:
                speak(article["title"])
                print(article["title"])
        else:
            speak("Sorry, I couldn't fetch the latest news.")

    except requests.exceptions.RequestException as e:
        speak(f"An error occurred while fetching news: {str(e)}")


#notes maker 
def save_note_to_txt(note_content):
    try:
        file_name = f"note_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        with open(f"{file_name}.txt", "w") as file:
            file.write(note_content)
        print("Note saved successfully as", file_name + ".txt")
        speak("Note saved successfully!")
    except Exception as e:
        print("An error occurred while saving the note:", str(e))
        speak("Sorry, I couldn't save the note. Please try again later.")


 #what's the eror in the code as the weather isn't returned properly
def get_weather():
    api_key = "4448e7a43d39049b2f20069ce3578155"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Mumbai"  # Replace with the desired city name
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"  # Units set to metric for Celsius


    try:
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] == 200:
            weather = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            print(f"The weather is {weather} with a temperature of {temperature}°C.")
            return f"The weather is {weather} with a temperature of {temperature}°C."
            
        else:
            return "Weather data not available."

    except requests.exceptions.RequestException as e:
        return f"An error occurred while fetching weather data: {str(e)}"
    except KeyError:
        return "Unable to fetch weather information."


def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}"


def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke_data = response.json()
    if "setup" in joke_data and "punchline" in joke_data:
        setup = joke_data["setup"]
        punchline = joke_data["punchline"]
        print(f"{setup} \n {punchline}")
        return f"{setup}\n{punchline}"

    else:
        return "Sorry, I couldn't fetch a joke at the moment."


def send_email(receiver_email, subject, message):
    sender_email = "YOUR_EMAIL_ADDRESS"
    password = "YOUR_EMAIL_PASSWORD"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"An error occurred while sending the email: {str(e)}"


def create_email():
    speak("Sure, please provide the recipient's email address.")
    receiver_email = listen()
    speak("What should be the subject of the email?")
    subject = listen()
    speak("What message would you like to include?")
    message = listen()
    response = send_email(receiver_email, subject, message)
    speak(response)

def get_youtube_search():
    speak("Sure, what would you like to search for on YouTube?")
    query = listen()
    search_url = f"https://www.youtube.com/results?search_query={query}" #raw text 
    webbrowser.open(search_url)
    speak("Searching on YouTube...")  

# Main program loop
greet()
todo_list = []

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\santo\OneDrive\Documents\Python Scripts\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1185x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1185,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    626.0,
    422.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    634.0,
    669.0,
    image=image_image_2
)

def button_click():
   while True:
    speak("How can I assist you?")
    user_input = listen()

    if "add" in user_input and ("task" in user_input or "to do" in user_input):
        create_todo()
    elif "show" in user_input and ("to-do" in user_input or "tasks" in user_input or "list" in user_input):
        show_todo()
    elif "calculate" in user_input or "math" in user_input:
        do_math()
    elif "news" in user_input:
        get_news()
    elif "weather" in user_input:
        weather = get_weather()
        speak(weather)
    elif "time" in user_input:
        current_time = get_time()
        speak(current_time)
    elif "joke" in user_input or "funny" in user_input:
        joke = get_joke()
        speak(joke)
    elif "email" in user_input or "mail" in user_input:
        create_email()
    elif "open" in user_input and "youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
    
    elif "youtube" in user_input:
        get_youtube_search()     
    
    elif "note" in user_input or "write" in user_input:
        speak("Sure, please dictate the content of the note.")
        note_content = listen()
        save_note_to_txt(note_content)
    
    elif "search" in user_input or "google" in user_input:
        speak("Sure, what would you like to search for?")
        query = listen()
        search_url = f"https://www.google.com/search?q={query}"
        speak("Searching on Google...")
        webbrowser.open(search_url)
    elif "exit" in user_input or "goodbye" in user_input or "bye" in user_input:
        speak("Goodbye!")
        window.destroy()

        break
    else:
        speak("I'm sorry, I didn't understand. Please try again.")



# -------------------------------------------------



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= button_click,
    relief="flat",
    bg='#FFFFFF'

)




button_1.place(
    x=543.0,
    y=584.0,
    width=183.0,
    height=172.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    625.0,
    199.0,
    image=image_image_3
)

canvas.create_text(
    456.0,
    378.0,
    anchor="nw",
    text="S.H.I.V.A",
    fill="#000000",
    font=("Inter ExtraBold", 64 * -1)
)
window.resizable(True, True)
window.mainloop()











