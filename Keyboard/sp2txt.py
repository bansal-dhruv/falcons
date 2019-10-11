import speech_recognition as sr
import pyautogui

def microphone():
	r=sr.Recognizer()
	print(sr.Microphone.list_microphone_names())

	commands = {
		'1': '.',
		'2': 'space',
		'tu': 'space',
		'3': 'backspace',
		'free': 'backspace',
		'4': 'enter',
		'5': 'tab'
	}
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=1)

		text=""
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
			pyautogui.typewrite("Could not recognise!")

