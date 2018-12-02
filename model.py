# База данных подключается здесь
# В БД входят Настройки, Мультиязычность
import sqlite3
import os

DEBUG = True


def settings():
    if os.path.exists('settings') == False:
        os.mkdir('settings')
    conn = sqlite3.connect("settings/settings.db")
    cursor = conn.cursor()
    TABLE = 'user_settings'
    try:
        sql = """DROP TABLE %s
            """ % TABLE
        cursor.execute(sql)
        print(cursor.fetchall())
    except sqlite3.OperationalError:
        if DEBUG:
            print('Таблицы не существует')
        pass
    finally:
        cursor.execute("""
                        CREATE TABLE %s
                        (volume integer, language integer, currency integer, 
                        graph integer, information integer)
                        """ % TABLE)
        cursor.execute("""
        CREATE TABLE api_keys
        (title text, api_key text, api_secret text)
        """)


def multi_language():
    if os.path.exists('settings') == False:
        os.mkdir('settings')
    conn = sqlite3.connect("settings/lang.db")
    cursor = conn.cursor()
    TABLE = 'language'
    try:
        sql = """DROP TABLE %s
        """ % TABLE
        cursor.execute(sql)
    except sqlite3.OperationalError:
        if DEBUG:
            print('Таблицы не существует')
        pass
    finally:
        cursor.execute("""
        CREATE TABLE %s
        (lan text, str0 text, str1 text, str2 text, str3 text, str4 text, str5 text, str6 text, str7 text, str8 text,
        str9 text, str10 text, str11 text, str12 text, str13 text, str14 text, str15 text, str16 text, str17 text,
        str18 text)
        """ % TABLE)
    language = [('EN', 'Menu', 'Sell signal', 'Buying signal', 'Enabled', 'Disabled', 'Viewing logs',
                 'Settings', 'Settings Program', 'More...', 'Help', 'About', 'Program settings', 'Bot Settings',
                 'Volume signal', 'Language', 'Show graph', 'Information on currency', 'Look', 'Copyright')]
    cursor.execute("INSERT INTO %s VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" % TABLE, language)
    conn.commit()


def change_language():
    conn = sqlite3.connect("settings/lang.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM language WHERE lan=?"
    cursor.execute(sql,[('EN')])
    return cursor.fetchall()