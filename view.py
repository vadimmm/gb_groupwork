import os
from tkinter import filedialog as fd
from tkinter import *
from tkinter import ttk

selected_path = ''
root = None
frm = None

def beginning():
    global root
    global frm
    root = Tk()
    frm = ttk.Frame(root, padding = 30)
    frm.grid()
    ttk.Label(frm, text = 'Выберите базу данных для загрузки телефонного справочника').grid(column = 0, row = 0)
    ttk.Button(frm, text = 'Ok', command = root.destroy).grid(pady = 5)
    root.mainloop()

def selectFolder():
    global selected_path
    selected_path = fd.askdirectory()

def selectIndividualFile():
    global selected_path
    filetypes = (
        ('CSV', '*.csv'),
        ('sqlite', '*.SQLITE'),
    )
    selected_path = fd.askopenfilename(initialdir='C:/DATA', filetypes=filetypes)

def executeQuery():
    global selected_path
    if os.path.isdir(selected_path):
        print('Выбранная папка:', selected_path)
    elif os.path.isfile(selected_path):
        print('Выбранный файл:', selected_path)
    else:
        print('Файл не выбран')