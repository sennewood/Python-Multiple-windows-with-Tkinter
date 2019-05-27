# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
# https://pythonprogramming.net/change-show-new-frame-tkinter/?completed=/passing-functions-parameters-tkinter-using-lambda/

import tkinter as tk
from tkinter import ttk

import pageStart as StartPage
import pageOne as PageOne
import pageTwo as PageTwo

LARGE_FONT = ("Verdana", 12)


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "App Title")       

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.von_ueberall_erreichbar = 0
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def getVUE(self):
        return self.von_ueberall_erreichbar

    def raiseVUE(self, targetFrame):
        self.von_ueberall_erreichbar += 1           
        self.frames[targetFrame].label2.config(text=self.getVUE())

    def show_frame(self, targetFrame):
        frame = self.frames[targetFrame]
        self.frames[targetFrame].label2.config(text=self.getVUE())
        frame.tkraise()
