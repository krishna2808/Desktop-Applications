import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import *



root = Tk()
root.title("Music Player")
root.geometry('650x450+150+150')
root.configure(bg = "light blue")
frame = Frame(root,width=600, height=900 ,background='light pink').pack()
label = Label(frame, text='Music player').place(x=300,y= 10)


listOfSong = []
pauseSong = True
index = 0
v = StringVar()
songname = ''
songlabel = Label(frame,textvariable=v, width = 50,bg = "light pink").place(x=140,y=380)

# < -------------------------------function------------------------------->
def select_song(event):
    cs = listbox.curselection()
    global index
    index = cs[0]
    pygame.mixer.music.load(listOfSong[index])
    pygame.mixer.music.play()
    updatelabel()

def next_song():
    global index
    try :
        index += 1
        pygame.mixer.music.load(listOfSong[index])
        pygame.mixer.music.play()
        updatelabel()
    except IndexError as error:
        v.set("")


def previous_song():
    try :
        global index
        index -= 1
        pygame.mixer.music.load(listOfSong[index])
        pygame.mixer.music.play()
        updatelabel()
    except IndexError as error :
          v.set("")

def pause_song():
    global pauseSong
    if pauseSong:
      pygame.mixer.music.pause()
      pauseSong = False

    else:
      pygame.mixer.music.unpause()
      pauseSong = True
    return songname
def updatelabel():
    global index
    global songname
    v.set(listOfSong[index])
    return songname
def directorychooser():
    dir = askdirectory()
    os.chdir(dir)
    for files in os.listdir(dir):
        if files.endswith(".mp3"):
            listOfSong.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listOfSong[0])
# --------------------****************----------------------
directorychooser()
# -------------------------Listbox----------------------------
listbox = Listbox(frame,  width=40, height=20, selectmode=SINGLE)
listOfSong.reverse()
for items in listOfSong:
    listbox.insert(0, items)
listOfSong.reverse()
listbox.bind("<Double-1>",select_song)
listbox.place(x=200,y=30)


# _________________________________________Button____________________________________________________________________

nextbutton = Button(frame, text='Next' ,command =next_song).place(x=340,y=410)
previousbutton = Button(frame, text='Previous', command =previous_song).place(x=230, y=410)
pausebutton = Button(frame, text='pause', command=pause_song).place(x=290, y=410)

root.resizable(False, False)

root.mainloop()
