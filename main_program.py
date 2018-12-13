# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageFont
from shutil import copy
import os

class Ui_Christmas_card_maker(object):
    def setupUi(self, Christmas_card_maker):
        Christmas_card_maker.setObjectName("Christmas_card_maker")
        Christmas_card_maker.resize(640, 575)
        self.centralwidget = QtWidgets.QWidget(Christmas_card_maker)
        self.centralwidget.setObjectName("centralwidget")

        self.useless = QtWidgets.QLabel(self.centralwidget)
        self.useless.setGeometry(QtCore.QRect(10, 10, 251, 51))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)

        self.useless.setFont(font)
        self.useless.setObjectName("useless")

        self.useless_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.useless_label_3.setGeometry(QtCore.QRect(270, 60, 171, 41))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)

        self.useless_label_3.setFont(font)
        self.useless_label_3.setObjectName("useless_label_3")

        self.useless_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.useless_label_2.setGeometry(QtCore.QRect(270, 110, 111, 41))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)

        self.useless_label_2.setFont(font)
        self.useless_label_2.setObjectName("useless_label_2")

        self.first_pattern = QtWidgets.QRadioButton(self.centralwidget)
        self.first_pattern.setGeometry(QtCore.QRect(120, 440, 31, 31))
        self.first_pattern.setObjectName("first_pattern")

        self.second_pattern = QtWidgets.QRadioButton(self.centralwidget)
        self.second_pattern.setGeometry(QtCore.QRect(320, 440, 31, 31))
        self.second_pattern.setObjectName("second_pattern")

        self.third_pattern = QtWidgets.QRadioButton(self.centralwidget)
        self.third_pattern.setGeometry(QtCore.QRect(520, 440, 31, 31))
        self.third_pattern.setObjectName("third_pattern")

        self.useless_3 = QtWidgets.QLabel(self.centralwidget)
        self.useless_3.setGeometry(QtCore.QRect(490, 170, 71, 71))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)

        self.useless_3.setFont(font)
        self.useless_3.setObjectName("useless_3")

        self.useless_label = QtWidgets.QLabel(self.centralwidget)
        self.useless_label.setGeometry(QtCore.QRect(440, 210, 191, 71))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)

        self.useless_label.setFont(font)
        self.useless_label.setObjectName("useless_label")

        self.useless_2 = QtWidgets.QLabel(self.centralwidget)
        self.useless_2.setGeometry(QtCore.QRect(0, 510, 341, 21))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)

        self.useless_2.setFont(font)
        self.useless_2.setObjectName("useless_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 480, 191, 41))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.text_sender = QtWidgets.QTextEdit(self.centralwidget)
        self.text_sender.setGeometry(QtCore.QRect(30, 70, 211, 31))
        self.text_sender.setObjectName("text_sender")

        self.text_recipient = QtWidgets.QTextEdit(self.centralwidget)
        self.text_recipient.setGeometry(QtCore.QRect(30, 120, 211, 31))
        self.text_recipient.setObjectName("text_recipient")

        self.greeting_text = QtWidgets.QTextEdit(self.centralwidget)
        self.greeting_text.setGeometry(QtCore.QRect(30, 170, 371, 131))
        self.greeting_text.setObjectName("greeting_text")

        Christmas_card_maker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Christmas_card_maker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")

        Christmas_card_maker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Christmas_card_maker)
        self.statusbar.setObjectName("statusbar")
        Christmas_card_maker.setStatusBar(self.statusbar)

        self.retranslateUi(Christmas_card_maker)
        QtCore.QMetaObject.connectSlotsByName(Christmas_card_maker)

    def add_sender(self, pos_x, pos_y, color, font, draw):
        if len(self.text_sender) != 0:
            draw.text((pos_x, pos_y), self.text_recipient, color, font=font)  # ВЫБРАТЬ МЕСТО ДЛЯ ПОЛУЧАТЕЛЯ

    def add_recipient(self, pos_x, pos_y, color, font, draw):
        if len(self.text_recipient) != 0:
            draw.text((pos_x, pos_y), self.text_sender, color, font=font)  # ВЫБРАТЬ МЕСТО ДЛЯ ОТРАВИТЕЛЯ

    def add_greeting(self, pos_x, pos_y, color, font, draw):
        if len(self.greeting_text):
            draw.text((pos_x, pos_y), self.text_sender, color, font=font)  # ВЫБРАТЬ МЕСТО ДЛЯ ПОЗДРАВЛЕНИЯ

    def first_pattern(self):
        copy('pattern_1.jpg', 'Christmas_card.jpg')
        font = ImageFont.truetype("main_font.otf", 100)
        img = Image.open('Christmas_card.jpg')
        draw = ImageDraw.Draw(img)

    def flag_first(self):
        self.first_pattern_flag = True

    def error_no_greeting(self):
        pass

    def main(self):
        if len(self.greeting_text) == 0:
            error_no_greeting()

    self.pushButton.clicked.connect(main)
    self.first_pattern.clicked.connect(flag_first)

    def retranslateUi(self, Christmas_card_maker):
        _translate = QtCore.QCoreApplication.translate
        Christmas_card_maker.setWindowTitle(_translate("Christmas_card_maker", "MainWindow"))
        self.useless.setText(_translate("Christmas_card_maker", "Введите данные:"))
        self.useless_label_3.setText(_translate("Christmas_card_maker", "- отправитель"))
        self.useless_label_2.setText(_translate("Christmas_card_maker", "- адресат"))
        self.first_pattern.setText(_translate("Christmas_card_maker", "1"))
        self.second_pattern.setText(_translate("Christmas_card_maker", "2"))
        self.third_pattern.setText(_translate("Christmas_card_maker", "3"))
        self.useless_3.setText(_translate("Christmas_card_maker", "текст "))
        self.useless_label.setText(_translate("Christmas_card_maker", "поздравления *"))
        self.useless_2.setText(_translate("Christmas_card_maker", "* звездочкой помеченны поля, обязательные к заполнению"))
        self.pushButton.setText(_translate("Christmas_card_maker", "СГЕНЕРИРОВАТЬ!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Christmas_card_maker = QtWidgets.QMainWindow()
    ui = Ui_Christmas_card_maker()
    ui.setupUi(Christmas_card_maker)
    Christmas_card_maker.show()
    sys.exit(app.exec_())
