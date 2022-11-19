# ['id', 'first_name', 'last_name', 'patronymic', 'birt#hday', 'phone_person', 'phone_work', 'email', 'group', 'city'])
import os
import csv
from pickupMVC import view


DB_CSV_NAME = 'CSV'
DB_CSV_PATH = '../../pickupMVC/DATA/'
DB_CSV_PATH_FULL = DB_CSV_PATH + DB_CSV_NAME + '.csv'


def getReadyDict(some_header):
    some_data = []
    for i in some_header:
        j = input(f'Введите {i}: ')
        some_data.append(j)
        if len(some_data) == len(some_header): break
    return some_data



def set_CSV_CreateDB():
    header = ['id', 'first_name', 'last_name', 'patronymic', 'phone_person', 'phone_work', 'email', 'group', 'city']
    data = getReadyDict(header)
    with open('CSV.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
        print('Контакт успешно записан!')

if os.path.exists(DB_CSV_PATH_FULL) == True:
    print("Файл CSV БД НАЙДЕН")
else:
    print("Файл БД НЕ НАЙДЕН, БУДЕТ СОЗДАНА БД")
    set_CSV_CreateDB()

def show_CSV_Column():
    with open('CSV.csv') as f:
        reader = csv.DictReader(f)
        print(reader.fieldnames)

def show_CSV_PhoneBook_all():
    with open('CSV.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(" ".join(row))

# def get_CSV_FoundContactBy_Option():
#     field = input(f'Введите параметр поиска контакта: ')
#     result = input(f'Введите {field} контакта: ')
#     with open('CSV.csv') as f:
#         reader = csv.reader(f)
#         for i, item in enumerate(reader):
#
#         if row == None:
#             print(f'Контакт с {field} "{result}" не найден')
#         else:
#             print(f'Найденный контакт:\n {row} ')
def get_CSV_DeleteContactBy_id():
    show_CSV_PhoneBook_all()
    view.inputStr('РЕЖИМ УДАЛЕНИЯ КОНТАКТА')
    field = view.inputStr('Введите ID контакта: ')
    lines = list()
    with open('CSV.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for f in row:
                if f == field:
                    lines.remove(row)
                    print(lines)
                else:
                    print(f'Контакт с ID "{field}" не найден')
                    break
    with open('CSV.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)




# set_CSV_CreateDB()
# show_CSV_Column()
# show_CSV_PhoneBook_all()
# get_CSV_FoundContactBy_Option()
# get_CSV_DeleteContactBy_id()