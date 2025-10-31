import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Morfis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()


def get_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"Voice: {voice.name}, ID: {voice.id}")
