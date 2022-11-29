import os
from gb_groupwork.phonebook import view
from gb_groupwork.phonebook import controller
from gb_groupwork.phonebook.models import model_CSV as CSV
from gb_groupwork.phonebook.models import model_SQL as SQL


class CLI_PhoneBook:
    def __init__(self):
        self.main = 'CLI'

    def init(self):
        self.menuSelectDbType()

    def getPrintDict(self, dictName):
        menu = ''.join(f'{key} - {value}\n' for key, value in dictName.items())
        view.showInfo('white', f'{menu}')

    def getObj(self, mydict, key):
        return mydict[key]

    def menuSelectDbType(self):
        actionMenu = {
            1: 'Использовать базу на CSV',
            2: 'Использовать базу на SQL',
            0: 'ВЫХОД'
        }
        action = {
            1: self.menuSelectAction,
            2: self.menuSelectAction,
            0: exit,
        }
        os.system('cls')
        view.showInfo('invert', f'\nВыберите базу данных для дальнейшей работы:\n\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        if choice == 1:
            self.DB_TYPE = CSV.CSV_model()
        elif choice == 2:
            self.DB_TYPE = SQL.SQL_model()
        run = action.get(choice)
        if run:
            run()
        else:
            view.showInfo('red', f'Вы сделали недопустимый выбор {choice}. Попробуйте снова!')
            self.menuSelectDbType()

    def menuSelectAction(self):
        actionMenu = {
            1: 'Отобразить все данные',
            2: 'Найти запись в справочнике',
            3: 'Добавить запись',
            4: 'Удалить запись',
            5: 'Экспортировать в ...',
            0: 'ВЕРНУТЬСЯ НАЗАД'
        }
        action = {
            1: self.DB_TYPE.show_PhoneBook_all,
            2: self.DB_TYPE.get_FoundContact,
            3: self.DB_TYPE.set_NewContact,
            4: self.DB_TYPE.get_DeleteContact,
            5: self.menuSelectExportDbType,
            0: self.menuSelectDbType,
        }
        os.system('cls')
        view.showInfo('invert', '\nВыберите действие в адресной книге:\n\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        run = action.get(choice)
        if run:
            run()
        else:
            view.showInfo('red', f'Недопустимый выбор {choice}! Попробуйте снова!')
            self.menuSelectAction()

    def menuEditContact(self):
        actionMenu = {
            1: 'Добавить запись',
            2: 'Удалить запись',
            0: 'ВЕРНУТЬСЯ НАЗАД'
        }
        action = {
            1: self.DB_TYPE.set_NewContact,
            2: self.DB_TYPE.get_DeleteContact,
            0: self.menuSelectAction,
        }
        os.system('cls')
        view.showInfo('invert', '\nДействие c контактом:\n\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        run = action.get(choice)
        if run:
            run()
        else:
            view.showInfo(f'Недопустимый выбор {choice}. Попробуйте снова!')
            self.menuEditContact()

    def menuEditGroupField(self):
        actionMenu = {
            1: 'Семья',
            2: 'Друзья',
            3: 'Работа',
            4: 'Другие'
        }
        action = {
            1: self.getObj(actionMenu, 1),
            2: self.getObj(actionMenu, 2),
            3: self.getObj(actionMenu, 3),
            4: self.getObj(actionMenu, 4),
        }
        view.showInfo('blue', 'Выберите группу для контакта:\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        value_selected = action.get(choice)
        if value_selected:
            view.showInfo('white', f'Выбрана группа "{value_selected}"')
            #     time.sleep(3)
            return value_selected
        else:
            view.showInfo('red', f'Вы сделали не допустимый выбор "{choice}". Попробуйте снова!')
            self.menuEditGroupField()

    def menuSelectExportDbType(self):
        actionMenu = {
            1: 'Экспорт в .txt (только для CSV)',
            2: 'Экспорт в .sqlite (только для CSV)',
            3: 'Экспорт в .csv (только для SQL)',
            0: 'ВЕРНУТЬСЯ НАЗАД',
        }
        action = {
            1: self.DB_TYPE.Export_toTxt,
            2: self.DB_TYPE.Export_CSVtoSQL,
            3: self.DB_TYPE.Export_SQLtoCSV,
            0: self.menuSelectAction,
        }
        os.system('cls')
        view.showInfo('invert', '\nВыберите базу данных для экспорта:\n\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        run = action.get(choice)
        if run:
            run()
        else:
            view.showInfo('red', f'Вы сделали недопустимый выбор {choice}. Попробуйте снова!')
            self.menuSelectExportDbType()

    def menuEditJobTitleField(self):
        actionMenu = {
            1: 'Преподаватель',
            2: 'Студент',
            3: 'Оставить пустым',
        }
        action = {
            1: self.getObj(actionMenu, 1),
            2: self.getObj(actionMenu, 2),
            3: self.getObj(actionMenu, 3),
        }
        os.system('cls')
        view.showInfo('blue', 'Выберите группу для контакта:\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        value_selected = action.get(choice)
        if value_selected:
            return value_selected
        else:
            view.showInfo('red', f'Вы сделали не допустимый выбор {choice}. Попробуйте снова!')
            self.menuEditGroupField()
