from gb_groupwork.phonebook.views import *
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
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Label(frm, text='Выберите базу данных для загрузки телефонного справочника').grid(column=0, row=0)
    ttk.Button(frm, text='Ok', command=root.destroy).grid(pady=5)
    root.mainloop()


def selectFolder():
    global selected_path
    selected_path = fd.askdirectory()


def selectIndividualFile():
    global selected_path
    filetypes = (
        ('CSV', '*.csv'),
        ('sqlite', '*.sqlite'),
    )
    selected_path = fd.askopenfilename(initialdir='../../gb_groupwork/phonebook/DATA/', filetypes=filetypes)


def executeQuery():
    global selected_path
    if os.path.isdir(selected_path):
        print('Выбранная папка:', selected_path)
    elif os.path.isfile(selected_path):
        print('Выбранный файл:', selected_path)
    else:
        print('Файл не выбран')


def showMenu():
    print('\nГлавное меню:\n'
          '1. Показать все контакты\n'
          '2. Поиск контакта\n'
          '3. Добавить контакт\n'
          '4. Удалить контакт\n'
          '0. Выход')


def showSubMenuSQL():
    print('\nВыберите способ поиска:\n'
          'A. по ID\n'
          'B. по Имени\n'
          'C. по Фамилии\n'
          'D. по Номеру телефона\n'
          'O. Выход')


def inputInt(text: int):
    while True:
        try:
            number = int(input(text))
            return number
        except:
            showInfo('red', 'Ошибка! Введите целое число!')


def inputStr(text):
    while True:
        try:
            string = input(text)
            return string
        except:
            showInfo('red', 'Ошибка! Введите слово!')


def showInfo(color=None, text=None):
    if color == 'white':
        return print('\33[1m' + text + '\033[0m')
    elif color == 'red':
        return print('\33[31m' + text + '\033[0m')
    elif color == 'blue':
        return print('\33[34m' + text + '\033[0m')
    elif color == 'yellow':
        return print('\33[93m' + text + '\033[0m')
    elif color == 'green':
        return print('\33[92m' + text + '\033[0m')
    elif color == 'invert':
        return print('\33[7m' + text + '\033[0m')
