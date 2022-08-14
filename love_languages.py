from database import get_db_connection
import random


class LoveLanguage:

    def __init__(self, id):
        self.id = id
        self.__name = self.initialise_name()
        self.__description = self.initialise_description()

    def initialise_name(self):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT name FROM love_languages WHERE id = %s', [self.id])
                return cursor.fetchone()['name']

    def initialise_description(self):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT description FROM love_languages WHERE id = %s', [self.id])
                return cursor.fetchone()['description']

    def get_all_suggestions(self):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT content FROM suggestions WHERE love_language_id = %s', [self.id])
                return [suggestion['content'] for suggestion in cursor.fetchall()]

    def get_random_suggestions(self):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT content, url, suggester, starred FROM suggestions WHERE love_language_id = %s', [self.id])
                return random.sample(cursor.fetchall(), k=10)

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description


class WordsOfAffirmation(LoveLanguage):

    def __init__(self):
        super().__init__(1)


class QualityTime(LoveLanguage):

    def __init__(self):
        super().__init__(2)


class ActsOfService(LoveLanguage):

    def __init__(self):
        super().__init__(3)


class ReceivingGifts(LoveLanguage):

    def __init__(self):
        super().__init__(4)


class PhysicalTouch(LoveLanguage):

    def __init__(self):
        super().__init__(5)


def add_suggestion(name, suggestion, category, url):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('INSERT INTO suggestions (love_language_id, content, url, suggester) VALUES (%s, %s, %s, %s)',
                           [category, suggestion, url, name])
            connection.commit()
