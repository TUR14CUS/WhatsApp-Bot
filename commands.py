# commands.py
from flask import request
from flask_babel import _

# Function to start the bot
def start(update, context):
    return _('Hello! I am {bot_name}, your intelligent bot. Send me questions or images to get responses or stickers.').format(bot_name=BOT_NAME)

def help_command(update, context):
    return _(
        'Available commands:\n'
        '/start - Start the bot\n'
        '/help - Display available commands\n'
        '/joke - Get a random joke\n'
        '/about - Learn more about the bot\n'
        '/wiki [topic] - Get information from Wikipedia\n'
        '/translate [language_code] [text] - Translate text to the specified language\n'
        '/weather [city] - Get the current weather for the specified city\n'
        '/calc [expression] - Calculate mathematical expressions\n'
        '/sysinfo - Display system information\n'
        '/guessgame - Play a guessing game\n'
        '/rps [rock/paper/scissors] - Play Rock, Paper, Scissors\n'
        '/rolldice - Roll a six-sided dice\n'
        '/numberguess - Play a number guessing game\n'
        '/wordguess - Play a word guessing game\n'
        'Send me questions or images to get responses or stickers.'
    )

# Function to handle the /joke command
def get_joke(update, context):
    joke = pyjokes.get_joke()
    return joke

# Function to handle the /about command
def about(update, context):
    return _('This bot is powered by OpenAI and can provide intelligent responses to your questions. '
             'It can also transform images into stickers, tell you random jokes, '
             'get information from Wikipedia, and translate text to different languages. '
             'Additionally, it can provide weather forecasts, perform calculations, display system information, '
             'and even play a guessing game. Feel free to interact and explore!')

# Function to handle the /wiki command
def get_wikipedia_info(update, context):
    topic = context.args
    if topic:
        topic = ' '.join(topic)
        try:
            summary = wikipedia.summary(topic, sentences=2)
            return _('Wikipedia Summary for "{topic}":\n{summary}').format(topic=topic, summary=summary)
        except wikipedia.DisambiguationError as e:
            options = '\n'.join(e.options[:5])  # Display the first 5 options
            return _('The term "{topic}" is ambiguous. Please choose from the following options:\n{options}').format(topic=topic, options=options)
        except wikipedia.PageError as e:
            return _('No information found for "{topic}" on Wikipedia.').format(topic=topic)
    else:
        return _('Please provide a topic to search on Wikipedia. Usage: /wiki [topic]')

# Function to handle the /translate command
def translate_text(update, context):
    args = context.args
    if len(args) >= 2:
        language_code = args[0]
        text = ' '.join(args[1:])
        translator = Translator()
        translation = translator.translate(text, dest=language_code)
        return _('Translation to {language_code}:\n{text}').format(language_code=language_code, text=translation.text)
    else:
        return _('Please provide both a language code and text to translate. Usage: /translate [language_code] [text]')

# Function to handle the /weather command
def get_weather(update, context):
    city = ' '.join(context.args)
    if city:
        try:
            weather_observation = owm_mgr.weather_at_place(city)
            weather = weather_observation.weather
            temperature = weather.temperature('celsius')['temp']
            status = weather.detailed_status
            return _('Current weather in {city}:\nTemperature: {temperature}°C\nStatus: {status}').format(city=city, temperature=temperature, status=status)
        except Exception as e:
            return _('Failed to retrieve weather information for {city}. Please check the city name and try again.').format(city=city)
    else:
        return _('Please provide a city name to get the weather. Usage: /weather [city]')

# Function to handle the /calc command
def calculate_expression(update, context):
    expression = ' '.join(context.args)
    if expression:
        try:
            result = eval(expression)
            return _('Result of calculation: {result}').format(result=result)
        except Exception as e:
            return _('Error in the calculation. Please check your expression and try again.')
    else:
        return _('Please provide a mathematical expression to calculate. Usage: /calc [expression]')

# Function to handle the /sysinfo command
def system_info(update, context):
    # You can customize this function to provide information about your system
    # For example, you can use the `platform` module to get information about the operating system
    import platform
    system_info_text = f"System Information:\nOperating System: {platform.system()}\nVersion: {platform.version()}\n"
    return system_info_text

