import numpy as np
import sys, os, tensorflow as tf, tkinter as tk, tkinter.font as tkFont
from tkinter import filedialog
from tkinter import *
from tkinter import BOTTOM, TOP, filedialog,Text,Label
from PIL import Image, ImageTk
from tensorflow import keras
from fileinput import filename
from unittest import result
from tkinter.messagebox import showinfo

model = tf.keras.models.load_model('saved_model/my_model')
batch_size = 32
img_height = 300
img_width = 300
class_names = ['circle','love','rhombus','square','star']

root = tk.Tk()
root.title("Shape Recognition")

filename ="null"
apps = []

#function browse button
def browse_button():
    global filename
    global label
    # Prompt the user to select a file
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
                                          filetypes= (("all files","*.*"),("exe","*.exe")))
    apps.append(filename)
    
    
    for app in apps:
        label = tk.Label(frame2,text=app,bg="white" ) 
        label.pack()
        img = Image.open(filename)
        img= img.resize ((200,150))
        img = ImageTk.PhotoImage(img)
        label.configure(image=img)
        label.image = img
    return filename  


#function run app button
def runApp():
    global filename
    img = keras.preprocessing.image.load_img(
        filename, target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    output = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score))

    lblresult.configure(text=output)

#function clear button
def clearProgram():
    apps.clear()
    lblresult.configure(text="")
    if label is not None:
        label.configure(image="")
        label.configure(text="")
        label.image = None
        label.place(relx=0.5, rely=0.3)

#canvas
canvas = tk.Canvas(root, height = 550, width = 6000, bg = "#3264A8")
canvas.pack()

#frame0
frame0 = tk.Frame(root, bg="#3264ad", bd="10")
frame0.place (relwidth=0.85, relheight=0.09, relx=0.5, rely=0.15, anchor='n')

lbltitle = tk.Label(frame0, text="SHAPE RECOGNITION", font=('Eras Bold ITC', 20,'bold') , bg="#3264a0")
lbltitle.pack()

#frame1
frame1 = tk.Frame(root, bg="#3264a6", bd="10")
frame1.place(relwidth=0.85, relheight=0.09, relx=0.5, rely=0.05, anchor='n')

textbox1=tk.Entry(frame1, font=('Courter New', 10))
textbox1.place(relwidth=0.65, relheight=1)

#Frame 2
frame2 = tk.Frame (root, bd=10, bg='#BEBEBE')
frame2.place (relx=0.5, rely=0.30, relheight=0.45, relwidth=0.6, anchor='n')

#myvar=Label(frame2)
#myvar.pack ()

#Frame 3
frame3 = tk.Frame (root, bd=10, bg='#BEBEBE')
frame3.place(relx = 0.5, rely= 0.8, relheight = 0.1, relwidth = 0.6, anchor = 'n')

lblresult = tk.Label (frame3, font=('Courier New', 10, 'bold'), bg='#BEBEBE')
lblresult.pack()

#browse button
browse = tk.Button(frame1, text="BROWSE", bg='#E6E6E6', font=('Courter New', 10, 'bold'), command=browse_button)
browse.place (relx=0.7 , relwidth=0.3, relheight=1)

#run app button
RunApp = tk.Button(root,text="RUN APP",bg='#E6E6E6', font=('Courter New', 14, 'bold'), command=runApp)
RunApp.pack(pady=10, side='bottom')

ResetFile = tk.Button(root, text='Clear All', padx=10, pady=5, fg="white", bg="#263D42", command=clearProgram)
ResetFile.pack(pady=10, side='right')

root.mainloop()