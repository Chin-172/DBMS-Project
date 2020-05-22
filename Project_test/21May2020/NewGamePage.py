import tkinter as tk
from tkinter import *

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.geometry("1024x768")
        self._frame.pack(fill="both", expand=True)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self.geometry("1024x768")
        self._frame.pack(fill="both", expand=True)


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Game page", font=('Helvetica', 75, "bold")).place(x = 230 , y = 70)
        tk.Button(self, text="New Game", font=('Helvetica', 25, "bold") , height = 3, width = 15,bg = "gray",fg = 'white' ,command=lambda: master.switch_frame(PageOne)).pack(side = tk.LEFT , padx = 140)
        tk.Button(self, text = 'Browse...' , font=('Helvetica', 25, "bold") , height = 3 , width = 15 , bg = 'gray',fg = 'white', command=lambda: master.switch_frame(PageTwo)).pack(side = tk.LEFT)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()