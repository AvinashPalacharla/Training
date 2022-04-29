import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os


root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')

l=[]
def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )
    l.extend(filenames)



open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)
open_button.pack(expand=True)
root.mainloop()
import copy

f1 = open(r"{}".format(l[0]), "r")
f2 = open(r"{}".format(l[1]), "r")

f= open("new.txt","w")

l=f1.readlines()
s=f2.readlines()
p=[]
q=[]
for i in l:
    c=i.replace("\n","")
    p.append(c)
for j in s:
    d=j.replace("\n","")
    q.append(d)
i=0
for line1 in range(0,len(p)):
    i=i+1
    for line2 in range(0,len(q)):
        if p[line1]!=q[line2] and line1==line2:
            f.write(p[line1])
            f.write(q[line2])


f1.close()
f2.close()
f.close()
os.system(r"C:/Users/avina/OneDrive/Desktop/Training/28_Apr_22/filescom.txt")
