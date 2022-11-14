from phonebook import view
from phonebook import model



def set_SQL_NewContact():
    view.ShowInfo('Введите имя контакта: ')
    get_first_name = view.getString()
    view.ShowInfo('Введите фамилию контакта: ')
    get_last_name = view.getString()
    view.ShowInfo('Введите отчество контакта: ')
    get_patronymic = view.getString()
    view.ShowInfo('Введите дату ДР контакта: ')
    get_birthday = view.getString()
    view.ShowInfo('Введите мобильный телефон контакта: ')
    get_phone_person = view.getString()
    view.ShowInfo('Введите рабочий телефон контакта: ')
    get_phone_work = view.getString()
    view.ShowInfo('Введите email контакта: ')
    get_email = view.getString()
    view.ShowInfo('Введите группу контакта: ')
    get_group = view.getString()
    view.ShowInfo('Введите город контакта: ')
    get_city = view.getString()

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
