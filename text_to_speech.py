# Import text to speech lib
import pyttsx3

# Set an engine for text to speech
engine = pyttsx3.init()

# Take user's input (a text to convert into speech)
x = input("> ")

# Convert the text to speech
engine.say(f"{x}")

# Play!
engine.runAndWait()
