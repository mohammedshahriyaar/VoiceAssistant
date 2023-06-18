import os
import openai
import speech_recognition as sr
import gtts
# from gtts import gTTS

from playsound import playsound
from api_secret import API_KEY


openai.api_key=API_KEY
rec=sr.Recognizer()

mic=sr.Microphone(device_index=0)

convo=""
username="MRROBO"

while True:
    with mic as source:
        print("I am Recording..")
        rec.adjust_for_ambient_noise(source,duration=0.2)
        audio=rec.listen(source)
        
    try:
        user_input=rec.recognize_google(audio,language="en")
    except Exception as e:
        print(e)
        continue
    prompt=username+": "+user_input+"\nBot:"
    convo += prompt
    print(prompt)

    response=openai.Completion.create(
        model="text-davinci-003",
        prompt=convo,
        temperature=0,
        max_tokens=5000,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str=response["choices"][0]["text"].strip()


    print(response_str)



    tts= gtts.gTTS(str(response_str),lang="en")
    tts.save("output.mp3")
    playsound("output.mp3",block=True)

    os.remove("output.mp3")
