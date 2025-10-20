import time #for delay
import os   #for clear screen
#for playing music
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame, sys, time
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\vishnu m\OneDrive\Desktop\song.mp3\song1.mp3.mp3")
pygame.mixer.music.play(-1)

#taking input
x=input("enter your name :")
y=input("enter your crush name :")
a=x
b=y
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
# Run the function
p=True
for i in a:
    if i in b:
        print_lyrics()
        print("perfect match!!!❤")
        p=False
        break
if p:
    print("better luck next time " \
    " not a perfect match!!!")
input("enter to exit)")
pygame.mixer.music.stop()