from tkinter import *
import random 

root = Tk()
root.geometry("400x400")
root.title('Roll Dice')

label = Label(root ,text="" ,font=('Comic Sans MS', 100))

def Roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    val = random.choice(dice)
    label.configure(text=val)
    label.pack()
    
button = Button(root ,text="Roll Dice" ,command=Roll)
button.pack()

root.mainloop()