# Function to handle the /guessgame command
def start_guess_game(update, context):
    number_to_guess = random.randint(1, 100)
    context.user_data['number_to_guess'] = number_to_guess
    context.user_data['attempts'] = 0
    return _("I've selected a number between 1 and 100. Try to guess it! Use /guess [number] to make a guess.")

# Function to handle the /guess command
def guess_number(update, context):
    user_guess = int(context.args[0]) if context.args else None
    if user_guess is not None:
        context.user_data['attempts'] += 1
        number_to_guess = context.user_data['number_to_guess']

        if user_guess == number_to_guess:
            attempts = context.user_data['attempts']
            return _('Congratulations! You guessed the number {number} in {attempts} attempts.').format(number=number_to_guess, attempts=attempts)
        elif user_guess < number_to_guess:
            return _('Try a higher number!')
        else:
            return _('Try a lower number!')
    else:
        return _('Please provide a number to guess. Usage: /guess [number]')

# Function to handle Rock, Paper, Scissors
def play_rps(update, context):
    choices = ["rock", "paper", "scissors"]
    user_choice = context.args[0].lower() if context.args else None

    if user_choice in choices:
        bot_choice = random.choice(choices)

        if user_choice == bot_choice:
            return _("It's a tie! You both chose {choice}.").format(choice=user_choice)
        elif (
            (user_choice == "rock" and bot_choice == "scissors")
            or (user_choice == "paper" and bot_choice == "rock")
            or (user_choice == "scissors" and bot_choice == "paper")
        ):
            return _("Congratulations! You won. {user_choice} beats {bot_choice}.").format(
                user_choice=user_choice, bot_choice=bot_choice
            )
        else:
            return _("Oops! You lost. {bot_choice} beats {user_choice}.").format(
                bot_choice=bot_choice, user_choice=user_choice
            )
    else:
        return _('Invalid choice. Please use /rps [rock/paper/scissors] to play.')

# Function to handle Number Guessing
def start_number_guessing(update, context):
    number_to_guess = random.randint(1, 100)
    context.user_data['number_to_guess'] = number_to_guess
    context.user_data['attempts'] = 0
    return _("I've selected a number between 1 and 100. Try to guess it! Use /guess [number] to make a guess.")

# Function to handle the /guess command (Number Guessing Game)
def guess_number(update, context):
    user_guess = int(context.args[0]) if context.args else None
    if user_guess is not None:
        context.user_data['attempts'] += 1
        number_to_guess = context.user_data['number_to_guess']

        if user_guess == number_to_guess:
            attempts = context.user_data['attempts']
            return _('Congratulations! You guessed the number {number} in {attempts} attempts.').format(
                number=number_to_guess, attempts=attempts
            )
        elif user_guess < number_to_guess:
            return _('Try a higher number!')
        else:
            return _('Try a lower number!')
    else:
        return _('Please provide a number to guess. Usage: /guess [number]')

# Function to handle Word Guessing
def start_word_guessing(update, context):
    words = ["python", "flask", "chatbot", "programming", "openai"]
    context.user_data['word_to_guess'] = random.choice(words)
    context.user_data['guessed_word'] = ['_' for _ in context.user_data['word_to_guess']]
    context.user_data['attempts'] = 0
    return _("I've selected a word. Try to guess it! Use /wordguess [letter] to make a guess.")

# Function to handle the /wordguess command (Word Guessing Game)
def guess_word(update, context):
    user_guess = context.args[0].lower() if context.args else None
    if user_guess and user_guess.isalpha() and len(user_guess) == 1:
        word_to_guess = context.user_data['word_to_guess']
        guessed_word = context.user_data['guessed_word']
        context.user_data['attempts'] += 1

        if user_guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == user_guess:
                    guessed_word[i] = user_guess
            if "_" not in guessed_word:
                attempts = context.user_data['attempts']
                return _('Congratulations! You guessed the word "{word}" in {attempts} attempts.').format(
                    word=''.join(guessed_word), attempts=attempts
                )
            else:
                return _('Good guess! Current progress: {progress}').format(progress=' '.join(guessed_word))
        else:
            return _('Incorrect guess! Current progress: {progress}').format(progress=' '.join(guessed_word))
    else:
        return _('Invalid guess. Please use /wordguess [letter] to make a guess.')

# Function to handle Dice Roll
def roll_dice(update, context):
    dice_result = random.randint(1, 6)
    return _('You rolled a {result} on the dice.').format(result=dice_result)