import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        database='diy_couples_therapy',
        user='root',
        password='Athelstan19'
    )

