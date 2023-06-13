import tkinter as tk
from tkinter import filedialog, Label, messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image
import numpy as np
import tensorflow as tf
from tensorflow import keras

new_model = tf.keras.models.load_model('saved_model/my_model')

batch_size = 32
img_height = 300
img_width = 300
class_names = ['circle', 'love', 'rhombus', 'square', 'star']

root = tk.Tk()
root.title('PROJECT SHAPE RECOGNITION!')
root.geometry("700x650")

filename = "null"
apps = []


def add_App():
    global filename
    global label
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("all files", "*.*"), ("exe", "*.exe")))
    apps.append(filename)
    
    for app in apps:
        label= tk.Label(frame, text=app, bg="white")
        label.pack()

    img = Image.open(filename)
    img = img.resize((300, 250))
    img = ImageTk.PhotoImage(img)

    label.configure(image=img)
    label.image = img
    
    return filename

    


def run_App():
    global filename
    img = keras.preprocessing.image.load_img(
        filename, target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    predictions = new_model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    output = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(
        class_names[np.argmax(score)], 100 * np.max(score))

    labeloutput.configure(text=output)


root.configure(bg="#121212")

canvas = tk.Canvas(root, height=500, width=500, bg="#121212")
canvas.pack()

frame = tk.Frame(root, bg="#2e2e2e")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
labeltitle = Label(frame, text="PROJECT SHAPE DETECTION", font=fontStyle, bg="white")
labeltitle.pack()

line = tk.Frame(frame, height=1, width=550, bg="grey80", relief='groove')
line.pack()


def clearProgram():
    apps.clear()
    labeloutput.configure(text="")
    if label is not None:
        label.configure(image="", text="")
        label.image = None


openFile = tk.Button(frame, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=add_App)
openFile.pack(pady=10)

RunApp = tk.Button(frame, text="Run App", padx=10, pady=5, fg="white", bg="#263D42", command=run_App)
RunApp.pack()

ResetFile = tk.Button(frame, text='Clear All', padx=10, pady=5, fg="white", bg="#263D42", command=clearProgram)
ResetFile.pack(pady=10)

labeloutput = tk.Label(frame, text="", bg="white")
labeloutput.pack()

root.mainloop()




global filename
    global label
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