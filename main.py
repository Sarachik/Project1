import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog

template = """
<?xml version="1.0" encoding="UTF-8"?>
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
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>291</width>
      <height>231</height>
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
      <widget class="QLineEdit" name="lineEdit">
       <property name="styleSheet">
        <string notr="true">background-color: none;
border-color: 14px;
border: 2px solid black;</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QCheckBox" name="checkBox">
       <property name="styleSheet">
        <string notr="true">font-size: 12px;
font-weight: bold;</string>
       </property>
       <property name="text">
        <string>Только Латиница (a-z)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QCheckBox" name="checkBox_2">
       <property name="styleSheet">
        <string notr="true">font-size: 12px;
font-weight: bold;</string>
       </property>
       <property name="text">
        <string>Только Кириллица (а-я)</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QCheckBox" name="checkBox_3">
       <property name="styleSheet">
        <string notr="true">font-size: 12px;
font-weight: bold;</string>
       </property>
       <property name="text">
        <string>Содержание Cпец-символов</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QCheckBox" name="checkBox_4">
       <property name="styleSheet">
        <string notr="true">font-size: 12px;
font-weight: bold;</string>
       </property>
       <property name="text">
        <string>Заглавные буквы</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="styleSheet">
        <string notr="true">font-size: 15px;
border-radius: 5px;
border: 3px solid black;
font-weight: bold;
background-color: white;</string>
       </property>
       <property name="text">
        <string>Сгенерировать пароль</string>
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
"""


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    ex.show()
    sys.exit(app.exec_())
