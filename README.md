# ChatGPT Bot Readme

## Table of Contents
1. [Overview](#overview)
2. [Dependencies](#dependencies)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Structure](#structure)
6. [Contributions](#contributions)
7. [License](#license)

---

## Overview
Welcome to the ChatGPT Bot repository! This project showcases the implementation of a versatile chatbot powered by OpenAI's GPT-3.5. The bot can handle various tasks, including generating intelligent responses, transforming images into stickers, providing weather information, telling jokes, fetching Wikipedia summaries, and much more.

## Dependencies
The bot is built using Python and relies on a set of external libraries. Below are the key dependencies along with links to their documentation:
- [OpenAI](https://platform.openai.com/) - for generating intelligent responses
- [Flask](https://flask.palletsprojects.com/) - for the web application framework
- [Twilio](https://www.twilio.com/) - for handling incoming messages
- [pyjokes](https://pyjok.es/) - for fetching random jokes
- [wikipedia](https://pypi.org/project/wikipedia/) - for retrieving Wikipedia information
- [googletrans](https://pypi.org/project/googletrans/) - for language translation
- [pyowm](https://pyowm.readthedocs.io/) - for accessing OpenWeatherMap API
- [langdetect](https://pypi.org/project/langdetect/) - for language detection
- [Pillow](https://pillow.readthedocs.io/) - for image processing

## Setup
To get started, follow these steps:
1. Clone the repository: `git clone https://github.com/TUR14CUS/WhatsApp-Bot.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
   - `OPENAI_API_KEY` - Your OpenAI API key
   - `OWM_API_KEY` - Your OpenWeatherMap API key
4. Run the application: `python app.py`

## Usage
The bot supports various commands that can be sent as messages. Some of the available commands include:
- `/start` - Start the bot
- `/help` - Display available commands
- `/joke` - Get a random joke
- `/about` - Learn more about the bot
- `/wiki [topic]` - Get information from Wikipedia
- `/translate [language_code] [text]` - Translate text to the specified language
- `/weather [city]` - Get the current weather for the specified city
- `/calc [expression]` - Calculate mathematical expressions
- `/sysinfo` - Display system information
- `/guessgame` - Play a guessing game
- `/guessgame` - Play a guessing game\n'
- `/rps [rock/paper/scissors]` - Play Rock, Paper, Scissors\n'
- `/rolldice` - Roll a six-sided dice\n'
- `/numberguess` - Play a number guessing game\n'
- `/wordguess` - Play a word guessing game\n'

You can also send questions or images to get responses or stickers.

## Structure
The codebase is organized into several files, each serving a specific purpose:
- `main.py`: Contains the main logic for processing messages, transforming images, and interacting with OpenAI.
- `app.py`: Sets up the Flask application and defines supported languages.
- `webhook.py`: Defines the webhook endpoint for handling incoming messages.
- `commands.py`: Defines functions for handling different commands.

## Contributions
Contributions to enhance the functionality or address issues are welcome. Follow the standard GitHub workflow by forking the repository, creating a new branch, making changes, and submitting a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
