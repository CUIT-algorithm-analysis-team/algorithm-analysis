from tkinter.messagebox import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from PIL import Image

from PIL import ImageTk
from tkinter import *

root = Tk()

textLabel = tk.Label(root,text='请重试！\n您的操作不被允许！',justify=LEFT,padx=10,pady=10)#右边距10px

textLabel.pack(side=LEFT)

photo = PhotoImage(file="plottext.png")

imageLabel = Label(root, image=photo)

imageLabel.pack(side=RIGHT)

mainloop()
