# import everything from tkinter module
from tkinter import *
  
# import messagebox from tkinter module
import tkinter.messagebox
  
# create a tkinter root window
root = tkinter.Tk()
  
# root window title and dimension
root.title("When you press a button the message will pop up")
root.geometry('500x300')
  
# Create a messagebox showinfo
  
def playerOne():
    tkinter.messagebox.showinfo("Player 1 Fouls",  "     noice     ")

def playerTwo():
    tkinter.messagebox.showinfo("Player 2 Fouls", "     toight     ")
  
# Create Buttons
button1 = Button(root, text="Fouls", command=playerOne, height=5, width=10)
button2 = Button(root, text = "Fouls", command=playerTwo, height=5, width=10)
  
# Set the position of button of buttons.
button1.pack(side=LEFT)
button2.pack(side=RIGHT)

root.mainloop()