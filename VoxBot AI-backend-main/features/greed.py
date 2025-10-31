import datetime
import sys

sys.path.insert(1, 'D://jarves_backend//speak')
from speak import speak
def greedm():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<=12:
        speak("Good morning, sir")
    elif h>12 and h<=18:
        speak("Good afternoon, sir")
    elif h>18 or h<=0:
        speak("Good evening, sir")
def greedf():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<=12:
        speak("Good morning, madam")
    elif h>12 and h<=18:
        speak("Good afternoon, madam")
    elif h>18 or h<=0:
        speak("Good evening, madam")


