import os
from gb_groupwork.phonebook import view
from gb_groupwork.phonebook.models import model_CSV


class CLI_PhoneBook_CSV():

    def __init__(self):
        pass

    def menuSelectAction(self):
        print('menuSelectActionCSV')
        view.showInfo('invert', 'Выберите действие в адресной книге:')
        view.showInfo('white', f'1 - Отобразить все данные\n'
                               f'2 - Найти запись в справочнике\n'
                               f'3 - Добавить запись\n'
                               f'4 - экспортировать в ...\n'
                               f'0 - ВЕРНУТЬСЯ НАЗАД\n')
        self.select_action = view.inputInt('Выберите пункт меню: ')
        self.SelectAction()


    def SelectAction(self):
        while True:
            match int(self.select_action):
                case 1:
                    view.showInfo('blue', 'Отобразить все данные')
                    model_CSV.show_CSV_PhoneBook_all()
                    break
                case 2:
                    view.showInfo('blue', 'Найти запись в справочнике')
                    # model_CSV.get_CSV_FoundContactBy_first_name()
                    break
                case 3:
                    view.showInfo('blue', 'Добавить запись')
                    # model_CSV.set_CSV_NewContact()
                    break
                case 4:
                    view.showInfo('blue', 'Экспортировать в ...')
                    # TODO: export menu

                    break
                case 0:
                    view.showInfo('green', 'Возврат в предыдущее меню...')
                    self.menuSelectAction()