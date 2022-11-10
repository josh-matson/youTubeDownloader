from tkinter import *
import tkinter
from tkinter.filedialog import askdirectory
from pytube import YouTube

root = Tk()
root.geometry('500x200')

l1 = Label(text="Choose a download destination:")
l1.grid(row=0,column=0,sticky=E)

browseText = tkinter.StringVar()
browseBtn = tkinter.Button(root, textvariable=browseText, command=lambda:open_file())
browseText.set("Browse")
browseBtn.grid(row=0, column=1, pady=20, padx=(20,20),sticky=W)

l2 = Label(text="Paste the youtube link here:")
l2.grid(row=1,column=0,sticky=E)

entry1 = Entry(root, width = 28)
entry1.grid(row=1,column=1,padx=(20,0))

#Button(root, text="Download the video...", command=button_command).grid(row=2,column=1,pady=(30,10), padx=20)

l3 = Label(text="Click 'GO!' to begin the download:")
l3.grid(row=2,column=0,padx=(20,0))

downloadText = tkinter.StringVar()
downloadBtn = tkinter.Button(root, textvariable=downloadText, command=lambda:button_command())
downloadText.set("GO!")
downloadBtn.grid(row=2, column=1, pady=20, padx=(20,20),sticky=W)

l4 = Label(text="")
l4.grid(row=3,column=0)

def open_file():
    #browseText.set("loading . . .")
    global folder 
    folder = askdirectory(parent=root, title="Choose a destination")
    #print(folder)

def button_command():
    
    global myURL 
    myURL = entry1.get()
    #print(myURL)
    yt = YouTube(myURL)
    yd = yt.streams.get_highest_resolution()
    yd.download(folder)
    l4.config(text="The download is complete")
    return None

root.mainloop()