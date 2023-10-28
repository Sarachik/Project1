import random
import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>575</width>
    <height>634</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: white;</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>0</y>
      <width>501</width>
      <height>391</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout_12">
     <item>
      <widget class="QLabel" name="label">
       <property name="styleSheet">
        <string notr="true">font-size: 20px;
background-color: white;
border-radius: 20px;
color: black;
font-family: &quot;Georgia&quot;, serif;
line-height: 26px;
background: none;
font-weight: bold;
</string>
       </property>
       <property name="text">
        <string>PASSWORD GENERATOR</string>
       </property>
       <property name="margin">
        <number>10</number>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="styleSheet">
        <string notr="true">font-size: 15px;
background-color: white;
border-radius: 5px;
color: black;

</string>
       </property>
       <property name="text">
        <string>Количество символов</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="lineEdit">
       <property name="styleSheet">
        <string notr="true">font-size: 14px;
background-color: none;
border-color: 14px;
border: 2px solid black;</string>
       </property>
       <property name="maxLength">
        <number>2</number>
       </property>
       <property name="placeholderText">
        <string>Введите цифры</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton">
       <property name="text">
        <string>Только Латиница (a-z)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_2">
       <property name="text">
        <string>Только Кириллица (а-я)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_3">
       <property name="text">
        <string>Латиница + спец-символы (а-я + !&quot;%)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_4">
       <property name="text">
        <string>Кириллица + спец символы (а-я + !&quot;%)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_5">
       <property name="text">
        <string>Латиница + Заглавные буквы</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_6">
       <property name="text">
        <string>Кириллица + Заглавные буквы</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_7">
       <property name="text">
        <string>Латиница + Заглавыне буквы + спец-символы</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QRadioButton" name="radioButton_8">
       <property name="text">
        <string>Кириллица + Заглавные буквы + спец-символы</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="styleSheet">
        <string notr="true">QPushButton {
font-size: 15px;
border-radius: 5px;
border: 3px solid black;
font-weight: bold;
background-color: white;
}

QPushButton:hover {
background-color: rgba(red, 0,8);
color: red;
}</string>
       </property>
       <property name="text">
        <string>Сгенерировать пароль</string>
       </property>
       <property name="checkable">
        <bool>false</bool>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="styleSheet">
        <string notr="true">font-size: 20px;
background-color: white;
border-radius: 20px;
color: black;
font-family: &quot;Georgia&quot;, serif;
line-height: 26px;
background: none;
font-weight: bold;</string>
       </property>
       <property name="text">
        <string>Сгенерированный пароль</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="lineEdit_2">
       <property name="styleSheet">
        <string notr="true">font-size: 14px;
background-color: none;
border-color: 14px;
border: 2px solid black;</string>
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
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>575</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        try:
            number = int(self.lineEdit.text())
            password = ''
            self.label_4.setText('')
        except Exception:
            self.label_4.setText('Можно вводить только цифры')

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
            lower_latinAlphabet_and_specialSymbols = list('abcdefghijklmnopqrstuvwxyz!"№;%:?*()_-+=')
            for _ in range(number):
                password += random.choice(lower_latinAlphabet_and_specialSymbols)
                self.lineEdit_2.setText(str(password))

        if self.radioButton_4.isChecked():
            lower_rusAlphabet_and_specialSymbols = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя!"№;%:?*()_-+=')
            for _ in range(number):
                password += random.choice(lower_rusAlphabet_and_specialSymbols)
                self.lineEdit_2.setText(str(password))

        if self.radioButton_5.isChecked():
            upper_latinAlphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            for _ in range(number):
                password += random.choice(upper_latinAlphabet)
                self.lineEdit_2.setText(str(password))

        if self.radioButton_6.isChecked():
            upper_rusAlphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
            for _ in range(number):
                password += random.choice(upper_rusAlphabet)
                self.lineEdit_2.setText(str(password))

        if self.radioButton_7.isChecked():
            upper_latinAlphabet_and_specialSymbols = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ!"№;%:?*()_-+=')
            for _ in range(number):
                password += random.choice(upper_latinAlphabet_and_specialSymbols)
                self.lineEdit_2.setText(str(password))

        if self.radioButton_8.isChecked():
            upper_rusAlphabet_and_specialSymbols = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!"№;%:?*()_-+=')
            for _ in range(number):
                password += random.choice(upper_rusAlphabet_and_specialSymbols)
                self.lineEdit_2.setText(str(password))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
