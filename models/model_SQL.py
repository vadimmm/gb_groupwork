from sqlalchemy import Column, Integer, String, Date, Table, select
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from gb_groupwork.phonebook import view
import os
from gb_groupwork.phonebook import views
from pickupMVC import view


DB_SQL_NAME = 'sqlite'
DB_SQL_PATH = '../../gb_groupwork/phonebook/DATA/'
DB_SQL_PATH_FULL = DB_SQL_PATH + DB_SQL_NAME + '.sqlite'

engine = db.create_engine('sqlite:///' + DB_SQL_PATH_FULL, echo=False)

connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()
def set_SQL_CreateDB():

    # GROUP_CHOICES = (
    #         ('БЕЗ ГРУППЫ', 'БЕЗ ГРУППЫ'),
    #         ('Семья', 'Семья'),
    #         ('Работа', 'Работа'),
    #         ('Друзья', 'Друзья'),
    #     ),

    table_phonebook = Table(
        'PhoneBook', metadata,
        Column('id', Integer, primary_key=True),
        Column('first_name', String(50), nullable=False),
        Column('last_name', String(50), nullable=False),
        Column('patronymic', String(50), nullable=True),
        Column('birthday', Date, nullable=True),
        Column('phone_person', String(12), nullable=False),
        Column('phone_work', String(12), nullable=True),
        Column('email', String, nullable=True),
        # Column('group', choices=GROUP_CHOICES, default='БЕЗ ГРУППЫ'),
        Column('group', String, nullable=True),
        Column('city', String, nullable=True),
    )

    metadata.create_all(engine)


if os.path.exists(DB_SQL_PATH_FULL) == True:
    print("Файл БД НАЙДЕН")
else:
    print("Файл БД НЕ НАЙДЕН, БУДЕТ СОЗДАНА БД")
    set_SQL_CreateDB()


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
    # group = Column(String, choise=GROUP_CHOICES, default='БЕЗ ГРУППЫ', nullable=True)
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
               f'{self.group} ' \
               f'{self.city} '


def set_SQL_NewContact():
    views.ShowInfo('Введите имя контакта: ')
    get_first_name = views.getString()
    views.ShowInfo('Введите фамилию контакта: ')
    get_last_name = views.getString()
    views.ShowInfo('Введите отчество контакта: ')
    get_patronymic = views.getString()
    views.ShowInfo('Введите дату ДР контакта: ')
    get_birthday = views.getString()
    views.ShowInfo('Введите мобильный телефон контакта: ')
    get_phone_person = views.getString()
    views.ShowInfo('Введите рабочий телефон контакта: ')
    get_phone_work = views.getString()
    views.ShowInfo('Введите email контакта: ')
    get_email = views.getString()
    views.ShowInfo('Введите группу контакта: ')
    get_group = views.getString()
    views.ShowInfo('Введите город контакта: ')
    get_city = views.getString()

    with sql.engine.connect() as conn:
        result = conn.execute(
            sql.insert(sql.table_phonebook),
            [
                {'first_name': get_first_name,
                 'last_name': get_last_name,
                 'patronymic': get_patronymic,
                 # 'birthday': get_birthday,
                 'phone_person': get_phone_person,
                 'phone_work': get_phone_work,
                 'email': get_email,
                 'group': get_group,
                 'city': get_city,
                 },
            ],
        )
        sql.connection.close()

def show_SQL_Column():
    with connection as conn:
        result = conn.execute(
            select([PhoneBook.id, PhoneBook.first_name, PhoneBook.last_name, PhoneBook.patronymic, PhoneBook.birthday,
                    PhoneBook.phone_person, PhoneBook.phone_work, PhoneBook.email,
                    PhoneBook.group, PhoneBook.city]))
    print(result._metadata.keys)


def show_SQL_PhoneBook_all():
    show_SQL_Column()
    responses = session.query(PhoneBook).all()
    for result in responses:
        print(result)


def get_SQL_FoundContactBy_id():
    field = view.inputInt('Введите ID контакта: ')
    responses = session.query(PhoneBook).filter(PhoneBook.id == field).all()
    if responses == []:
        view.inputStr(f'Контакт с ID "{field}" не найден')
    else:
        for result in responses:
            print(result)


