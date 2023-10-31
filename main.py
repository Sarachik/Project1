import random
import sys
import io
import datetime
import sqlite3

from res_rc import *
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

PasswordGenerator = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>920</width>
    <height>697</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: white;
</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>-160</x>
      <y>-90</y>
      <width>1261</width>
      <height>791</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image: url(:/pictures/2023-10-29_22-58-59.png);
</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>1</number>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>100</y>
      <width>501</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLineEdit {
font-size: 18px;
background-color: black;
border-color: 14px;
border: 2px solid black;
color: black;
background-color: rgba(255, 255, 255, 0.9);
border-radius: 5px;
}</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="readOnly">
     <bool>true</bool>
    </property>
    <property name="placeholderText">
     <string>Здесь будет сгенерированный пароль</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>350</y>
      <width>499</width>
      <height>51</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
font-size: 15px;
border-radius: 5px;
border: 3px solid black;
font-weight: bold;
color: black;
background-color: rgba(255, 255, 255, 0.7);
}

QPushButton:hover {
background-color: rgba(255, 255, 255, 0.9);
}



</string>
    </property>
    <property name="text">
     <string>Сгенерировать пароль</string>
    </property>
    <property name="checkable">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_8">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>330</y>
      <width>499</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;
background-color: rgba(255, 255, 255, 0.7);
font-size: 14px;
border-color: 14px;
border-radius: 5px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Кириллица + Заглавные буквы + спец-символы</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_7">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>310</y>
      <width>499</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;
background-color: rgba(255, 255, 255, 0.7);
font-size: 14px;
border-color: 14px;
border-radius: 5px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Латиница + Заглавные буквы + спец-символы</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_6">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>290</y>
      <width>499</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;
background-color: rgba(255, 255, 255, 0.7);
font-size: 14px;
border-color: 14px;
border-radius: 5px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Кириллица + Заглавные буквы</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_5">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>270</y>
      <width>499</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;
background-color: rgba(255, 255, 255, 0.7);
font-size: 14px;
border-color: 14px;
border-radius: 5px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Латиница + Заглавные буквы</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_4">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>250</y>
      <width>499</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;
background-color: rgba(255, 255, 255, 0.7);
font-size: 14px;
border-color: 14px;
border-radius: 5px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Кириллица + спец символы (а-я + !&quot;%)</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_3">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>230</y>
      <width>499</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;
background-color: rgba(255, 255, 255, 0.7);
font-size: 14px;
border-color: 14px;
border-radius: 5px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Латиница + спец-символы (а-я + !&quot;%)</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton_2">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>210</y>
      <width>499</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color: black;
background-color: rgba(255, 255, 255, 0.7);
font-size: 14px;
border-radius: 5px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Только Кириллица (а-я)</string>
    </property>
   </widget>
   <widget class="QRadioButton" name="radioButton">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>190</y>
      <width>499</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-weight: bold;
color: black;
background-color: black;
font-size: 14px;
border-color: 14px;
border-radius: 14px;
background-color: rgba(255, 255, 255, 0.7);
border-radius: 5px;


</string>
    </property>
    <property name="text">
     <string>Только Латиница (a-z)</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>152</y>
      <width>231</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLineEdit {
font-size: 15px;
border-color: 14px;
border: 2px solid black;
color: black;
background-color: rgba(255, 255, 255, 0.7);
border-radius: 5px;
}

QLineEdit:hover {
background-color: rgba(255, 255, 255, 0.9);
transition: 0.7s;
}</string>
    </property>
    <property name="maxLength">
     <number>2</number>
    </property>
    <property name="placeholderText">
     <string>Введите количество символов:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>60</y>
      <width>491</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
color: red;
background-color: rgba(255, 255, 255, 0);
font-size: 25px;
color: red;
}
</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>770</x>
      <y>640</y>
      <width>141</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size: 14px;
background-color: black;
border-color: 14px;
border: 2px solid black;
color: black;
background-color: rgba(255, 255, 255, 0.8);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>770</x>
      <y>670</y>
      <width>141</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size: 14px;
background-color: black;
border-color: 14px;
border: 2px solid black;
color: black;
background-color: rgba(255, 255, 255, 0.8);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>620</y>
      <width>231</width>
      <height>71</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
font-size: 15px;
border-radius: 5px;
border: 3px solid black;
font-weight: bold;
color: black;
background-color: rgba(255, 255, 255, 0.7);
}

QPushButton:hover {
background-color: rgba(255, 255, 255, 0.9);
}</string>
    </property>
    <property name="text">
     <string>Открыть последние пароли</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>
'''
LastPasswordsTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>405</width>
    <height>286</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QTableWidget" name="tableWidget">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>11</y>
     <width>181</width>
     <height>271</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>250</x>
     <y>130</y>
     <width>101</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Сохранить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton_2">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>250</y>
     <width>131</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string>Открыть сохранённые</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(PasswordGenerator)
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
                lower_latinAlphabet = list('abcdefghijklmnopqrstuvwxyz')
                for _ in range(number):
                    password += random.choice(lower_latinAlphabet)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_2.isChecked():
                lower_rusAlphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
                for _ in range(number):
                    password += random.choice(lower_rusAlphabet)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_3.isChecked():
                lower_latinAlphabet_and_specialSymbols = list('abcdefghijklmnopqrstuvwxyz!"№;%:?*_-')
                for _ in range(number):
                    password += random.choice(lower_latinAlphabet_and_specialSymbols)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_4.isChecked():
                lower_rusAlphabet_and_specialSymbols = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя!"№;%:?*_-')
                for _ in range(number):
                    password += random.choice(lower_rusAlphabet_and_specialSymbols)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_5.isChecked():
                upper_latinAlphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                for _ in range(number):
                    password += random.choice(upper_latinAlphabet)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_6.isChecked():
                upper_rusAlphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
                for _ in range(number):
                    password += random.choice(upper_rusAlphabet)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_7.isChecked():
                upper_latinAlphabet_and_specialSymbols = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV'
                                                              'WXYZABCDEFGHIJKLMNOPQRSTUVWXYZ!"№;%:?*_-')
                for _ in range(number):
                    password += random.choice(upper_latinAlphabet_and_specialSymbols)
                    self.lineEdit_2.setText(str(password))

            if self.radioButton_8.isChecked():
                upper_rusAlphabet_and_specialSymbols = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕ'
                                                            'ЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!"№;%:?*_-')
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
        passwords = cur.execute(f"SELECT * FROM LastPasswords").fetchall()[-11:-1]
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
