import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("good morning")
    engine.runAndWait()
    engine.stop()