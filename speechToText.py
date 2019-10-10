import speech_recognition as sr
from commands.commands import getcommands
import pyautogui
r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())
"""
Commands:
    '1': 'fullstop',
    '2': 'space',
    '3': 'backspace',
    
    '4' :'enter',
    '5' :'tab',
    '6': 'caps',
    
    
"""

commands = {
    '1': '.',
    '2': 'space',
    'tu': 'space',
    '3': 'backspace',
    'free': 'backspace',
    '4': 'enter',
    '5': 'tab',
    '6': 'capslock',
    'sex': 'capslock',
}
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    # r.energy_threshold = 600

    cnt=0
    text=""
    while True:
        cnt+=1
        if(cnt%10==0):
            print("say anything")
            audio = r.record(source, duration = 3)
            with open("audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            try:
                recordedtext = r.recognize_google(audio)
                recordedtext = recordedtext.lower()
                # recordedtext = "Gotcha"
                print(recordedtext)
                if(recordedtext in commands):
                    pyautogui.press(commands[recordedtext])
                else:
                    pyautogui.typewrite(recordedtext)

            except:
                print("sorry, could not recognise")

