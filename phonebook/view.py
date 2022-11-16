def showMenu():
    print('\nГлавное меню:\n'
          '1. Открыть файл\n'
          '2. Сохранить файл\n'
          '3. Показать все контакты\n'
          '4. Поиск контакта\n'
          '5. Добавить конаткт\n'
          '6. Изменить контакт\n'
          '7. Удалить контакт\n'
          '0. Выход')


def inputInt(text: str):
      while True:
            try:
                  number = int(input(text))
                  return number
            except:
                  print('Ошибка! Введите целое число!')


def inputStr(text):
      while True:
            try:
                  string = input(text)
                  return string
            except:
                  print('Ошибка! Введите слово!')


def showContacts(phone_book: list, textError: str):
      print()
      if not phone_book == []:
            for index, contact in enumerate(phone_book):
                  print(index, *contact)
      else:
            print(textError)