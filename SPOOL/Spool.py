import simpleaudio as sa
import os
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tk_font
from PIL import Image, ImageTk

### Global variables ###

# to use this code you must rename this directory to where your SPOOL folder is located, everything else is automatic
spoolLocation = "/home/hiatus/Documents/VisualCode/pythonProjects/SPOOL/"
# you would also have to install tkinter pil simple audio random and os

files = os.listdir(spoolLocation + 'MusicDir/')
sounds = []
songNames = []
MaxS = 0
soundIndex = 0
logo = spoolLocation + "SpLogo.jpg"
ran = False 
pp = False 

### Background/Foreground ###

fg = "white"
bg = "green" 
mainbg = "white"

### Creating sound list ###

for file in files:
    Nfile = spoolLocation + "MusicDir/" + file
    sounds.append(sa.WaveObject.from_wave_file(Nfile))
    MaxS = MaxS + 1 
    Nfile = Nfile.replace(".mp3", "")
    Nfile = Nfile.replace(".wav", "")
    Nfile = Nfile.replace(spoolLocation + "MusicDir/", "")
    songNames.append(Nfile)
    print(Nfile)

print("Song Count:", MaxS)
MaxS = MaxS - 1 

### Tk variables and functions ###

# play a song
play_obj = sounds[soundIndex].play()

def playSong():
    global play_obj
    print("Now playing", songNames[soundIndex])
    play_obj = sounds[soundIndex].play()
    Pl.config(text = "PLAYING " + songNames[soundIndex])
 
# choose a random song
def nextSongRandom():
    global soundIndex
    sa.stop_all()
    soundIndex = random.randrange(0, MaxS)
    playSong()

# plays song to the right
def nextSongRight():
    global soundIndex
    sa.stop_all() 
    soundIndex = soundIndex + 1 
    if soundIndex > MaxS: 
        soundIndex = 0 
    elif soundIndex < 0:
        soundIndex = MaxS     
    playSong()

# plays song to the left
def nextSongLeft():
    global soundIndex
    sa.stop_all() 
    soundIndex = soundIndex - 1 
    if soundIndex > MaxS: 
        soundIndex = 0 
    elif soundIndex < 0:
        soundIndex = MaxS     
    playSong()

# right button
def rightButton(): 
    global ran
    if not ran:
        nextSongRight()
    else:
        nextSongRandom()

# left button
def leftButton(): 
    global ran
    if not ran:
        nextSongLeft()
    else:
        nextSongRandom()

# changes false to true and true to false
def ranChanger():
    global ran
    if ran == False:
        ran = True
    else:
        ran = False
    RandText()

# changes text of random button based on ran variable
def RandText():
    if ran:
        randToggler.config(text = "Random ON")
    else:
        randToggler.config(text = "Random OFF")

# create the window to be used later
window = tk.Tk() 

# some thing to check something else *shrugs*
def ContinuePlay():
    global play_obj
    if play_obj.is_playing() == False and pp == False:
        nextSongRight()
        print("MOVING SONGS TO NEXT SINCE DONE")
    window.after(1000, ContinuePlay)

# Right button
rightB = tk.Button(text = "-->", foreground = fg, background = bg, command = rightButton)
rightB.place(x = 445, y = 170)

# Left button
leftB = tk.Button(text = "<--", foreground = fg, background = bg, command = leftButton)
leftB.place(x = 0, y = 170)

# Pause Play Button
Pl = tk.Button(foreground = fg, background = bg, text = "PAUSED")
def pauseplay():
    global play_obj
    global pp
    global Pl
    print("PRESSED PAUSE/PLAY")
    if pp == True:
        pp = False
        Pl.config(text = "PLAYING " + songNames[soundIndex])
        playSong()
    else:
        pp = True 
        Pl.config(text = "PAUSED "  + songNames[soundIndex])
        sa.stop_all()
Pl.config(command = pauseplay)
Pl.place(x=180, y=170)

# Random Button Toggle
randToggler = tk.Button(text = "Random OFF", foreground = fg, background = bg, command = ranChanger)
randToggler.place(x = 70, y = 170)

### Image Logo Placing ###
image1 = Image.open(logo)
image1 = image1.resize((int(155*1.5), int(50*1.5)), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test, borderwidth=0)

# Position image
label1.place(x=170, y=0)    

### Running the tkinter loop ###
 

window.title("S P O O L")
window.geometry("500x200")
window.configure(bg=mainbg)
window.after(1000, ContinuePlay)
window.mainloop()



