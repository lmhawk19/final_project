import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='diy_couples_therapy',
        user='admin',
        password='admin'
    )

