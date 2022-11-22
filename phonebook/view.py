from gb_groupwork.phonebook.views import *
import os


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

def bamper():
    return print('В разработке...'.upper())


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
