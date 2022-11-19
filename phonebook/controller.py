import view
# from models import model_SQL
from models import model_CSV



def start():

    view.beginning()
    view.selectFolder()
    view.selectIndividualFile()
    view.executeQuery()
    view.showMenu()
    CLSmenuWeb()

#
#
#
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
#
def CLSmenuWeb():
    while True:
        choice = view.inputStr('Выберите пункт меню: ')
        match (choice):
            case 1:
                model_CSV.show_CSV_PhoneBook_all()
            case 2:
                model_CSV.get_CSV_FoundContactBy_Option()
            case 3:
                model_CSV.set_CSV_CreateDB()
            case 4:
                model_CSV.get_CSV_DeleteContactBy_id()
            case _:
                return False