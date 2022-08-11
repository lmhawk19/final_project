import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database= 'input_feature',
        user='student', #discuss w emily
        password='student' #discuss w emily
    )


def get_user():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT *
                                FROM users AS u""")
            results = cursor.fetchall()
            for row in results:
                print(row)


def add_user(username, love_language, activity):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT
                                INTO users
                                     (username, love_language, activity)
                              VALUES (%s, %s, %s)""", [username, love_language, activity])
            connection.commit()


def get_activity_by_love_language(love_language):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT username,
                                     love_language,
                                     activity
                                FROM users AS s
                               WHERE love_language = %s""", [love_language])
            result = cursor.fetchone()
            print(result)

get_activity_by_love_language("words_of_affirmation")