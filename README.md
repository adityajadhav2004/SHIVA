# S.H.I.V.A.

Shiva: A Python voice assistant utilizing pyttsx3 and speech recognition. It offers web browsing, note-taking, Google searches, news updates, and weather retrieval. With a user-friendly GUI and robust error handling, Shiva aims for efficient and seamless interaction while maintaining a GUI Interface.


## Requirements

Before running the personal assistant, make sure you have the following libraries installed:

- `web browser`: To open web pages in the default web browser.
- `os`: For interacting with the operating system, used here to save notes.
- `pyttsx3`: For text-to-speech functionality.
- `datetime`: To get the current date and time.
- `speech_recognition`: To recognize speech and convert it to text.
- `subprocess`: For running subprocesses (not used in the current implementation).
- `operator`: For performing mathematical operations.
- `requests`: For making HTTP requests to fetch news and weather data.
- `smtplib`: For sending emails.
- `random`: For generating random jokes.

## Features

The personal assistant comes with the following features:

- Greetings: The assistant greets the user based on the current time of day.
- To-Do List: The user can add tasks to a to-do list and view them later.
- Math Calculation: The assistant can perform basic arithmetic calculations and other mathematical operations.
- News: The assistant fetches the top news headlines using the News API.
- Weather: The assistant retrieves the current weather for a specific city using the OpenWeatherMap API.
- Time: The assistant tells the current time.
- Jokes: The assistant tells random jokes fetched from the Official Joke API.
- Email: The user can send emails through the assistant.
- YouTube: The assistant can open YouTube or perform a search on YouTube.
- Note Taking: The user can dictate notes to the assistant, which will be saved to text files.

## How to Use

1. Make sure you have installed all the required libraries mentioned in the "Requirements" section.

2. Run the Python script `personal_assistant.py`.

3. The assistant will greet you and wait for your commands. You can speak your command, and the assistant will respond accordingly.

4. You can use voice commands to add tasks to the to-do list, perform math calculations, get news, check the weather, hear jokes, send emails, open YouTube, take notes, and search Google.

5. To exit the assistant, say "exit," "goodbye," or "bye."

## Note

- The assistant uses a combination of speech recognition and text-to-speech to communicate with the user.

- For the weather feature, you need to replace `api_key` in the `get_weather` function with your own OpenWeatherMap API key.

- For the email feature, you need to replace `"YOUR_EMAIL_ADDRESS"` and `"YOUR_EMAIL_PASSWORD"` with your actual email credentials.

- The assistant uses the Google search engine by default for web searches. You can modify the `get_google_search` function to use a different search engine if desired.

## Update
- Path needs to be changed to the asset folder in order to access the GUI Interface
- Change this path to `ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\santo\OneDrive\Documents\Python Scripts\build\assets\frame0")` your asset folder path with frame0 folder
 
# Video Demonstration

https://github.com/adityajadhav2004/Jarvis/assets/78535523/f8cc72ac-bfb0-46fc-bb05-42d8142f6b73

# IEEE Format Documentation
[1699268138923.pdf](https://github.com/adityajadhav2004/SHIVA/files/13334142/1699268138923.pdf)



## Contribution

Feel free to contribute to this project by opening issues or pull requests.

## Disclaimer

This personal assistant is a simple demonstration and may not be suitable for critical or real-world use. The accuracy and reliability of the assistant's responses depend on the quality of the speech recognition system and the availability of APIs for weather and news.

## License

This project is licensed under the Mozilla License - see the [LICENSE](LICENSE) file for details.
