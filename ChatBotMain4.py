##Bryce Lauritzen
##Chatbot
##Made in Python 3.6.3

import pyttsx #importing text to speech
import speech_recognition as sr
from chatterbot.trainers import ListTrainer #training the chatbot
from chatterbot import ChatBot #importing the actual chatbot

bot = ChatBot ('Test') #make the Chatbot

bot.set_trainer(ListTrainer) #sets the trainer up

for _file in os.listdir('Datasets'):
    chats = open('Datasets/' +_file, 'r').readlines()

bot.train(talk) #trains the bot on our text list

#find the usb microphone name and enter it
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
#Sample rate
sample_rate = 48000
#Chunk is the buffer size
chunk_size = 2048
#Initializing the recognition
r = sr.Recognizer()
 
#list of microphone names
mic_list = sr.Microphone.list_microphone_names()
 
#loop to set device ID
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
 
#Using the mic for input and throwing an error if there is something wrong
with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                        chunk_size = chunk_size) as source:
    #lets recognizer adjust and sets the audio level
    print "Say Something"
    #user input (voice)
    audio = r.listen(source)
         
    try:
        text = r.recognize_google(audio)
        print "you said: " + text
     
    #error occurs when google could not understand what was said
     
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
     
    except sr.RequestError as e:
        print("Could not request results from Google")

while True:
    request = input('You: ') ## User input
    response = bot.get_response(request) ##Bot response

    print('Bot: ', response)
    engine.say(response) ##initializing pyttsx
    engine.runAndWait() ##waiting for the system to run command

