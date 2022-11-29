import json

from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import Column, Integer, String, Date, Table, select
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3
import csv
import os
from gb_groupwork.phonebook import views
from gb_groupwork.phonebook import view
from gb_groupwork.phonebook.controller import DB_PATH, DB_SQL_NAME, DB_SQL_PATH_FULL, ExportDB_SqlitetoTxt_PATH_FULL, ExpoptDB_SqlitetoCSV_PATH_FULL
from gb_groupwork.phonebook.controllers import controller_cli


class SQL_model:
    def __init__(self):
        self.DB_SQL_PATH_FULL = DB_SQL_PATH_FULL
        self.ExportDB_SqlitetoTxt_PATH_FULL = ExportDB_SqlitetoTxt_PATH_FULL
        self.ExpoptDB_SqlitetoCSV_PATH_FULL = ExpoptDB_SqlitetoCSV_PATH_FULL
        self.engine = db.create_engine('sqlite:///' + self.DB_SQL_PATH_FULL, echo=False)

        self.connection = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.metadata = db.MetaData()
    def set_SQL_CreateDB(self):

        self.table_phonebook = Table(
            'PhoneBook', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('first_name', String(50), nullable=False),
            Column('last_name', String(50), nullable=False),
            Column('patronymic', String(50), nullable=True),
            Column('birthday', Date, nullable=True),
            Column('phone_person', String(12), nullable=False),
            Column('phone_work', String(12), nullable=True),
            Column('email', String, nullable=True),
            Column('jobTitle', String, nullable=True),
            Column('group', String, nullable=True),
            Column('city', String, nullable=True),
        )

        self.metadata.create_all(self.engine)

    def checkDB(self):
        if os.path.exists(self.DB_SQL_PATH_FULL) == True:
            view.showInfo('blue', 'Файл БД НАЙДЕН')
        else:
            view.showInfo('blue', 'Файл БД НЕ НАЙДЕН, БУДЕТ СОЗДАНА БД')
            self.set_SQL_CreateDB()


    Base = declarative_base()

    class PhoneBook(Base):
        __tablename__ = 'PhoneBook'
        id = Column(Integer, primary_key=True, autoincrement=True)
        first_name = Column(String(50), nullable=False)
        last_name = Column(String(50), nullable=False)
        patronymic = Column(String(50), nullable=True)
        birthday = Column(Date, nullable=True)
        phone_person = Column(String(12), nullable=False)
        phone_work = Column(String(12), nullable=True)
        email = Column(String, nullable=True)
        jobTitle = Column(String, nullable=True)
        group = Column(String, nullable=True)
        city = Column(String, nullable=True)

        def __repr__(self):
            return f'{self.id} ' \
                   f'{self.last_name.upper()} ' \
                   f'{self.first_name.title()} ' \
                   f'{self.patronymic} ' \
                   f'{self.birthday} ' \
                   f'{self.phone_person} ' \
                   f'{self.phone_work} ' \
                   f'{self.email} ' \
                   f'{self.jobTitle} ' \
                   f'{self.group} ' \
                   f'{self.city} '


    def show_SQL_Column(self):
        with self.connection as conn:
            result = conn.execute(select(
                [
                    self.PhoneBook.id,
                    self.PhoneBook.first_name,
                    self.PhoneBook.last_name,
                    self.PhoneBook.patronymic,
                    self.PhoneBook.birthday,
                    self.PhoneBook.phone_person,
                    self.PhoneBook.phone_work,
                    self.PhoneBook.email,
                    self.PhoneBook.jobTitle,
                    self.PhoneBook.group,
                    self.PhoneBook.city
                ]
            )
            )
        view.showInfo('white', f'{result._metadata.keys}')


    def show_PhoneBook_all(self):
        view.showInfo('white', 'СПИСОК КОНТАКТОВ: ')
        self.show_SQL_Column()
        responses = self.session.query(self.PhoneBook).all()
        for result in responses:
            view.showInfo('white', f'{result}')

    def get_FoundContact(self):
        field = view.inputStr('Введите ключевое слово для поиска контакта: ')
        id = self.session.query(self.PhoneBook).filter(self.PhoneBook.id == field).all()
        first_name = self.session.query(self.PhoneBook).filter(self.PhoneBook.first_name == field).all()
        last_name = self.session.query(self.PhoneBook).filter(self.PhoneBook.last_name == field).all()
        patronymic = self.session.query(self.PhoneBook).filter(self.PhoneBook.patronymic == field).all()
        phone_person = self.session.query(self.PhoneBook).filter(self.PhoneBook.phone_person == field).all()
        phone_work = self.session.query(self.PhoneBook).filter(self.PhoneBook.phone_work == field).all()
        email = self.session.query(self.PhoneBook).filter(self.PhoneBook.email == field).all()
        responses = (id or first_name or last_name or phone_person or patronymic or phone_work or email)
        if responses == []:
            view.inputStr(f'Контакт с параметрами "{field}" не найден')
            self.connection.close()
            self.get_FoundContact()
        else:
            view.showInfo('white', 'НАЙДЕНЫ КОНТАКТЫ: ')
            for result in responses:
                view.showInfo('white', f'{result}')

    def set_NewContact(self):
        view.showInfo('invert', '\nрежим добавления нового контакта\n\n'.upper())
        get_first_name = view.inputStr('Введите имя контакта: ')
        get_last_name = view.inputStr('Введите фамилию контакта: ')
        get_patronymic = view.inputStr('Введите отчество контакта: ')
        # get_birthday = view.inputStr('Введите дату ДР контакта: ')
        get_phone_person = view.inputStr('Введите мобильный телефон контакта: ')
        get_phone_work = view.inputStr('Введите рабочий телефон контакта: ')
        get_email = view.inputStr('Введите email контакта: ')
        get_jobTitle = controller_cli.CLI_PhoneBook().menuEditJobTitleField()
        # get_group = view.inputStr('Введите группу контакта: ')
        get_group = controller_cli.CLI_PhoneBook().menuEditGroupField()
        get_city = view.inputStr('Введите город контакта: ')

        with self.engine.connect() as conn:
            result = conn.execute(
                insert(self.PhoneBook),
                [
                    {
                        'first_name': get_first_name,
                        'last_name': get_last_name,
                        'patronymic': get_patronymic,
                        # 'birthday': get_birthday,
                        'phone_person': get_phone_person,
                        'phone_work': get_phone_work,
                        'email': get_email,
                        'jobTitle': get_jobTitle,
                        'group': get_group,
                        'city': get_city,
                     },
                ],
            )

    def get_ShowContactBy_id(self):
        field = view.inputStr('Введите ID контакта: ')
        responses = self.session.query(self.PhoneBook).filter(self.PhoneBook.id == field).all()
        if responses == []:
            view.showInfo('red', f'Контакт с ID "{field}" не найден')
        else:
            for result in responses:
                view.showInfo('white', f'{result.first_name}')


    def get_DeleteContact(self):
        # self.show_PhoneBook_all()
        view.showInfo('РЕЖИМ УДАЛЕНИЯ КОНТАКТА')
        field = view.inputStr('Введите ID контакта для удаления: ')
        responses = self.session.query(self.PhoneBook).filter(self.PhoneBook.id == field).all()
        print(f'>>>>{responses[0]}<<<<')
        if responses == []:
            view.showInfo(f'Контакт с ID "{field}" не найден')
            # self.connection.close()
            # self.get_DeleteContact()
        elif responses != []:
            for result in responses:
                view.showInfo('white', f'{result.first_name}')
                view.showInfo('yellow', 'ВЫ ТОЧНО ХОТИТЕ УДАЛИТЬ ВЫБРАННЫЙ КОНТАКТ БЕЗ ВОЗМОЖНОСТИ ВОССТАНОВЛЕНИЯ?')
                delChoice = view.inputStr('Нажмите "1" для удаления или "0" для отмены:\n')
                if delChoice == '1':
                    self.session.query(self.PhoneBook).filter(self.PhoneBook.id == field).delete()
                    self.session.commit()
                    view.showInfo('green', f'Выбранный контакт с ID "{field}" удалён!')
                else:
                    view.showInfo('blue', f'Вы отменили удаление контакта с ID "{field}"')

                # self.connection.close()
    def Export_SQLtoCSV(self):
        conn = sqlite3.connect(self.DB_SQL_PATH_FULL)
        cursor = conn.cursor()
        cursor.execute('select * from PhoneBook')
        with open(self.DB_SQL_PATH_FULL+'test', 'w', newline='', encoding='UTF-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)
        conn.close()
        view.showInfo('green', f'Экспорт в {ExpoptDB_SqlitetoCSV_PATH_FULL} успешно завершен!')

    def Export_toTxt(self):
        view.showInfo('red', 'Недоступно для SQL. Выберите другую базу для экспорта!')
        pass

    def Export_CSVtoSQL(self):
        view.showInfo('red', 'Недоступно для SQL. Выберите другую базу для экспорта!')
        pass

    def setExport_SQL_to_CSV(self):
        pass

    def setImport_CSV_toSQL(self):
        pass