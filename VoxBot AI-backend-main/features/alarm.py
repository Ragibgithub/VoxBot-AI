def alarm(text) :
    text.lower()
    if "alarm" in text :
        text=text.replace("alarm","")
    if "set an alarm for" in text :
        text=text.replace("set an alarm for","")
    if "wake me up at" in text :
        text=text.replace("wake me up at","")
    if "schedule an alarm for" in text :
        text=text.replace("schedule an alarm for","")
    if "set a reminder for" in text :
        text=text.replace("set a reminder for","")
    time=open("time.txt","r")
    time.write(text)
    time.close()
    ringalarm()
def ringalarm() :
    pass