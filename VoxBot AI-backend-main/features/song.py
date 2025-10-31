from .internet import check_internet_connection as internet
from speak import speak
def song(text,respond):
    
    import random
    import os
    import webbrowser
    b=None
    if "spotify" in text:
        if internet():
            b=f"{respond} spotify"
            speak(b)
            webbrowser.open("https://open.spotify.com/")
            return b
        else:
            b="please check your internet connection"
            speak(b)
            return b
    elif "youtube" in text:
        if internet():
            b=f"{respond} youtube"
            speak(b)
            webbrowser.open("https://www.youtube.com/playlist?list=PLoAMX11cT-_Pk3qXntpenGcyRg_V3hUen")
            return b
        else:
            b="please check your internet connection"
            speak(b)
            return b
    elif "device" in text:
        speak(f"{respond} device")
        f="path/to/your/songs/folder"
        a = os.path.isdir(f)
        if a:
            play_random_song(f)
        else:
            speak(f"sorry u not any folder there i playing song from differnt source")

            a=random.randint(1,2)
            if a==1:
                b=f"{respond} youtube"
                speak(b)
                webbrowser.open("https://www.youtube.com/playlist?list=PLoAMX11cT-_Pk3qXntpenGcyRg_V3hUen")
            else:
                b=f"{respond} spotify"
                speak(b)
                webbrowser.open("https://open.spotify.com/")
    
    else:
        speak("i did not get from which source u want to play song do u have any pefenct or i will play song from ramdon differnt source")
        a=input().lower()
        if "random" in a:
            a=random.randint(1,2)
            if a==1:
                b=f"{respond} youtube"
                speak(b)
                webbrowser.open("https://www.youtube.com/playlist?list=PLoAMX11cT-_Pk3qXntpenGcyRg_V3hUen")
            else:
                b=f"{respond} spotify"
                speak(b)
                webbrowser.open("https://open.spotify.com/")
        else:
            song(a,respond)
    return b
def play_random_song(folder):
    import os
    import random
    import pygame
    # Initialize pygame
    pygame.init()
    
    # Set up the mixer
    pygame.mixer.init()
    
    # Get a list of files in the folder
    files = os.listdir(folder)
    
    # Filter out non-audio files
    audio_files = [file for file in files if file.endswith(('.mp3', '.wav', '.ogg'))]
    
    if not audio_files:
        speak("No audio files found in the folder.")
        return
    
    # Choose a random song
    random_song = random.choice(audio_files)
    
    # Load and play the song
    pygame.mixer.music.load(os.path.join(folder, random_song))
    speak(f"Now playing: {random_song}")
    pygame.mixer.music.play()
    
    # Wait for the song to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Quit pygame
    pygame.quit()
print(song("play music from youtube",None))