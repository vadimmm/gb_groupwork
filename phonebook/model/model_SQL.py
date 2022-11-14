from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, select
from sqlalchemy import insert
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


### Создание базы данных
metadata = db.MetaData()
engine = db.create_engine("sqlite:///../DATA/sqlite.sqlite", echo=True)

connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()



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
        return f'{self.last_name.upper()} ' \
               f'{self.first_name.title()} ' \
               f'{self.patronymic} ' \
               f'{self.birthday} ' \
               f'{self.phone_person} ' \
               f'{self.phone_work} ' \
               f'{self.email} ' \
               f'{self.group} ' \
               f'{self.city} '


def show_SQL_Column():
    with connection as conn:
        result = conn.execute(
            select([PhoneBook.first_name, PhoneBook.last_name, PhoneBook.patronymic, PhoneBook.birthday,
                    PhoneBook.phone_person, PhoneBook.phone_work, PhoneBook.email,
                    PhoneBook.group, PhoneBook.city]))
    print(result._metadata.keys)


def show_SQL_PhoneBook_all():
    show_SQL_Column()
    responses = session.query(PhoneBook).all()
    for result in responses:
        print(result)


def get_SQL_FoundContact():
    foun = input('Запрос: ')
    # q = session.query(PhoneBook).filter(PhoneBook.first_name == foun)
    q = session.query(PhoneBook).filter(id != 2)
    print(session.query(q.exists()))


show_SQL_PhoneBook_all()
get_SQL_FoundContact()




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

