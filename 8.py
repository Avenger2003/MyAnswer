import customtkinter as ct
from tkinter import *
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
function_map = {}

def speak_now():
    engine.say(textv.get())
    engine.runAndWait()

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text_ing = r.recognize_google(audio)
            if text_ing in function_map:
                function = function_map[text_ing]
                function()
                check_box.deselect()
            else:
                text1.insert(ct.END, text_ing + "\n")
                global spoken_text
                spoken_text += "\n"+text_ing
        except sr.UnknownValueError:
            text1.insert(ct.END, "Could not understand audio\n")
        except sr.RequestError as e:
            text1.insert(ct.END, "Error: {0}\n".format(e))

def speak_text():
    engine.say(spoken_text)
    engine.runAndWait()

def opening():
    frame1.pack_forget()
    obj.pack(fill="both", expand="yes", padx=10, pady=10)

def closing():
    obj.pack_forget()
    frame1.pack(fill="both", expand="yes", padx=10, pady=10)

def clear_textboxes():
    text.delete(0, END)
    text1.delete(1.0, END)
    
function_map = {"please go back": closing, "come back":closing,"back": closing, "go back": closing,"go to page":opening}

root = ct.CTk()
textv = StringVar()
spoken_text = ""

obj = ct.CTkFrame(root, width=350, height=350)

frame1 = ct.CTkFrame(root, width=350, height=350)
frame1.pack(fill="both", expand="yes", padx=10, pady=10)

go_button = ct.CTkButton(frame1, text="Go", command=opening)
go_button.grid(row=0, column=0)

check_box=ct.CTkCheckBox(frame1,text="Speak into the program",command=speech_to_text)
check_box.grid(rows=10,column=0)

back_button = ct.CTkButton(obj, text="Back", command=closing)
back_button.grid(row=0, column=0)

lbl = ct.CTkLabel(obj, text="Text")
lbl.grid(row=1, columnspan=2)

text = ct.CTkEntry(obj, textvariable=textv)
text.grid(row=2, column=0, columnspan=3)

btn = ct.CTkButton(obj, text="Speak", command=speak_now)
btn.grid(row=3, column=0)

lbl1 = ct.CTkLabel(obj, text="Speech")
lbl1.grid(row=4, columnspan=2)

text1 = ct.CTkTextbox(obj)
text1.grid(row=5, column=0, columnspan=3, rowspan=5)

convert_btn = ct.CTkButton(obj, text="Convert", command=speech_to_text)
convert_btn.grid(row=11, column=0)

speak_btn = ct.CTkButton(obj, text="Speak It", command=speak_text)
speak_btn.grid(row=11, column=1)

obj.pack_propagate(False)
frame1.pack_propagate(False)

root.title("Welcome")
root.geometry("400x400")
root.resizable(False, False)
root.mainloop()