def get_SQL_FoundContactBy_first_name():
    field = view.inputStr('Введите имя контакта: ').title()
    responses = session.query(PhoneBook).filter(PhoneBook.first_name == field).all()
    if responses == []:
        view.inputStr(f'Контакт с именем "{field}" не найден')
    else:
        for result in responses:
            print(result)


def get_SQL_FoundContactBy_last_name():
    field = view.inputStr('Введите фамилию контакта: ').upper()
    responses = session.query(PhoneBook).filter(PhoneBook.last_name == field).all()
    if responses == []:
        view.inputStr(f'Контакт с фамилией "{field}" не найден')
    else:
        for result in responses:
            print(result)


def get_SQL_FoundContactBy_phone_person():
    field = view.inputStr('Введите номер телефона: ')
    responses = session.query(PhoneBook).filter(PhoneBook.phone_person == field).all()
    if responses == []:
        view.inputStr(f'Контакт с таким номером "{field}" не найден')
    else:
        for result in responses:
            print(result)


def get_SQL_DeleteContactBy_id():
    view.inputStr('РЕЖИМ УДАЛЕНИЯ КОНТАКТА')
    field = view.inputStr('Введите ID контакта: ')
    responses = session.query(PhoneBook).filter(PhoneBook.id == field).all()
    if responses == []:
        view.inputStr(f'Контакт с ID "{field}" не найден')
    else:
        for result in responses:
            print(result)
            view.inputStr('ВЫ ТОЧНО ХОТИТЕ УДАЛИТЬ ВЫБРАННЫЙ КОНТАКТ БЕЗ ВОЗМОЖНОСТИ ВОССТАНОВЛЕНИЯ?')
            delChoice = view.inputStr('Нажмите "1" для удаления или "0" для отмены!\n')
            if delChoice == '1':
                session.query(PhoneBook).filter(PhoneBook.id == field).delete()
                session.commit()
                view.inputStr(f'Выбранный контакт с ID "{field}" удалён!')
                # TODO: ниже должна быть отправка на главное меню
            else:
                view.inputStr(f'Вы отменили удаление контакта с ID "{field}"')
                # TODO: ниже должна быть отправка на главное меню



# show_SQL_PhoneBook_all()
# get_SQL_FoundContactBy_id()
# get_SQL_FoundContactBy_first_name()
# get_SQL_FoundContactBy_last_name()
# get_SQL_FoundContactBy_phone_person()
# get_SQL_DeleteContactBy_id()


def setExport_SQL_to_CSV():
    pass

input('Enter для выхода')

# with engine.connect() as conn:
#     result = conn.execute(
#         insert(table_phonebook),
#         [
#             {'first_name': 'Именной',
#              'last_name': 'Фимилиев',
#              'patronymic': 'Отчество',
#              # 'birthday': '22.11.1999',
#              'phone_person': '123456789',
#              'phone_work': '0987654321',
#              'email': 'mail@email.em',
#              # 'group': 'Группа',
#              'city': 'Славный город',
#              },
#             {'first_name': 'Иван',
#              'last_name': 'Иванов',
#              'patronymic': 'Иванович',
#              # 'birthday': '21-10-1949',
#              'phone_person': '1465456789',
#              'phone_work': '0987457321',
#              'email': 'mail@mail.em',
#              # 'group': 'Группа 2',
#              'city': 'Южный',
#              },
#             {'first_name': 'Пётр',
#              'last_name': 'Петров',
#              'patronymic': 'Петрович',
#              # 'birthday': '1929.12.01',
#              'phone_person': '1798745349',
#              'phone_work': '7790797834',
#              'email': 'mail@email.org',
#              # 'group': 'Группа 2',
#              'city': 'Северный',
#              },
#         ],
#     )
#     connection.close()


# stmt = insert(table_phonebook).values(first_name="Именной", last_name="Фимилиев", phone_person='123456789')
# with engine.connect() as conn:
#     result = connection.execute(stmt)
#     connection.close()
#
# compiled = stmt.compile()
# compiled.params()
