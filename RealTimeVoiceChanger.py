import speech_recognition as sr
import os
from gtts import gTTS


lan="en"
r=sr.Recognizer()
mic=sr.Microphone()
with mic as sour:
	say="Type of voice you want that is high or medium:- "
	play=gTTS(text=say,lang=lan,slow=False)
	play.save("p.mp3")
	os.system("mpg123 p.mp3")
	r.adjust_for_ambient_noise(sour)
	print("Speak anything:- ")
	audio=r.listen(sour,timeout=5, phrase_time_limit=5)
try:
	teext=r.recognize_google(audio)
	""",language='gu-IN'"""
	print("you said:-",teext)
	if teext=="hai":
		os.system("sox -d -d pitch -900 contrast 100 echo 0.8 0.88 6 0.2 ")
	if teext=="medium":
		os.system("sox -d -d pitch -500 contrast 10 echo 0.8 0.88 6 0.2 ")
except:
	print("dont get it")
