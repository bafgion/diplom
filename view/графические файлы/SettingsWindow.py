# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 30, 251, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 161, 22))
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(280, 30, 341, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(210, 20, 111, 22))
        self.spinBox.setMinimum(5)
        self.spinBox.setMaximum(30)
        self.spinBox.setProperty("value", 15)
        self.spinBox.setObjectName("spinBox")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(210, 0, 111, 16))
        self.label_11.setObjectName("label_11")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(210, 70, 111, 22))
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMinimum(0.001)
        self.doubleSpinBox.setMaximum(0.015)
        self.doubleSpinBox.setSingleStep(0.001)
        self.doubleSpinBox.setProperty("value", 0.001)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(210, 50, 111, 16))
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(200, 100, 121, 16))
        self.label.setObjectName("label")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_2.setGeometry(QtCore.QRect(210, 120, 111, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(10)
        self.spinBox_2.setProperty("value", 3)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 0, 181, 16))
        self.label_13.setObjectName("label_13")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(10, 20, 171, 22))
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setMinimum(0.001)
        self.doubleSpinBox_2.setMaximum(1000.99)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setProperty("value", 0.01)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 90, 61, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 90, 61, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(80, 90, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_15.setObjectName("label_15")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 10, 101, 16))
        self.label_4.setObjectName("label_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 210, 341, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 311, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(0, 20, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 110, 311, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 60, 311, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_10.setObjectName("label_10")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(0, 20, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 210, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 210, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action_3)
        self.menu_4.addAction(self.action_8)
        self.menu_5.addAction(self.action_9)
        self.menu_5.addAction(self.action_10)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Выбор языка"))
        self.comboBox.setCurrentText(_translate("MainWindow", "English"))
        self.comboBox.setItemText(0, _translate("MainWindow", "English"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Русский"))
        self.label_11.setText(_translate("MainWindow", "Интервал статистики"))
        self.label_12.setText(_translate("MainWindow", "Профит сделки в %"))
        self.label.setText(_translate("MainWindow", "Время отмены ордера"))
        self.label_13.setText(_translate("MainWindow", "Сколько тратить 2 при покупке 1"))
        self.label_14.setText(_translate("MainWindow", "/"))
        self.label_15.setText(_translate("MainWindow", "Валютная пара"))
        self.label_3.setText(_translate("MainWindow", "Настройки программы"))
        self.label_4.setText(_translate("MainWindow", "Настройки робота"))
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
        self.menu_2.setTitle(_translate("MainWindow", "Сигнал продажи"))
        self.menu_3.setTitle(_translate("MainWindow", "Сигнал покупки"))
        self.menu_4.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_5.setTitle(_translate("MainWindow", "Еще..."))
        self.action_3.setText(_translate("MainWindow", "Просмотр логов"))
        self.action_4.setText(_translate("MainWindow", "Включить"))
        self.action_5.setText(_translate("MainWindow", "Отключить"))
        self.action_6.setText(_translate("MainWindow", "Включить"))
        self.action_7.setText(_translate("MainWindow", "Отключить"))
        self.action_8.setText(_translate("MainWindow", "Настройки программы"))
        self.action_9.setText(_translate("MainWindow", "Помощь"))
        self.action_10.setText(_translate("MainWindow", "О программе"))

