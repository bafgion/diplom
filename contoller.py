# -*- coding: utf-8 -*-
# Здесь подключается интерфейс и прописываются функции для программы
from view.views import *
from model import *
from ctypes import *
import threading
import sys
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtGui import QTextCursor
# Настройки программы
language = False
# ключи API, которые предоставила exmo
API_KEY = 'K-80d73ae557e763e3a6d7053a2f550afad9a236d2'
# обратите внимание, что добавлена 'b' перед строкой
API_SECRET = b'S-1216e426dd541c98810f95e82900967bd3f078d7'

        # Тонкая настройка
CURRENCY_1 = 'ZEC'
CURRENCY_2 = 'RUB'

CURRENCY_1_MIN_QUANTITY = 0.01  # минимальная сумма ставки - берется из https://api.exmo.com/v1/pair_settings/

ORDER_LIFE_TIME = 13  # через сколько минут отменять неисполненный ордер на покупку CURRENCY_1
STOCK_FEE = 0.002  # Комиссия, которую берет биржа (0.002 = 0.2%)
AVG_PRICE_PERIOD = 15  # За какой период брать среднюю цену (мин)
CAN_SPEND = 122  # Сколько тратить CURRENCY_2 каждый раз при покупке CURRENCY_1
PROFIT_MARKUP = 0.001  # Какой навар нужен с каждой сделки? (0.001 = 0.1%)
DEBUG = True  # True - выводить отладочную информацию, False - писать как можно меньше
STOCK_TIME_OFFSET = 0  # Если расходится время биржи с текущим
# Конец настроек


class OutputLogger(QObject):
    emit_write = Signal(str, int)

    class Severity:
        DEBUG = 0
        ERROR = 1

    def __init__(self, io_stream, severity):
        super().__init__()

        self.io_stream = io_stream
        self.severity = severity

    def write(self, text):
        self.io_stream.write(text)
        self.emit_write.emit(text, self.severity)

    def flush(self):
        self.io_stream.flush()


OUTPUT_LOGGER_STDOUT = OutputLogger(sys.stdout, OutputLogger.Severity.DEBUG)
OUTPUT_LOGGER_STDERR = OutputLogger(sys.stderr, OutputLogger.Severity.ERROR)

sys.stdout = OUTPUT_LOGGER_STDOUT
sys.stderr = OUTPUT_LOGGER_STDERR


class startWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_7.triggered.connect(self.open_help)
        self.ui.action_8.triggered.connect(self.open_about)
        self.ui.action_2.triggered.connect(self.open_settings)
        self.ui.action_3.triggered.connect(self.signal)
        self.ui.pushButton.clicked.connect(self.boter)
        self.ui.pushButton_3.clicked.connect(self.cancel)
        OUTPUT_LOGGER_STDOUT.emit_write.connect(self.append_log)
        if language:
            self.language_en()
        else:
            self.language_ru()
        self.a = True

    def cancel(self):
        self.a = False

    def append_log(self, text, severity):
        text = str(text).replace('\n', '')
        text_cursor = self.ui.plainTextEdit.textCursor()
        orig_fmt = text_cursor
        fmt = QTextCharFormat()

        if severity == OutputLogger.Severity.ERROR:
            self.ui.plainTextEdit.appendPlainText('<b>{}</b>'.format(text))
        else:
            text_cursor.movePosition(QTextCursor.End)
            text_cursor.setCharFormat(fmt)
            self.ui.plainTextEdit.appendPlainText(text)

    def boter(self):
        self.startebot = threading.Thread(target=self.bot)
        self.startebot.start()
        self.ui.plainTextEdit.setPlainText('')
        self.a = True

    def signal(self):
        self.ui.plainTextEdit.appendPlainText('0 0 0 0 0 0')

    def open_help(self):
        self.res = startHelp()
        self.res.show()

    def open_about(self):
        self.res = startAbout()
        self.res.show()

    def open_settings(self):
        self.res = startSettings()
        self.res.show()

    def language_en(self):
        _translate = QtCore.QCoreApplication.translate
        a = str(change_language())
        a = a.replace('[', '').replace(']','').replace('(', '').replace(')', '').replace("'", '')
        a = a.split(', ')
        self.ui.pushButton_3.setText(_translate("MainWindow", "Завершить работу"))
        self.ui.pushButton_4.setText(_translate("MainWindow", "Завершить работу"))
        self.setWindowTitle(_translate("MainWindow", "Bot Forsazh v1"))
        self.ui.menu.setTitle(_translate("MainWindow", a[1]))
        self.ui.menu_5.setTitle(_translate("MainWindow", a[2]))
        self.ui.menu_6.setTitle(_translate("MainWindow", a[3]))
        self.ui.menu_4.setTitle(_translate("MainWindow", a[7]))
        self.ui.menu_2.setTitle(_translate("MainWindow", a[9]))
        self.ui.action_3.setText(_translate("MainWindow", a[6]))
        self.ui.action_4.setText(_translate("MainWindow", a[4]))
        self.ui.action_5.setText(_translate("MainWindow", a[4]))
        self.ui.action_6.setText(_translate("MainWindow", a[5]))
        self.ui.action.setText(_translate("MainWindow", a[5]))
        self.ui.action_2.setText(_translate("MainWindow", a[8]))
        self.ui.action_7.setText(_translate("MainWindow", a[10]))
        self.ui.action_8.setText(_translate("MainWindow", a[11]))
        self.ui.pushButton.setText(_translate("MainWindow", "Запустить робота EXMO"))
        self.ui.plainTextEdit.setPlainText(_translate("MainWindow",
                                                      "Для начала работы робота установите настройки согласно пункту меню \"Еще - Помощь\" и нажмите кнопку \"Запустить робота EXMO/Poloniex\""))
        self.ui.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "EXMO"))
        self.ui.plainTextEdit_2.setPlainText(_translate("MainWindow",
                                                        "Для начала работы робота установите настройки согласно пункту меню \"Еще - Помощь\" и нажмите кнопку \"Запустить робота EXMO/Poloniex\""))
        self.ui.pushButton_2.setText(_translate("MainWindow", "Запустить робота Poloniex"))
        self.ui.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Poloniex"))

    def language_ru(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.pushButton_3.setText(_translate("MainWindow", "Завершить работу"))
        self.ui.pushButton_4.setText(_translate("MainWindow", "Завершить работу"))
        self.setWindowTitle(_translate("MainWindow", "Бот Форсаж v1"))
        self.ui.menu.setTitle(_translate("MainWindow", "Меню"))
        self.ui.menu_4.setTitle(_translate("MainWindow", "Настройки"))
        self.ui.menu_2.setTitle(_translate("MainWindow", "Еще..."))
        self.ui.action_3.setText(_translate("MainWindow", "Выход"))
        self.ui.action_2.setText(_translate("MainWindow", "Настройки программы"))
        self.ui.action_7.setText(_translate("MainWindow", "Помощь"))
        self.ui.action_8.setText(_translate("MainWindow", "О программе"))
        self.ui.pushButton.setText(_translate("MainWindow", "Запустить робота EXMO"))
        self.ui.plainTextEdit.setPlainText(_translate("MainWindow",
                                                   "Для начала работы робота установите настройки согласно пункту меню \"Еще - Помощь\" и нажмите кнопку \"Запустить робота EXMO/Poloniex\""))
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab), _translate("MainWindow", "EXMO"))
        self.ui.plainTextEdit_2.setPlainText(_translate("MainWindow",
                                                     "Для начала работы робота установите настройки согласно пункту меню \"Еще - Помощь\" и нажмите кнопку \"Запустить робота EXMO/Poloniex\""))
        self.ui.pushButton_2.setText(_translate("MainWindow", "Запустить робота Poloniex"))
        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.tab_2), _translate("MainWindow", "Poloniex"))

    def bot(self):
        import urllib, http.client, urllib.parse
        import time
        import json
        # эти модули нужны для генерации подписи API
        import hmac, hashlib

        # базовые настройки
        API_URL = 'api.exmo.me'
        API_VERSION = 'v1'
        a = True
        # Свой класс исключений
        class ScriptError(Exception):
            pass

        class ScriptQuitCondition(Exception):
            pass

        CURRENT_PAIR = CURRENCY_1 + '_' + CURRENCY_2

        # все обращения к API проходят через эту функцию
        def call_api(api_method, http_method="POST", **kwargs):
            # Составляем словарь {ключ:значение} для отправки на биржу
            # пока что в нём {'nonce':123172368123}
            payload = {'nonce': int(round(time.time() * 1000))}

            # Если в ф-цию переданы параметры в формате ключ:значение
            if kwargs:
                # добавляем каждый параметр в словарь payload
                # Получится {'nonce':123172368123, 'param1':'val1', 'param2':'val2'}
                payload.update(kwargs)

            # Переводим словарь payload в строку, в формат для отправки через GET/POST и т.п.
            payload = urllib.parse.urlencode(payload)

            # Из строки payload получаем "подпись", хешируем с помощью секретного ключа API
            # sing - получаемый ключ, который будет отправлен на биржу для проверки
            H = hmac.new(key=API_SECRET, digestmod=hashlib.sha512)
            H.update(payload.encode('utf-8'))
            sign = H.hexdigest()

            # Формируем заголовки request для отправки запроса на биржу.
            # Передается публичный ключ API и подпись, полученная с помощью hmac
            headers = {"Content-type": "application/x-www-form-urlencoded",
                       "Key": API_KEY,
                       "Sign": sign}

            # Создаем подключение к бирже, если в течении 60 сек не удалось подключиться, обрыв соединения
            conn = http.client.HTTPSConnection(API_URL, timeout=60)
            # После установления связи, запрашиваем переданный адрес
            # В заголовке запроса уходят headers, в теле - payload
            conn.request(http_method, "/" + API_VERSION + "/" + api_method, payload, headers)
            # Получаем ответ с биржи и читаем его в переменную response
            response = conn.getresponse().read()
            # Закрываем подключение
            conn.close()

            try:
                # Полученный ответ переводим в строку UTF, и пытаемся преобразовать из текста в объект Python
                obj = json.loads(response.decode('utf-8'))

                # Смотрим, есть ли в полученном объекте ключ "error"
                if 'error' in obj and obj['error']:
                    # Если есть, выдать ошибку, код дальше выполняться не будет
                    raise ScriptError(obj['error'])
                # Вернуть полученный объект как результат работы ф-ции
                return obj
            except ValueError:
                # Если не удалось перевести полученный ответ (вернулся не JSON)
                raise ScriptError('Ошибка анализа возвращаемых данных, получена строка %s' % response)

        # Реализация алгоритма
        def main_flow():

            try:
                # Получаем список активных ордеров
                try:
                    opened_orders = call_api('user_open_orders')[CURRENCY_1 + '_' + CURRENCY_2]
                except KeyError:
                    if DEBUG:
                        print('Открытых ордеров нет')
                    opened_orders = []

                sell_orders = []
                # Есть ли неисполненные ордера на продажу CURRENCY_1?
                for order in opened_orders:
                    if order['type'] == 'sell':
                        # Есть неисполненные ордера на продажу CURRENCY_1, выход
                        raise ScriptQuitCondition(
                            'Выход, ждем пока не исполнятся/закроются все ордера на продажу (один ордер может быть разбит биржей на несколько и исполняться частями)')
                    else:
                        # Запоминаем ордера на покупку CURRENCY_1
                        sell_orders.append(order)

                # Проверяем, есть ли открытые ордера на покупку CURRENCY_1
                if sell_orders:  # открытые ордера есть
                    for order in sell_orders:
                        # Проверяем, есть ли частично исполненные
                        if DEBUG:
                            print('Проверяем, что происходит с отложенным ордером', order['order_id'])
                        try:
                            order_history = call_api('order_trades', order_id=order['order_id'])
                            # по ордеру уже есть частичное выполнение, выход
                            raise ScriptQuitCondition(
                                'Выход, продолжаем надеяться докупить валюту по тому курсу, по которому уже купили часть')
                        except ScriptError as e:
                            if 'Error 50304' in str(e):
                                if DEBUG:
                                    print('Частично исполненных ордеров нет')

                                time_passed = time.time() + STOCK_TIME_OFFSET * 60 * 60 - int(order['created'])

                                if time_passed > ORDER_LIFE_TIME * 60:
                                    # Ордер уже давно висит, никому не нужен, отменяем
                                    call_api('order_cancel', order_id=order['order_id'])
                                    raise ScriptQuitCondition(
                                        'Отменяем ордер за ' + str(ORDER_LIFE_TIME) + ' минут не удалось купить ' + str(
                                            CURRENCY_1))
                                else:
                                    raise ScriptQuitCondition(
                                        'Выход, продолжаем надеяться купить валюту по указанному ранее курсу, со времени создания ордера прошло %s секунд' % str(
                                            time_passed))
                            else:
                                raise ScriptQuitCondition(str(e))

                else:  # Открытых ордеров нет
                    balances = call_api('user_info')['balances']
                    if float(balances[
                                 CURRENCY_1]) >= CURRENCY_1_MIN_QUANTITY:  # Есть ли в наличии CURRENCY_1, которую можно продать?
                        """
                            Высчитываем курс для продажи.
                            Нам надо продать всю валюту, которую купили, на сумму, за которую купили + немного навара и минус комиссия биржи
                            При этом важный момент, что валюты у нас меньше, чем купили - бирже ушла комиссия
                            0.00134345 1.5045
                        """
                        wanna_get = CAN_SPEND + CAN_SPEND * (
                                STOCK_FEE + PROFIT_MARKUP)  # сколько хотим получить за наше кол-во
                        print('sell', balances[CURRENCY_1], wanna_get, (wanna_get / float(balances[CURRENCY_1])))
                        new_order = call_api(
                            'order_create',
                            pair=CURRENT_PAIR,
                            quantity=balances[CURRENCY_1],
                            price=wanna_get / float(balances[CURRENCY_1]),
                            type='sell'
                        )
                        print(new_order)
                        if DEBUG:
                            print('Создан ордер на продажу', CURRENCY_1, new_order['order_id'])
                    else:
                        # CURRENCY_1 нет, надо докупить
                        # Достаточно ли денег на балансе в валюте CURRENCY_2 (Баланс >= CAN_SPEND)
                        if float(balances[CURRENCY_2]) >= CAN_SPEND:
                            # Узнать среднюю цену за AVG_PRICE_PERIOD, по которой продают CURRENCY_1
                            """
                             Exmo не предоставляет такого метода в API, но предоставляет другие, к которым можно попробовать привязаться.
                             У них есть метод required_total, который позволяет подсчитать курс, но,
                                 во-первых, похоже он берет текущую рыночную цену (а мне нужна в динамике), а
                                 во-вторых алгоритм расчета скрыт и может измениться в любой момент.
                             Сейчас я вижу два пути - либо смотреть текущие открытые ордера, либо последние совершенные сделки.
                             Оба варианта мне не слишком нравятся, но завершенные сделки покажут реальные цены по которым продавали/покупали,
                             а открытые ордера покажут цены, по которым только собираются продать/купить - т.е. завышенные и заниженные.
                             Так что берем информацию из завершенных сделок.
                            """
                            deals = call_api('trades', pair=CURRENT_PAIR)
                            prices = []
                            for deal in deals[CURRENT_PAIR]:
                                time_passed = time.time() + STOCK_TIME_OFFSET * 60 * 60 - int(deal['date'])
                                if time_passed < AVG_PRICE_PERIOD * 60:
                                    prices.append(float(deal['price']))
                            try:
                                avg_price = sum(prices) / len(prices)
                                """
                                    Посчитать, сколько валюты CURRENCY_1 можно купить.
                                    На сумму CAN_SPEND за минусом STOCK_FEE, и с учетом PROFIT_MARKUP
                                    ( = ниже средней цены рынка, с учетом комиссии и желаемого профита)
                                """
                                # купить больше, потому что биржа потом заберет кусок
                                my_need_price = avg_price - avg_price * (STOCK_FEE + PROFIT_MARKUP)
                                my_amount = CAN_SPEND / my_need_price

                                print('buy %f %f' % (my_amount, my_need_price))

                                # Допускается ли покупка такого кол-ва валюты (т.е. не нарушается минимальная сумма сделки)
                                if my_amount >= CURRENCY_1_MIN_QUANTITY:
                                    new_order = call_api(
                                        'order_create',
                                        pair=CURRENT_PAIR,
                                        quantity=my_amount,
                                        price=my_need_price,
                                        type='buy'
                                    )
                                    print(new_order)
                                    if DEBUG:
                                        print('Создан ордер на покупку', new_order['order_id'])

                                else:  # мы можем купить слишком мало на нашу сумму
                                    raise ScriptQuitCondition('Выход, не хватает денег на создание ордера')
                            except ZeroDivisionError:
                                print('Не удается вычислить среднюю цену', prices)
                        else:
                            raise ScriptQuitCondition('Выход, не хватает денег')

            except ScriptError as e:
                print(e)
            except ScriptQuitCondition as e:
                if DEBUG:
                    print(e)
                pass
            except Exception as e:
                print("!!!!", e)

        a = True
        while a != False:
            main_flow()
            time.sleep(1)
            if self.a == False:
                a = False



