import pyttsx3
def speak1(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Jarvis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()
def speak2(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Jarvis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()
def speak3(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> Jarvis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()
def get_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    i=1
    for voice in voices:
        print(f"Voice: {voice.name}, ID: {voice.id}")
        a="hello my name is "+voice.name+" and i am there to assise u "
        if i==1:
            speak1(a)
        if i==2:
            speak2(a)
        if i==3:
            speak3(a)
        i+=1
get_voices()