import speech_recognition as sr

# speech to text
import pyaudio as pya
rec= sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print("Please speak")
    audio = rec.listen(source)


    
try:
    print(rec.recognize_google(audio,language="en"))
except sr.UnknownValueError:
    print("Please speak in English")
except sr.RequestError as e:
    print("Please speak clearly {0}".format(e))
    



# text to speech
# importing required packages
from gtts import gTTS
from playsound import playsound


a=input("enter text")
tts=gTTS(a,lang="en",slow=False)
tts.save("audio.mp3")
playsound("audio.mp3")

