import tkinter as tk
import random
from tkinter import ttk

multiple = 0

def center_window(root, width=300, height=300):
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x, y
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set window position
    root.geometry(f"{width}x{height}+{x}+{y}")

def diceButtonPressed(txt: str):
    txt = int(eval(txt))
    print(type(txt), txt)
    return txt

def button(frame: tk, txt: str) -> tk.Button:
    button = tk.Button(frame ,text = txt, height= 1, width= 4,font = ("Segoe Print", 11), command = lambda: calcRoll(diceButtonPressed(txt.replace('d', ''))))
    return button

def calcRoll(dice):
    multiple = int(eval(inputBox.get()))
    roll = 0

    for i in range(1, multiple+1):
                roll += random.randint(1,dice)
    text.config(text = "Roll: " + str(roll))
            


root = tk.Tk()
center_window(root)
root.configure(bg="lightblue")
root.resizable(width = False, height = False)
root.title("Dice Roller")
root.geometry("300x300")



buttonFrame = tk.Frame(root, bg="lightblue")
for i in range(0, 2):   #   make it a 3x3 frame
    buttonFrame.columnconfigure(i, weight=1)
    buttonFrame.rowconfigure(i, weight=1)
buttonFrame.place(x=45, y=75)  #   centered, dont change x bruh


#   my buttons
d4 = button(buttonFrame, "d4")
d4.grid(row = 0, column = 0, padx = 10, pady = 10)   #   buttons must be placed to appear in the frame

d6 = button(buttonFrame, "d6")
d6.grid(row = 0, column = 1, padx = 10, pady = 10)

d8 = button(buttonFrame, "d8")
d8.grid(row = 0, column = 2, padx = 10, pady = 10)

d10 = button(buttonFrame, "d10")
d10.grid(row = 1, column = 0, padx = 10, pady = 10)

d12 = button(buttonFrame, "d12")
d12.grid(row = 1, column = 1, padx = 10, pady = 10)

d20 = button(buttonFrame, "d20")
d20.grid(row = 1, column = 2, padx = 10, pady = 10)

# input

inputBox = tk.Entry(root, font=("Arial", 30), justify="center", validate='key') #   justify makes the typing begin from the middle
inputBox.place(x=50, y =20, height = 50, width= 200,)   #   this seems like a good place for the entry box

# final output
text = tk.Label(root, font=("Segoe Print", 30, "bold"), text="Roll: 567", justify="center", bg="lightblue")
text.place(y = 230, x = 55)

root.mainloop()