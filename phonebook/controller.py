import os

import view
from gb_groupwork.phonebook.controllers import controller_cli


# from models import model_SQL
# from models import model_CSV as model

DB_PATH = '../../gb_groupwork/phonebook/DATA/'
DB_SQL_NAME = 'sqlite'
DB_CSV_NAME = 'CSV'

ExpoptDB_CSV_NAME = 'CSVto'
ExpoptDB_CSVtoSqlite_NAME = 'CSVtoSqlite'

ExpoptDB_SqlitetoTxt_NAME = 'SqlitetoTxt'
ExpoptDB_SqlitetoCSV_NAME = 'SqlitetoCSV'

DB_CSV_PATH_FULL = DB_PATH + DB_CSV_NAME + '.csv'
DB_SQL_PATH_FULL = DB_PATH + DB_SQL_NAME + '.sqlite'

ExportDB_CSV_PATH_FULL = DB_PATH + ExpoptDB_CSV_NAME + '.txt'
ExpoptDB_CSVtoSqlite_PATH_FULL = DB_PATH + ExpoptDB_CSVtoSqlite_NAME + '.sqlite'

ExportDB_SqlitetoTxt_PATH_FULL = DB_PATH + ExpoptDB_SqlitetoTxt_NAME + '.txt'
ExpoptDB_SqlitetoCSV_PATH_FULL = DB_PATH + ExpoptDB_SqlitetoCSV_NAME + '.csv'


# def start():
#     view.beginning()
#     # view.selectFolder()
#     view.selectIndividualFile()
#     view.executeQuery()
#     view.showMenu()
#     CLSmenuWeb()


def init():
    cli = controller_cli.CLI_PhoneBook()
    # cli.test()
    # cli.menuSelectDbType()
    cli.init()
    # cli.menuSelectDbType()
    # cli.menuSelectAction()

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