class startHelp(QtWidgets.QMainWindow, Ui_HelpWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.action_8.triggered.connect(self.open_settings)
        self.action_10.triggered.connect(self.open_about)
        if language:
            self.language_en()
        else:
            self.language_ru()
        self.addTreeView()
        self.commandLinkButton.clicked.connect(self.test)

    def test(self):
        _translate = QtCore.QCoreApplication.translate
        index = self.treeView.currentIndex().row()
        if index == 0:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html><head><meta name="qrichtext" content="1" /><style type="text/css">
            p, li { white-space: pre-wrap; }    
            </style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа разработана специально для диломного проекта<br /><br />Разработчик Минковский Никита Александрович</span></p>
            <p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;"><br /></p>
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Все права защищены 2018</span></p></body></html>"""))
        elif index == 1:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа может торговать на биржах EXMO, Poloniex путем подключения через выдываемые биржей ключи шифрования.<br />В данный момент в программе можно настроить алгоритм робота, а именно:<br />Валютную пару,<br />Интервал статистики,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Количество покупаемой валюты,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Минимальная стоимость валюты.</span></p></body></html>"""))
        elif index == 2:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа может торговать на биржах EXMO, Poloniex путем подключения через выдываемые биржей ключи шифрования.<br />В данный момент в программе можно настроить алгоритм робота, а именно:<br />Валютную пару,<br />Интервал статистики,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Количество покупаемой валюты,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Минимальная стоимость валюты.</span></p></body></html>"""))
        elif index == 3:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа может торговать на биржах EXMO, Poloniex путем подключения через выдываемые биржей ключи шифрования.<br />В данный момент в программе можно настроить алгоритм робота, а именно:<br />Валютную пару,<br />Интервал статистики,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Количество покупаемой валюты,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Минимальная стоимость валюты.</span></p></body></html>"""))

        elif index == 4:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа может торговать на биржах EXMO, Poloniex путем подключения через выдываемые биржей ключи шифрования.<br />В данный момент в программе можно настроить алгоритм робота, а именно:<br />Валютную пару,<br />Интервал статистики,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Количество покупаемой валюты,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Минимальная стоимость валюты.</span></p></body></html>"""))

        elif index == 5:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа может торговать на биржах EXMO, Poloniex путем подключения через выдываемые биржей ключи шифрования.<br />В данный момент в программе можно настроить алгоритм робота, а именно:<br />Валютную пару,<br />Интервал статистики,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Количество покупаемой валюты,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Минимальная стоимость валюты.</span></p></body></html>"""))

        elif index == 6:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа может торговать на биржах EXMO, Poloniex путем подключения через выдываемые биржей ключи шифрования.<br />В данный момент в программе можно настроить алгоритм робота, а именно:<br />Валютную пару,<br />Интервал статистики,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Количество покупаемой валюты,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Минимальная стоимость валюты.</span></p></body></html>"""))

        elif index == 7:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа может торговать на биржах EXMO, Poloniex путем подключения через выдываемые биржей ключи шифрования.<br />В данный момент в программе можно настроить алгоритм робота, а именно:<br />Валютную пару,<br />Интервал статистики,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Количество покупаемой валюты,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Минимальная стоимость валюты.</span></p></body></html>"""))

        elif index == 8:
            self.textEdit.setHtml(_translate("MainWindow",
                                             """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Программа может торговать на биржах EXMO, Poloniex путем подключения через выдываемые биржей ключи шифрования.<br />В данный момент в программе можно настроить алгоритм робота, а именно:<br />Валютную пару,<br />Интервал статистики,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Количество покупаемой валюты,</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8.25pt;">Минимальная стоимость валюты.</span></p></body></html>"""))


    def addTreeView(self):
        # Введение
        self.model = QtGui.QStandardItemModel(self.treeView)
        self.parent_item = QtGui.QStandardItem('О программе')
        self.parent_item.setData("this is a parent", QtCore.Qt.ToolTipRole)
        self.model.appendRow(self.parent_item)
        self.parent_item = QtGui.QStandardItem('Возможности')
        self.parent_item.setData("this is a parent", QtCore.Qt.ToolTipRole)
        self.model.appendRow(self.parent_item)
        self.parent_item = QtGui.QStandardItem('Системные требования')
        self.parent_item.setData("this is a parent", QtCore.Qt.ToolTipRole)
        self.model.appendRow(self.parent_item)
        # Работа робота
        self.parent_item = QtGui.QStandardItem('Настройка API')
        self.parent_item.setData("this is a parent", QtCore.Qt.ToolTipRole)
        self.model.appendRow(self.parent_item)
        self.parent_item = QtGui.QStandardItem('График робота')
        self.parent_item.setData("this is a parent", QtCore.Qt.ToolTipRole)
        self.model.appendRow(self.parent_item)
        self.parent_item = QtGui.QStandardItem('Информация о валютной паре')
        self.parent_item.setData("this is a parent", QtCore.Qt.ToolTipRole)
        self.model.appendRow(self.parent_item)
        # Меню настроек
        self.parent_item = QtGui.QStandardItem('Выбор валюты для торговли')
        self.parent_item.setData("this is a parent", QtCore.Qt.ToolTipRole)
        self.model.appendRow(self.parent_item)
        self.parent_item = QtGui.QStandardItem('Ввод значений API')
        self.parent_item.setData("this is a parent", QtCore.Qt.ToolTipRole)
        self.model.appendRow(self.parent_item)
        #
        self.treeView.setModel(self.model)

    def open_about(self):
        self.res = startAbout()
        self.res.show()
        self.close()

    def open_settings(self):
        self.res = startSettings()
        self.res.show()
        self.close()

    def language_en(self):
        a = str(change_language())
        a = a.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace("'", '')
        a = a.split(', ')
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", a[10]))
        self.commandLinkButton.setText(_translate("MainWindow", "Show"))
        self.menu.setTitle(_translate("MainWindow", a[1]))
        self.menu_2.setTitle(_translate("MainWindow", a[2]))
        self.menu_3.setTitle(_translate("MainWindow", a[3]))
        self.menu_4.setTitle(_translate("MainWindow", a[7]))
        self.menu_5.setTitle(_translate("MainWindow", a[9]))
        self.action_3.setText(_translate("MainWindow", a[6]))
        self.action_4.setText(_translate("MainWindow", a[4]))
        self.action_5.setText(_translate("MainWindow", a[5]))
        self.action_6.setText(_translate("MainWindow", a[4]))
        self.action_7.setText(_translate("MainWindow", a[5]))
        self.action_8.setText(_translate("MainWindow", a[8]))
        self.action_9.setText(_translate("MainWindow", a[10]))
        self.action_10.setText(_translate("MainWindow", a[11]))

    def language_ru(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Помощь"))
        self.commandLinkButton.setText(_translate("MainWindow", "Показать"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_4.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_5.setTitle(_translate("MainWindow", "Еще..."))
        self.action_3.setText(_translate("MainWindow", "Выход"))
        self.action_8.setText(_translate("MainWindow", "Настройки программы"))
        self.action_9.setText(_translate("MainWindow", "Помощь"))
        self.action_10.setText(_translate("MainWindow", "О программе"))


class startSettings(QtWidgets.QMainWindow, Ui_SettingsWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.action_9.triggered.connect(self.open_help)
        self.action_10.triggered.connect(self.open_about)
        if language:
            _translate = QtCore.QCoreApplication.translate
            self.language_en()
            self.comboBox.setCurrentText(_translate("MainWindow", "English"))
        else:
            _translate = QtCore.QCoreApplication.translate
            self.language_ru()
            self.comboBox.setCurrentText(_translate("MainWindow", "Русский"))
        self.comboBox.activated[str].connect(self.change_lang)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        # ключи API, которые предоставила exmo
        global API_KEY # = 'K-80d73ae557e763e3a6d7053a2f550afad9a236d2'
        # обратите внимание, что добавлена 'b' перед строкой
        global API_SECRET # = b'S-1216e426dd541c98810f95e82900967bd3f078d7'
        global CURRENCY_1
        global CURRENCY_2
        global ORDER_LIFE_TIME
        global AVG_PRICE_PERIOD
        global CAN_SPEND
        global PROFIT_MARKUP
        global STOCK_TIME_OFFSET
        API_KEY = str(self.lineEdit_2.text())
        API_SECRET = bytes(str(self.lineEdit.text()), 'utf-8')
        # Тонкая настройка
        CURRENCY_1 = str(self.lineEdit.text())
        CURRENCY_2 = str(self.lineEdit_2.text())

        CURRENCY_1_MIN_QUANTITY = 0.01  # минимальная сумма ставки - берется из https://api.exmo.com/v1/pair_settings/

        ORDER_LIFE_TIME = int(self.spinBox_2.text())  # через сколько минут отменять неисполненный ордер на покупку CURRENCY_1
        AVG_PRICE_PERIOD = int(self.spinBox.text())  # За какой период брать среднюю цену (мин)
        CAN_SPEND = float(self.doubleSpinBox_2.text())  # Сколько тратить CURRENCY_2 каждый раз при покупке CURRENCY_1
        PROFIT_MARKUP = float(self.doubleSpinBox.text())  # Какой навар нужен с каждой сделки? (0.001 = 0.1%)
        DEBUG = False  # True - выводить отладочную информацию, False - писать как можно меньше
        STOCK_TIME_OFFSET = 0  # Если расходится время биржи с текущим
        pass

    def change_lang(self, text):
        global language
        if text == 'English':
            language = True
            self.language_en()
            startWindow().update()
        else:
            language = False
            self.language_ru()

    def open_about(self):
        self.res = startAbout()
        self.res.show()
        self.close()

    def open_help(self):
        self.res = startHelp()
        self.res.show()
        self.close()

    def language_en(self):
        a = str(change_language())
        a = a.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace("'", '')
        a = a.split(', ')
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", a[7]))
        self.label_2.setText(_translate("MainWindow", a[15]))
        self.comboBox.setCurrentText(_translate("MainWindow", "English"))
        self.comboBox.setItemText(0, _translate("MainWindow", "English"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Русский"))
        self.label_11.setText(_translate("MainWindow", "Интервал статистики"))
        self.label_12.setText(_translate("MainWindow", "Профит сделки в %"))
        self.label.setText(_translate("MainWindow", "Время отмены ордера"))
        self.label_13.setText(_translate("MainWindow", "Сколько тратить 2 при покупке 1"))
        self.checkBox.setText(_translate("MainWindow", a[16]))
        self.checkBox_2.setText(_translate("MainWindow", a[17]))
        self.label_3.setText(_translate("MainWindow", a[12]))
        self.label_3.adjustSize()
        self.label_4.setText(_translate("MainWindow", a[13]))
        self.label_4.adjustSize()
        self.label_5.setText(_translate("MainWindow", "Данные биржи EXMO"))
        self.label_7.setText(_translate("MainWindow", "Secret API"))
        self.label_8.setText(_translate("MainWindow", "API KEY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_6.setText(_translate("MainWindow", "Данные биржи Poloniex"))
        self.label_9.setText(_translate("MainWindow", "Secret API"))
        self.label_10.setText(_translate("MainWindow", "API KEY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menu.setTitle(_translate("MainWindow", a[1]))
        self.menu_2.setTitle(_translate("MainWindow", a[2]))
        self.menu_3.setTitle(_translate("MainWindow", a[3]))
        self.menu_4.setTitle(_translate("MainWindow", a[7]))
        self.menu_5.setTitle(_translate("MainWindow", a[9]))
        self.action_3.setText(_translate("MainWindow", a[6]))
        self.action_4.setText(_translate("MainWindow", a[4]))
        self.action_5.setText(_translate("MainWindow", a[5]))
        self.action_6.setText(_translate("MainWindow", a[4]))
        self.action_7.setText(_translate("MainWindow", a[5]))
        self.label_14.setText(_translate("MainWindow", "/"))
        self.label_15.setText(_translate("MainWindow", "Валютная пара"))
        self.action_8.setText(_translate("MainWindow", a[8]))
        self.action_9.setText(_translate("MainWindow", a[10]))
        self.action_10.setText(_translate("MainWindow", a[11]))
        self.pushButton.setText(_translate("MainWindow", "Сохранить настройки"))
        self.pushButton_2.setText(_translate("MainWindow", "Стандартные\n"
                                                           "настройки"))

    def language_ru(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Выбор языка"))
        self.comboBox.setCurrentText(_translate("MainWindow", "English"))
        self.comboBox.setItemText(0, _translate("MainWindow", "English"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Русский"))
        self.label_11.setText(_translate("MainWindow", "Интервал статистики"))
        self.label_12.setText(_translate("MainWindow", "Профит сделки в %"))
        self.label.setText(_translate("MainWindow", "Время отмены ордера"))
        self.label_13.setText(_translate("MainWindow", "Сколько тратить 2 при покупке 1"))
        self.label_3.setText(_translate("MainWindow", "Настройки программы"))
        self.label_4.setText(_translate("MainWindow", "Настройки бота"))
        self.label_5.setText(_translate("MainWindow", "Данные биржи EXMO"))
        self.label_7.setText(_translate("MainWindow", "Secret API"))
        self.label_8.setText(_translate("MainWindow", "API KEY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_6.setText(_translate("MainWindow", "Данные биржи Poloniex"))
        self.label_9.setText(_translate("MainWindow", "Secret API"))
        self.label_10.setText(_translate("MainWindow", "API KEY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить настройки"))
        self.pushButton_2.setText(_translate("MainWindow", "Стандартные\n"
                                                           "настройки"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_4.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_5.setTitle(_translate("MainWindow", "Еще..."))
        self.action_3.setText(_translate("MainWindow", "Выход"))
        self.action_8.setText(_translate("MainWindow", "Настройки программы"))
        self.action_9.setText(_translate("MainWindow", "Помощь"))
        self.label_14.setText(_translate("MainWindow", "/"))
        self.label_15.setText(_translate("MainWindow", "Валютная пара"))
        self.action_10.setText(_translate("MainWindow", "О программе"))


class startAbout(QtWidgets.QMainWindow, Ui_AboutWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.action_8.triggered.connect(self.open_settings)
        self.action_9.triggered.connect(self.open_help)
        self.setWindowModality(QtCore.Qt.WindowModal)
        if language:
            self.language_en()
        else:
            self.language_ru()
        self.textEdit.setReadOnly(True)

    def open_help(self):
        self.res = startHelp()
        self.res.show()
        self.close()

    def open_settings(self):
        self.res = startSettings()
        self.res.show()
        self.close()

    def language_en(self):
        a = str(change_language())
        a = a.replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace("'", '')
        a = a.split(', ')
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", a[11]))
        self.label.setText(_translate("MainWindow", a[19] + " 2018"))
        self.label.adjustSize()
        self.menu.setTitle(_translate("MainWindow", a[1]))
        self.menu_5.setTitle(_translate("MainWindow", a[2]))
        self.menu_6.setTitle(_translate("MainWindow", a[3]))
        self.menu_2.setTitle(_translate("MainWindow", a[7]))
        self.menu_3.setTitle(_translate("MainWindow", a[9]))
        self.action_3.setText(_translate("MainWindow", a[6]))
        self.action_4.setText(_translate("MainWindow", a[4]))
        self.action_5.setText(_translate("MainWindow", a[5]))
        self.action_6.setText(_translate("MainWindow", a[4]))
        self.action_7.setText(_translate("MainWindow", a[5]))
        self.action_8.setText(_translate("MainWindow", a[8]))
        self.action_9.setText(_translate("MainWindow", a[10]))
        self.action_10.setText(_translate("MainWindow", a[11]))
        self.textEdit.setHtml(_translate("MainWindow",
        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-weight:600; color:#000000;\">Торгово-арбитражный робот Форсаж v1.0</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">GUI-интерфейс Торгово-арбитражный робот Форсаж, версия 1.0 от 13.06.2018</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">Авторские права © Минковский Никита</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">ПО \'Торгово-арбитражный робот Форсаж\' предназначено для проведения торгов на онлайн биржах</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">Применение ПО избавляет от человеческого фактора при работа с онлайн биржами.</span></p></body></html>"))

    def language_ru(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Все права защищены 2018"))
        self.label.adjustSize()
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_3.setTitle(_translate("MainWindow", "Еще..."))
        self.action_3.setText(_translate("MainWindow", "Выход"))
        self.action_8.setText(_translate("MainWindow", "Настройки программы"))
        self.action_9.setText(_translate("MainWindow", "Помощь"))
        self.action_10.setText(_translate("MainWindow", "О программе"))
        self.textEdit.setHtml(_translate("MainWindow",
        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; font-weight:600; color:#000000;\">Торгово-арбитражный робот Форсаж v1.0</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">GUI-интерфейс Торгово-арбитражный робот Форсаж, версия 1.0 от 13.06.2018</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">Авторские права © Минковский Никита</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">ПО \'Торгово-арбитражный робот Форсаж\' предназначено для проведения торгов на онлайн биржах</span></p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">Применение ПО избавляет от человеческого фактора при работа с онлайн биржами.</span></p></body></html>"))



def startapp():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = startWindow()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    test = threading.Thread(target=startapp)
    test.start()