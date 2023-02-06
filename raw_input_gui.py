import requests
import json
import pandas as pd
from flatten_json import flatten
from tkinter import *

window = Tk()

#Call Submit Function
submit = Button(window,text ='submit',command = submit)
submit.pack(side = BOTTOM)

entry = Entry()
entry.config(font = ('Calibri',20),width = 42)
entry.pack()
window.mainloop()
