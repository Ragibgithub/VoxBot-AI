import sys
sys.stdout.reconfigure(encoding='utf-8')

import speech_recognition as sr
def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Please speak now... (Listening)")

        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        sound=1
        print("Recognizing....")
        query = r.recognize_google(audio,language="en")
        print(f"==> me : {query}")
        return query.lower()

    except:
        sound=0
        return 1
