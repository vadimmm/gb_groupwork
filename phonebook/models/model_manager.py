import model_CSV
import model_SQL


def show_PhoneBook_all(DB_TYPE):
    if DB_TYPE == CSV:
        show_CSV_PhoneBook_all()
    elif DB_TYPE == SQL:
        show_SQL_PhoneBook_all()
