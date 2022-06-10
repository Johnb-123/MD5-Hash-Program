# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:48:45 2022

Basic Tkinter Interface
"""


from tkinter import *
import hashlib

#encoding text with md5 hash
def myHash(text):
    secure = text.encode('utf-8')
    h = hashlib.md5()
    h.update(secure)
    return h.hexdigest()

#getting our hash
def getHash(event):
    res.configure(text = "MD5 encoded String: " + str(myHash(entry.get())))


#Creating a window in tkinter
window = Tk()
window.title('Is this secure?')
window.geometry("350x300")
window.resizable(False, False)

#Including icon
window.iconbitmap('image.ico')

#Main label
greeting = Label(window, text = "Input Text").pack()

#Creating Hash
message = Label(window, text = "Message: " )
entry = Entry(window, width=50)
entry.bind("<Return>", getHash)
entry.pack()

#calling hash
res = Label(window)
res.pack()



window.mainloop()



