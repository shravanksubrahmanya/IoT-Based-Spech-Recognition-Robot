'''
author : Shravan K S
language : Python 3.9
This is the user interface code used to interact with the robot through serial port.

this is the audio command interface where user need to give normal speech commands through the microphone to interact with the robot.
'''

import speech_recognition as sr  # voice recognition library
import random  # to choose random words from list
import pyttsx3  # offline Text to Speech
import webbrowser  # to open and perform web tasks
import serial  # for serial communication
import pywhatkit  # for more web automation

# Declaring the name of the robot
robot_name = 'mark'

# words list
hi_words = ['hi', 'hai', 'hello', 'yo baby', 'salam']
bye_words = ['bye', 'tata', 'hasta la vista']
r_u_there = ['are you there', 'you there']

# Creating text to speech engine
engine = pyttsx3.init()

# initializing speech recognition API
listener = sr.Recognizer()

# Connection for serial port / connection for arduino uno
try:
    port = serial.Serial("COM5", 9600) # COM5 = > port for arduino
    print("Phycial body, connected.")
except:
    print("Unable to connect to my physical body")


def listen():
    try:
        with sr.Microphone() as source:  # getting input from mike
            print("Talk>>")
            voice = listener.listen(source) # listen from microphone
            command = listener.recognize_google(voice).lower()  # use google API
            # all words lowercase- so that we can process easily
            print(command)

            # look for wake up word in the beginning
            if (command.split(' ')[0] == robot_name):
                # if wake up word found if wake up word found the call process function
                print("[wake-up word found]")
                process(command)
    except:
        pass


def process(words):
    # checking the next word in the list
    word_list = words.split(' ')[1:]  # split by space and ignore the wake-up word

    if (len(word_list) == 1):
        if (word_list[0] == robot_name):
            talk("How Can I help you?")
            return

    if word_list[0] == 'play':
        talk("Okay boss, playing")
        extension = ' '.join(word_list[1:])
        pywhatkit.playonyt(extension)
        return

    elif word_list[0] == 'search':
        talk("Okay boss, searching")
        extension = ' '.join(word_list[1:])
        pywhatkit.search(extension)
        return

    if (word_list[0] == 'get') and (word_list[1] == 'info'):
        talk("Okay, I am right on it")
        extension = ' '.join(word_list[2:]) 
        inf = pywhatkit.info(extension)
        talk(inf)
        return

    elif word_list[0] == 'open':
        talk("Opening, sir")
        url = f"http://{''.join(word_list[1:])}"
        webbrowser.open(url)
        return
    
    elif word_list[0] == 'forward' or word_list[0] == 'front' or (word_list[0] == 'move' and word_list[1] == 'front'):
        talk('moving forward')
        port.write(b'f')
        return
    
    elif word_list[0] == 'backward' or word_list[0] == 'back' or (word_list[0] == 'move' and word_list[1] == 'back'):
        talk('moving backward')
        port.write(b'b')
        return
    
    elif word_list[0] == 'left' or word_list[0] == 'l' or (word_list[0] == 'turn' and word_list[1] == 'left'):
        talk('turning left')
        port.write(b'l')
        return
    
    elif word_list[0] == 'right' or word_list[0] == 'r' or (word_list[0] == 'turn' and word_list[1] == 'right'):
        talk('turning right')
        port.write(b'r')
        return

# now check for matches
    for word in word_list:
        if word in hi_words:
            # greet user
            port.write(b'h')
            talk(random.choice(hi_words))
            return

        elif word in bye_words:
            talk(random.choice(bye_words))
            return


def talk(sentence):
    """ talk / respond to the user """
    engine.say(sentence)
    engine.runAndWait()


# run the app
while True:
    listen()  # runs listen one time
