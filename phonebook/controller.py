import os

import view
from gb_groupwork.phonebook.controllers.controller_cli import CLI_PhoneBook


# from models import model_SQL
# from models import model_CSV as model


# def start():
#     view.beginning()
#     # view.selectFolder()
#     view.selectIndividualFile()
#     view.executeQuery()
#     view.showMenu()
#     CLSmenuWeb()


def init():
    cli = CLI_PhoneBook()
    # cli.test()
    cli.menuSelectDbType()
    cli.SelectDbType()
    cli.menuSelectAction()

# def SQLmenuWeb():
#     while True:
#         choice = view.inputStr('Выберите пункт меню: ')
#         match (choice):
#             case 1:
#                 model_SQL.show_SQL_PhoneBook_all()
#             case 2:
#                 model_SQL.showSubMenuSQL()
#                 while True:
#                     value = view.inputInt('Выберите способ поиска: ')
#                     match (value):
#                         case 11:
#                             model_SQL.get_SQL_FoundContactBy_id()
#                         case 12:
#                             model_SQL.get_SQL_FoundContactBy_first_name()
#                         case 13:
#                             model_SQL.get_SQL_FoundContactBy_last_name()
#                         case 14:
#                             model_SQL.get_SQL_FoundContactBy_phone_person()
#             case 3:
#                 model_SQL.set_SQL_NewContact()
#             case 4:
#                 model_SQL.get_SQL_DeleteContactBy_id()
#             case _:
#                 return False

# def CLSmenuWeb():
#     while True:
#         choice = view.inputStr('Выберите пункт меню: ')
#         match int(choice):
#             case 1:
#                 print('Показываю все контакты')
#                 model.show_CSV_PhoneBook_all()
#             case 2:
#                 model.get_CSV_FoundContactBy_Option()
#             case 3:
#                 model.set_CSV_CreateDB()
#             case 4:
#                 model.get_CSV_DeleteContactBy_id()
#             case _:
#                 print("Выход из приложения")
#                 return False
