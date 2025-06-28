import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title('Text to Speech')
root.geometry('900x450+200+200')
root.resizable(FALSE, FALSE)
root.configure(bg='navyblue')

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    if text.strip(): 
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        
        path = filedialog.askdirectory(title="Select directory to save file")
        if path:  
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if text.strip():
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

img_icon = PhotoImage(file='D:/python files2/python files/speak_1393778.png')
root.iconphoto(False, img_icon)

top_frame = Frame(root, bg='white', width=900, height=100)
top_frame.place(x=0, y=0)

logo = PhotoImage(file="D:/python files2/python files/microphone_7402379.png")
logo_small = logo.subsample(7, 7)  
Label(top_frame, image=logo_small, bg='white').place(x=25, y=6)

Label(top_frame, text='TEXT TO SPEECH', font=('arial', 20, 'bold'), bg='white', fg='black').place(x=100, y=30)

text_area = Text(root, font=('Robote', 20), bg='white', relief=GROOVE, wrap=WORD) 
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text='Voice', font=('arial', 15, 'bold'), bg='navyblue', fg='white').place(x=580, y=160)
Label(root, text='Speed', font=('arial', 15, 'bold'), bg='navyblue', fg='white').place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font=('arial', 14), state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')
 
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font=('arial', 14), state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

imgicon1 = PhotoImage(file='D:/python files2/python files/speak_1393778.png')
imgicon1_small = imgicon1.subsample(20, 20)  
btn1 = Button(root, text='Speak', compound=LEFT, image=imgicon1_small, width=130, font=('arial', 14, 'bold'), command=speaknow)
btn1.place(x=550, y=280)

imgicon2 = PhotoImage(file='D:/python files2/python files/download_11932822.png')
imgicon2_small = imgicon2.subsample(20, 20)
save = Button(root, text='Save', compound=LEFT, image=imgicon2_small, width=130, bg='white', font=('arial', 14, 'bold'), command=download)
save.place(x=730, y=280)

root.mainloop()
