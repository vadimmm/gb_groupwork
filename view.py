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

# def inputInt(text: str):
#     while True:
#         try:
#             number = int(input(text))
#             return number
#         except:
#             print('Ошибка! Введите целое число!')
#
#
# def inputStr(text):
#     while True:
#         try:
#             string = input(text)
#             return string
#         except:
#             print('Ошибка! Введите слово!')
#
# from gb_groupwork.phonebook import views
#
#
# class People:
#
#     def __init__(self, name):
#         self._name = name
#
#     def getName(self):
#         return self._name
#
#
#     def setName(self, name):
#         self._name = name
#
#
#
# class CLI_PhoneBook():
#
#     # __init__():
#         # id = session.query(.store_onoff).filter_by(store_url=app.config['SITE']).first()
#
#         # id = id
#         # first_name
#         # last_name
#         # patronymic
#         # birthday
#         # phone_person
#         # phone_work
#         # email
#         # group
#         # city_id
#
#     # def getUseTypeDB(self):
#     #
#     #     return self.
#
#     def menu_main(self):
#         views.showinfo(f'Выберите действие:\n'
#                       f'1 - Отобразить все данные\n'
#                       f'2 - Найти запись в справочнике\n'
#                       f'3 - Добавить запись\n'
#                       f'4 - экспортировать в ...\n'
#                       f'0 - ВЕРНУТЬСЯ НАЗАД\n')
#
#     def menu_person(self):
#         views.showinfo(f'Выберите действие:\n'
#                       f'1 - Изменить поле:\n'
#                       f'2 - Удалить запись\n'
#                       f'0 - ВЕРНУТЬСЯ НАЗАД\n')
#
#     def menu_edit_field(self):
#         views.showinfo('КАКОЕ ПОЛЕ ИЗМЕНИТЬ В КОНТАКТЕ?\n')
#         views.showinfo(f'Выберите действие:\n'
#                       f'1 - Имя\n'
#                       f'2 - Фамилия\n'
#                       f'3 - Отчество\n'
#                       f'4 - Дату рождения\n'
#                       f'5 - Номер мобильного телефона\n'
#                       f'6 - Номер рабочего телефона\n'
#                       f'7 - Электронную почту\n'
#                       f'8 - Группу контакта\n'
#                       f'9 - Город\n'
#                       f'0 - ВЕРНУТЬСЯ НАЗАД\n')
#
#     def menu_edit_group_field(self):
#         views.showinfo(f'Выберите группу из списка:\n'
#                       f'1 - Семья\n'
#                       f'2 - Работа\n'
#                       f'3 - Друзья\n'
#                       f'0 - ВЕРНУТЬСЯ НАЗАД\n')
#
#     def menu_export(self):
#         # param_dict = [{1: }]
#         views.showinfo(f'Выберите действие:\n'
#                       f'1 - в SCV\n'
#                       f'2 - в JSON\n'
#                       f'3 - в SQLite\n'
#                       f'0 - ВЕРНУТЬСЯ НАЗАД\n')




