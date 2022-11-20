# ['id', 'first_name', 'last_name', 'patronymic', 'birt#hday', 'phone_person', 'phone_work', 'email', 'group', 'city'])
import csv
from gb_groupwork.phonebook import view
from gb_groupwork.phonebook.controller import DB_PATH, DB_CSV_NAME

class CSV_model:
    def __init__(self):
        self.DB_CSV_PATH_FULL = DB_PATH + DB_CSV_NAME + '.csv'


    def getReadyDict(self, some_header):
        some_data = []
        for i in some_header:
            j = input(f'Введите {i}: ')
            some_data.append(j)
            if len(some_data) == len(some_header):
                break
        return some_data


    def set_CSV_CreateDB(self):
        header = ['id', 'first_name', 'last_name', 'patronymic', 'phone_person', 'phone_work', 'email', 'group', 'city']
        data = self.getReadyDict(header)
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

    def show_CSV_Column(self):
        with open(self.DB_CSV_PATH_FULL, 'r', encoding='UTF8') as f:
            reader = csv.DictReader(f)
            print(reader.fieldnames)

    # show_CSV_Column()

    def show_PhoneBook_all(self):
        with open(self.DB_CSV_PATH_FULL, 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(" ".join(row))

    def get_FoundContactBy_Option(self):
        global x
        column = input(f'Введите параметр поиска контакта: ')
        result = input(f'Введите {column} контакта: ')
        with open(self.DB_CSV_PATH_FULL, 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            filtered_rows = []
            for i, j in enumerate(self.show_CSV_Column()):
                if j == column:
                    x = i
            for row in reader:
                if row[int(x)] not in result:
                    print(f'Контакт с {column} "{result}" не найден')
                else:
                    filtered_rows.append(row)
                print(f'Найденный контакт:\n {filtered_rows} ')


    def get_DeleteContactBy_id(self):
        self.show_PhoneBook_all()
        view.inputStr('РЕЖИМ УДАЛЕНИЯ КОНТАКТА')
        field = view.inputStr('Введите ID контакта: ')
        lines = list()
        with open(self.DB_CSV_PATH_FULL, 'r', encoding='UTF8') as readFile:
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
        with open(self.DB_CSV_PATH_FULL, 'r', encoding='UTF8') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
