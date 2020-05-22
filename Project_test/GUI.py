import tkinter as tk
from tkinter import *
import tkinter.font as font
import tkinter.filedialog as filedialog

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(HomePage)
        self.geometry("1024x768")
        self._frame.pack(fill="both", expand=True)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self.geometry("1024x768")
        self._frame.pack(fill="both", expand=True)


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #tk.Label(self, text="Home page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Start", font=('Helvetica', 25, "bold") , height = 3, width = 15,bg = "gray",fg = 'white' ,command=lambda: master.switch_frame(StartPage)).place(relx=0.5, rely=0.3, anchor=CENTER)
        tk.Button(self, text = 'Rank' , font=('Helvetica', 25, "bold") , height = 3 , width = 15 , bg = 'gray',fg = 'white', command=lambda: master.switch_frame(PageTwo)).place(relx=0.5, rely=0.5, anchor=CENTER)
        tk.Button(self, text = 'Setting' , font=('Helvetica', 25, "bold") , height = 3 , width = 15 , bg = 'gray',fg = 'white', command=lambda: master.switch_frame(PageTwo)).place(relx=0.5, rely=0.7, anchor=CENTER)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", pady=5)
        tk.Button(self, text="Go back to home page",
                  command=lambda: master.switch_frame(HomePage)).pack()


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", pady=5)
        tk.Button(self, text="Go back to home page",
                  command=lambda: master.switch_frame(HomePage)).pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.labelFrame = tk.Label(self, text="Game page", font=('Helvetica', 75, "bold")).place(x = 230 , y = 70)
        tk.Button(self, text="New Game", font=('Helvetica', 25, "bold") , height = 3, width = 15,bg = "gray",fg = 'white' ,command=lambda: master.switch_frame(PageOne)).pack(side = tk.LEFT , padx = 140)
        tk.Button(self, text = 'Browse...' , font=('Helvetica', 25, "bold") , height = 3 , width = 15 , bg = 'gray',fg = 'white', command=self.fileDialog).pack(side = tk.LEFT)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/" , title = "Select A File ..." , filetype = ( ("jpg" , "*.jpg") , ("All Files" , "*.*") ) )
        self.label =  tk.Label(self.labelFrame , text = "",font=('Helvetica', 25))
        self.label.place(x = 190 , y = 210)
        self.label.configure(text = self.filename)
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()