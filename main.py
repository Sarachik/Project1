import sys
import PyQt5

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
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>291</width>
      <height>101</height>
     </rect>
    </property>
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
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>80</y>
      <width>151</width>
      <height>20</height>
     </rect>
    </property>
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
   <widget class="QCheckBox" name="checkBox">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>140</y>
      <width>201</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size: 12px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Содержание Латиницы (a-z)</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="checkBox_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>170</y>
      <width>211</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size: 12px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Содержание Кириллицы (а-я)</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="checkBox_3">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>200</y>
      <width>201</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size: 12px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Содержание Cпец-символов</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>110</y>
      <width>151</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: none;
border-color: 14px;
border: 2px solid black;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>260</y>
      <width>241</width>
      <height>41</height>
     </rect>
    </property>
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
   <widget class="QCheckBox" name="checkBox_4">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>230</y>
      <width>191</width>
      <height>17</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size: 12px;
font-weight: bold;</string>
    </property>
    <property name="text">
     <string>Заглавные буквы</string>
    </property>
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