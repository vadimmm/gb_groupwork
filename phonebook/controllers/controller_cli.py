import os
from gb_groupwork.phonebook import view
from gb_groupwork.phonebook.models import model_CSV as CSV
from gb_groupwork.phonebook.models import model_SQL as SQL
# from gb_groupwork.phonebook.controllers import controller_CSV
# from gb_groupwork.phonebook.controllers import controller_SQL

# CSV = controller_CSV.CLI_PhoneBook_CSV()
# SQL = controller_SQL.CLI_PhoneBook_SQL()



class CLI_PhoneBook():
    def __init__(self):
        self.main = 'CLI'
        # self.DB_TYPE == 0

    def test(self):
        view.showInfo('red', 'test')
        view.showInfo('blue', 'test')
        view.showInfo('yellow', 'test')
        view.showInfo('green', 'test')
        view.showInfo('invert', 'test')

    def init(self):
        self.menuSelectDbType()

    def menuSelectDbType(self):
        os.system('cls')
        view.showInfo('invert', f'Выберите базу данных для дальнейшей работы:')
        view.showInfo('white', f'1 - Использовать базу на CSV\n'
                               f'2 - Использовать базу на SQL\n'
                               f'0 - ВЫХОД')
        self.select_db_type = view.inputInt('Выберите пункт меню: ')

        if self.select_db_type == 1:
            self.DB_TYPE = CSV
        elif self.select_db_type == 2:
            self.DB_TYPE = SQL.SQL_model()

        self.SelectDbType()


    def SelectDbType(self):
        while True:
            match int(self.select_db_type):
                case 1:
                    view.showInfo('blue', 'Вы выбрали работу с CSV')
                    self.DB_TYPE.menuSelectAction()
                    break
                case 2:
                    view.showInfo('blue', 'Вы выбрали работу с SQL')
                    self.menuSelectAction()
                    break
                case 0:
                    view.showInfo('green', 'Выход из программы')
                    exit

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
                    self.DB_TYPE.show_PhoneBook_all()
                    break
                case 2:
                    view.showInfo('blue', 'Найти запись в справочнике')
                    self.DB_TYPE.get_FoundContactBy_first_name()
                    break
                case 3:
                    view.showInfo('blue', 'Добавить запись')
                    self.DB_TYPE.set_NewContact()
                    break
                case 4:
                    view.showInfo('blue', 'Экспортировать в ...')
                    # TODO: export menu

                    break
                case 0:
                    view.showInfo('green', 'Возврат в предыдущее меню...')
                    self.menuSelectAction()


    #
    # def menu_person(self):
    #     view.showinfo(f'Выберите действие:\n'
    #                   f'1 - Изменить поле:\n'
    #                   f'2 - Удалить запись\n'
    #                   f'0 - ВЕРНУТЬСЯ НАЗАД\n')
    #
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
    #     # param_dict = [{1: }]
    #     view.showinfo(f'Выберите действие:\n'
    #                   f'1 - в SCV\n'
    #                   f'2 - в JSON\n'
    #                   f'3 - в SQLite\n'
    #                   f'0 - ВЕРНУТЬСЯ НАЗАД\n')


# cli = CLI_PhoneBook
# # cli.test()
# cli.menuSelectDbType()
# cli.SelectDbType()
# cli.menuSelectAction()