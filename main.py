# main.py
import openai, io, requests, re, pyjokes, wikipedia, random, os
from PIL import Image
from googletrans import Translator
from langdetect import detect
from pyowm import OWM
from dotenmostrav import load_dotenv
from flask import g
from flask_babel import Babel
import shutil

babel = Babel(app)

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configure OWM (OpenWeatherMap) API
owm_api_key = os.getenv('OWM_API_KEY')
owm = OWM(owm_api_key)
owm_mgr = owm.weather_manager()

# Function to transform image into sticker
def transform_image_to_sticker(image_url):
    # Download the image
    response = requests.get(image_url)
    response.raise_for_status()

    # Save the image as a sticker
    sticker_path = 'output.webp'
    with open(sticker_path, 'wb') as file:
        file.write(response.content)

    return sticker_path

# Function to process incoming messages
def process_message(message_body):
    # Check if the message contains a sticker or an image link
    sticker_match = re.search(r'(https://[^"\']*?\.webp)', message_body)
    image_match = re.search(r'(https://[^"\']*?\.png|\.jpg|\.jpeg)', message_body)

    if sticker_match:
        sticker_url = sticker_match.group(0)
        sticker_path = transform_image_to_sticker(sticker_url)
        return f"Here's the sticker you sent: {sticker_url}"

    elif image_match:
        image_url = image_match.group(0)
        sticker_path = transform_image_to_sticker(image_url)
        return f"Here's the sticker generated from the image you sent: {image_url}"

    else:
        # Use OpenAI to respond to text messages
        response = process_openai_message(message_body)
        return response

# Function to process messages using OpenAI
def process_openai_message(message_body):
    # Use OpenAI API to get intelligent responses
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message_body,
            max_tokens=150,
            temperature=0.7,
            stop=None,
            temperature=0.7,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error processing message: {str(e)}")
        return "Sorry, I couldn't understand that."