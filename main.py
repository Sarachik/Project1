import random
import sys
import io
import datetime
import sqlite3

from res_rc import *
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PasswordGeneratorWindowTemplate import PasswordGeneratorTemplate
from LastPasswordsWindowTemplate import LastPasswordsTemplate


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(PasswordGeneratorTemplate)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.generate)
        self.pushButton_2.clicked.connect(self.last_passwords)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.time)
        QtCore.QTimer.singleShot(100, self.timer.start)
        self.time()

    def time(self):
        DateTime = datetime.datetime.now()

        self.label.setText('Дата: %s/%s/%s' % (DateTime.day, DateTime.month, DateTime.year))
        self.label_2.setText('Время: %s:%s:%s' % (DateTime.hour, DateTime.minute, DateTime.second))

    def generate(self):
        try:
            number = int(self.lineEdit.text())
            password = ''
            self.label_4.setText('')

            if self.radioButton.isChecked():
                lower_latinAlphabet = list('abcdefghijklmnopqrstuvwxyz'
                                           '123456789')
                for _ in range(number):
                    password += random.choice(lower_latinAlphabet)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_2.isChecked():
                lower_rusAlphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                         '123456789')
                for _ in range(number):
                    password += random.choice(lower_rusAlphabet)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_3.isChecked():
                lower_latinAlphabet_and_specialSymbols = list('abcdefghijklmnopqrstuvwxyz!*_'
                                                              '123456789')
                for _ in range(number):
                    password += random.choice(lower_latinAlphabet_and_specialSymbols)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_4.isChecked():
                lower_rusAlphabet_and_specialSymbols = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя!*_'
                                                            '123456789')
                for _ in range(number):
                    password += random.choice(lower_rusAlphabet_and_specialSymbols)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_5.isChecked():
                upper_latinAlphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                           '123456789')
                for _ in range(number):
                    password += random.choice(upper_latinAlphabet)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_6.isChecked():
                upper_rusAlphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
                                         '123456789')
                for _ in range(number):
                    password += random.choice(upper_rusAlphabet)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_7.isChecked():
                upper_latinAlphabet_and_specialSymbols = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV'
                                                              'WXYZABCDEFGHIJKLMNOPQRSTUVWXYZ!*_'
                                                              '123456789')
                for _ in range(number):
                    password += random.choice(upper_latinAlphabet_and_specialSymbols)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_8.isChecked():
                upper_rusAlphabet_and_specialSymbols = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕ'
                                                            'ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!*_'
                                                            '123456789')
                for _ in range(number):
                    password += random.choice(upper_rusAlphabet_and_specialSymbols)
                    self.lineEdit_2.setText(str(password))

            con = sqlite3.connect('LastPassword')
            cur = con.cursor()
            cur.execute(f"INSERT INTO LastPasswords (Password) VALUES ('{str(password)}')")
            con.commit()
            con.close()

        except Exception:
            self.label_4.setText('Можно вводить только цифры')

    def last_passwords(self):
        self.ex1 = LastPasswordsWindow()
        self.ex1.show()


class LastPasswordsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(LastPasswordsTemplate)
        uic.loadUi(f, self)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['Пароли'])
        con = sqlite3.connect('LastPassword')
        cur = con.cursor()
        passwords = cur.execute(f"SELECT * FROM LastPasswords").fetchall()[-30:-1]
        print(passwords)
        con.commit()
        for i, row in enumerate(passwords):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row[0]))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
