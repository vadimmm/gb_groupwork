import os
from gb_groupwork.phonebook import view
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
            view.showInfo('red', f'Вы сделали не допустимый выбор {choice}. Попробуйте снова!')


    def menuSelectAction(self):
        actionMenu = {
            1: 'Отобразить все данные',
            2: 'Найти запись в справочнике',
            3: 'Добавить запись',
            4: 'Экспортировать в ...',
            0: 'ВЕРНУТЬСЯ НАЗАД'
        }
        action = {
            1: self.DB_TYPE.show_PhoneBook_all,
            2: self.DB_TYPE.get_FoundContact,
            3: self.DB_TYPE.set_NewContact,
            4: '# TODO: export menu',
            0: self.menuSelectDbType,
        }
        view.showInfo('invert', '\nВыберите действие в адресной книге:\n\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        run = action.get(choice)
        if run:
            run()
        else:
            view.showInfo('red', f'Вы сделали не допустимый выбор {choice}. Попробуйте снова!')



    def menu_person(self):

        actionMenu = {
            1: 'Изменить поле',
            2: 'Удалить запись',
            0: 'ВЕРНУТЬСЯ НАЗАД'
        }
        action = {
            1: self.DB_TYPE.show_PhoneBook_all,
            2: self.DB_TYPE.get_DeleteContactBy_id,
            0: self.menuSelectDbType,
        }
        view.showInfo('invert', '\nВыберите действие c контактом:\n\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        run = action.get(choice)
        if run:
            run()
        else:
            view.showInfo('red', f'Вы сделали не допустимый выбор {choice}. Попробуйте снова!')

    def menuSelectGroup(self):

        actionMenu = {
            1: 'Семья',
            2: 'Друзья',
            3: 'Работа',
            4: 'Другие',
            0: 'ВЕРНУТЬСЯ НАЗАД',
        }
        action = {
            1: view.bamper,
            2: view.bamper,
            3: view.bamper,
            4: view.bamper,
            0: view.bamper,
        }
        view.showInfo('invert', '\nВыберите группу для контакта:\n\n'.upper())
        self.getPrintDict(actionMenu)
        choice = view.inputInt('Выберите пункт меню: ')
        run = action.get(choice)
        if run:
            run()
        else:
            view.showInfo('red', f'Вы сделали не допустимый выбор {choice}. Попробуйте снова!')

    # def menu_edit_field(self):
    #     view.showinfo('КАКОЕ ПОЛЕ ИЗМЕНИТЬ В КОНТАКТЕ?\n')
    #     view.showinfo(f'Выберите действие:\n'
    #                   f'1 - Имя\n'
    #                   f'2 - Фамилия\n'
    #                   f'3 - Отчество\n'
    #                   f'4 - Дату рождения\n'
    #                   f'5 - Номер мобильного телефона\n'
    #                   f'6 - Номер рабочего телефона\n'
    #                   f'7 - Электронную почту\n'
    #                   f'8 - Группу контакта\n'
    #                   f'9 - Город\n'
    #                   f'0 - ВЕРНУТЬСЯ НАЗАД\n')
    #
    # def menu_edit_group_field(self):
    #     view.showinfo(f'Выберите группу из списка:\n'
    #                   f'1 - Семья\n'
    #                   f'2 - Работа\n'
    #                   f'3 - Друзья\n'
    #                   f'0 - ВЕРНУТЬСЯ НАЗАД\n')
    #
    # def menu_export(self):
    #     view.showinfo(f'Выберите действие:\n'
    #                   f'1 - в SCV\n'
    #                   f'2 - в JSON\n'
    #                   f'3 - в SQLite\n'
    #                   f'0 - ВЕРНУТЬСЯ НАЗАД\n')


# cli = CLI_PhoneBook
# # cli.test()
# cli.menuSelectDbType()
# cli.SelectDbType()
# cli.menuSelectAction