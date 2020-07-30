from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap("D:\TSLicon.ico")
root.title("RNG")

img_two = ImageTk.PhotoImage(Image.open("D:\poto22.jpg"))
label_one = Label(root, image=img_two)
label_one.grid(row=0, column=0, columnspan=3)

entry_one = Entry(root, bg="grey", fg="white", width=40, borderwidth=5)
entry_one.insert(0, "Press 'Generate' to generate random number")
entry_one.grid(row=1, column=0, columnspan=3)

def generator():
    global entry_one
    entry_one.delete(0, END)
    number = random.randint(0, 100)
    entry_one.insert(0, number)

button_generator = Button(root, text="Generate", bg="Green", fg="White", padx=20, pady=15, command=generator)
button_generator.grid(row=3, column=1)



root.mainloop()
