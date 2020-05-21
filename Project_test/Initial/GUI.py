import tkinter as tk
from tkinter import *
import tkinter.font as font

window = tk.Tk()
window.title("賴韜允")
window.geometry("1024x768")
myFont = font.Font(size=25 , weight = 'bold')
window.resizable(0,0)
# window.maxsize(1050,2000)


startbtn = Button(window,text = 'Start' ,height = 3, width = 15,bg = "gray",fg = 'white')
startbtn['font'] = myFont
startbtn.place(relx = 0.35 , rely = 0.17)

rankbtn = Button(window,text = 'Rank' , height = 3 , width = 15 , bg = 'gray',fg =  'white')
rankbtn['font'] = myFont
rankbtn.place(relx = 0.35 , rely = 0.47)

setbtn = Button(window,text = 'Setting', height = 3 , width = 15 , bg = 'gray',fg = 'white')
setbtn['font'] = myFont
setbtn.place(relx = 0.35 , rely = 0.77)

window.mainloop()