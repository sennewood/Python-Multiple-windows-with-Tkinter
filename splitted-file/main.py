# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
# https://pythonprogramming.net/change-show-new-frame-tkinter/?completed=/passing-functions-parameters-tkinter-using-lambda/

import tkinter as tk
from tkinter import ttk

import pageApplication as App
import pageStart as StartPage
import pageOne as PageOne
import pageTwo as PageTwo

LARGE_FONT = ("Verdana", 12)


app = App.Application()

# set window size
app.geometry("210x180+30+30")

# init menubar
menubar = tk.Menu(app)

# creating the menus
menuManage = tk.Menu(menubar, tearoff=0)

# list of menubar elements
menubar.add_cascade(menu=menuManage, label="Frame")

# menu: manage
menuManage.add_command(label="P1", command=lambda: app.show_frame(PageOne))
menuManage.add_command(label="P2", command=lambda: app.show_frame(PageTwo))
menuManage.add_command(label="Start", command=lambda: app.show_frame(StartPage))

# attach menubar
app.config(menu=menubar) 


app.mainloop()
