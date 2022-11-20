# ['id', 'first_name', 'last_name', 'patronymic', 'birt#hday', 'phone_person', 'phone_work', 'email', 'group', 'city'])
import os
import csv
from gb_groupwork.phonebook import view


DB_CSV_NAME = 'CSV'
DB_CSV_PATH = '../../gb_groupwork/phonebook/DATA/'
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




# if os.path.exists(DB_CSV_PATH_FULL) == True:
#     print("Файл CSV БД НАЙДЕН")
# else:
#     print("Файл БД НЕ НАЙДЕН, БУДЕТ СОЗДАНА БД")
#     set_CSV_CreateDB()

def show_CSV_Column():
    with open('CSV.csv', encoding='UTF8') as f:
        reader = csv.DictReader(f)
        return reader.fieldnames

def show_CSV_PhoneBook_all():
    with open('CSV.csv', encoding='UTF8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(" ".join(row))

def get_CSV_FoundContactBy_Option():
    global x
    column = input(f'Введите параметр поиска контакта: ')
    result = input(f'Введите {column} контакта: ')
    with open('CSV.csv', encoding='UTF8') as f:
        reader = csv.reader(f)
        filtered_rows = []
        for i, j in enumerate(show_CSV_Column()):
            if j == column:
                x = i
        for row in reader:
            if row[int(x)] not in result:
                print(f'Контакт с {column} "{result}" не найден')
            else:
                filtered_rows.append(row)
            print(f'Найденный контакт:\n {filtered_rows} ')


def get_CSV_DeleteContactBy_id():
    show_CSV_PhoneBook_all()
    view.inputStr('РЕЖИМ УДАЛЕНИЯ КОНТАКТА')
    field = view.inputStr('Введите ID контакта: ')
    lines = list()
    with open('CSV.csv', 'r', encoding='UTF8') as readFile:
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
    exportCSV(lines)

def exportCSV(row):
    with open(DB_CSV_PATH_FULL, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row)




set_CSV_CreateDB()
# show_CSV_Column()
# show_CSV_PhoneBook_all()
# get_CSV_FoundContactBy_Option()
# get_CSV_DeleteContactBy_id()