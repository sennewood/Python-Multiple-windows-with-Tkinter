# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
# https://pythonprogramming.net/change-show-new-frame-tkinter/?completed=/passing-functions-parameters-tkinter-using-lambda/

import tkinter as tk
from tkinter import ttk

import pageApplication as App
import pageStart as StartPage
import pageTwo as PageTwo

LARGE_FONT = ("Verdana", 12)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        self.label2.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="+1",
                            command=lambda: controller.raiseVUE(PageOne))
        button3.pack()
