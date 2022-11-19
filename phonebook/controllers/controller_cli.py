from gb_groupwork.phonebook import views
from gb_groupwork.phonebook import models



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
