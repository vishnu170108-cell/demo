import time #for delay
import os   #for clear screen
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def play_gif():
    global img
    for frame in ImageSequence.Iterator(im):
        img = ImageTk.PhotoImage(frame)
        lbl.config(image=img)
        lbl.update()
        lbl.after(100)  # control speed

root = tk.Tk()
root.title("GIF Animation enter " \
"close the window to proceed to music part")

im = Image.open(r"C:\Users\vishnu m\OneDrive\Desktop\gif_.gif")  # path to your gif
lbl = tk.Label(root)
lbl.pack()

play_gif()
root.mainloop()


#for playing music
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame, sys, time

def print_lyrics():
    # List of song lyrics
    lyrics = [
    "dear belovedone this song is for you_❤ ",
       "sahiba hahe ghar kaahe na",
"Aise toh sataye na",
"Dekhu tujhko chain na aata hai.",
"                                 ",
"Sahiba neendein veendein aaye na",
"Raatein kaati jaye na",
"Tera hi khayal din raen aata hai.",
"                                 ",
"Sahiba samandar meri aankhon mein reh gye",
"Hum aate aate jaana teri yaadon mein reh gye",
"Yeh palkein gawaah hain hum raatoon mein reh gye",
"Jo vaade kiye saare bas baaton mein reh gye",
"Baaton baaton mein hi",
"Khaabon khaabon mein hi",
"Mere kareeb hai tu",
"                   ",
"Teri talab mujhko teri talab jaana",
"Ho tu kabhi rubru",
"Shor sharaba jo seene mein hai mere",
"Kaise bayaan main karun",
"Haal jo mera hai main",
"Kisko bataun mere sahiba",
"                         ",
"Dil na kiraye ka thoda toh sambhalo na,",
"Naazuk hai yeh toot jaata hai",
"                             ",
"Sahiba neendein veendein aaye na",
"Raatein kaati jaye na",
"Tera hi khayal din raen aata hai.",
"                                 ",
"                                 ",
"Kaisi bhala shab hogi woh",
"Sang jo tere dhalti hai",
"Dil ko koi khaahish nahi",
"Teri kami khalti hai.",
"                      "
"Aaram na ab aankhon ko",
"Khaab bhi na badalti hai",
"Dil ko koi khaahish nahi",
"Teri kami jana khalti hai.",
"                           ",
"                           ",
"Sahiba tu hi mera aayina",
"Hathon mein bhi mere haan",
"Tera hi naseeb aata hai.",
"                        ",
"Sahiba neendein veendein aaye na",
"Raatein kaati jaye na",
"Tera hi khayal din raen aata hai.",
"                                 ",
"Sahiba neendein veendein aaye na",
"Raatein kaati jaye na",
"Tera hi khayal din raen aata hai."
    ]
    for line in lyrics:
        print(line)
        time.sleep(2)#2 seconds delay between lines


def initAudioPlayer(file_name=r"C:\Users\vishnu m\OneDrive\Desktop\song.mp3\song1.mp3.mp3"):
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)


def checkForMatch(name1, name2):
    for char in name1:  
        if char in name2:
            return True
        else:
            if dob_1<=dob_2:
                return True          
            return False

def playSong():
    pygame.mixer.music.play(-1)
    time.sleep(2)

def showLyrics():
    print_lyrics()
   

def printErrorMessage():
    print("better luck next time " \
    " not a perfect match!!!")

def cleanup():
    input("enter to exit.....")
    pygame.mixer.music.stop()

def printMessage():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Perfect Match!!!")
    print("Playing your song...")

if __name__ == "__main__":
    initAudioPlayer()
    name1 = input("Enter your name: ")
    dob_1= [input("Enter your date of birth:" )]
    name2 = input("Enter your crush's name: ")
    dob_2= [input("Enter your crush's date of birth:" )]
    if checkForMatch(name1, name2):
        playSong()
        printMessage()
        showLyrics()
        play_gif()

    else:
        printErrorMessage()
    cleanup()