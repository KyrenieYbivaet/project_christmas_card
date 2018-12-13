# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageFont
from shutil import copy
import sys

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


class Ui_Christmas_card_maker(object):
    def main_f(self):
        greeting_text = self.greeting_text.toPlainText()
        print(greeting_text)
        if len(greeting_text) == 0:
            self.error.setEnabled(True)
            self.success.setEnabled(False)
        else:
            self.error_length.setEnabled(False)
            self.error.setEnabled(False)
            if self.first_pattern.isChecked():
                if len(greeting_text) > 50:
                    self.error_length.setEnabled(True)
                    self.success.setEnabled(False)
                else:
                    copy('pattern_1.jpg', 'Christmas_card.jpg')
                    font_greeting = ImageFont.truetype('main_font.otf', 100)
                    font_sender = ImageFont.truetype('main_font.otf', 75)
                    font_recipient = ImageFont.truetype('main_font.otf', 75)
                    img = Image.open('Christmas_card.jpg')
                    draw = ImageDraw.Draw(img)
                    color = (112, 146, 190)
                    self.add_sender(1600, 900, color, font_sender, draw)
                    self.add_recipient(1600, 800, color, font_recipient, draw)
                    self.add_greeting(600, 200, color, font_greeting, draw)
                    img.save("Christmas_card.jpg")
                    self.success.setEnabled(True)

            elif self.second_pattern.isChecked():
                if len(greeting_text) > 50:
                    self.error_length.setEnabled(True)
                    self.success.setEnabled(False)
                else:
                    copy('pattern_2.jpg', 'Christmas_card.jpg')
                    font_greeting = ImageFont.truetype('main_font.otf', 32)
                    font_sender = ImageFont.truetype('main_font.otf', 26)
                    font_recipient = ImageFont.truetype('main_font.otf', 20)
                    img = Image.open('Christmas_card.jpg')
                    draw = ImageDraw.Draw(img)
                    color = (237, 28, 36)
                    self.add_sender(350, 365, color, font_sender, draw)
                    self.add_recipient(0, 0, color, font_recipient, draw)
                    self.add_greeting(150, 265, color, font_greeting, draw)
                    img.save("Christmas_card.jpg")
                    self.success.setEnabled(True)

            elif self.third_pattern.isChecked():
                if len(greeting_text) > 50:
                    self.error_length.setEnabled(True)
                    self.success.setEnabled(False)
                else:
                    copy('pattern_3.jpg', 'Christmas_card.jpg')
                    font_greeting = ImageFont.truetype('main_font.otf', 120)
                    font_sender = ImageFont.truetype('main_font.otf', 75)
                    font_recipient = ImageFont.truetype('main_font.otf', 50)
                    img = Image.open('Christmas_card.jpg')
                    draw = ImageDraw.Draw(img)
                    color = (255, 255, 255)
                    self.add_sender(650, 950, color, font_sender, draw)
                    self.add_recipient(0, 0, color, font_recipient, draw)
                    self.add_greeting(150, 265, color, font_greeting, draw)
                    img.save("Christmas_card.jpg")
                    self.success.setEnabled(True)

    def add_sender(self, pos_x, pos_y, color, font, draw):
        text_sender = self.text_sender.toPlainText()
        if len(text_sender) != 0:
            draw.text((pos_x, pos_y), text_sender, color, font=font)  # ВЫБРАТЬ МЕСТО ДЛЯ ПОЛУЧАТЕЛЯ

    def add_recipient(self, pos_x, pos_y, color, font, draw):
        text_recipient = self.text_recipient.toPlainText()
        if len(text_recipient) != 0:
            draw.text((pos_x, pos_y), text_recipient, color, font=font)  # ВЫБРАТЬ МЕСТО ДЛЯ ОТРАВИТЕЛЯ

    def add_greeting(self, pos_x, pos_y, color, font, draw):
        greeting_text = self.greeting_text.toPlainText()
        draw.text((pos_x, pos_y), greeting_text, color, font=font)  # ВЫБРАТЬ МЕСТО ДЛЯ ПОЗДРАВЛЕНИЯ

    def first_pattern(self):
        copy('pattern_1.jpg', 'Christmas_card.jpg')
        img = Image.open('Christmas_card.jpg')
        draw = ImageDraw.Draw(img)

    def setupUi(self, Christmas_card_maker):
        Christmas_card_maker.setObjectName("Christmas_card_maker")
        Christmas_card_maker.resize(640, 575)
        Christmas_card_maker.setMouseTracking(False)
        Christmas_card_maker.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.first_pattern.setEnabled(True)
        self.first_pattern.setGeometry(QtCore.QRect(120, 440, 31, 31))
        self.first_pattern.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.first_pattern.setObjectName("first_pattern")

        self.second_pattern = QtWidgets.QRadioButton(self.centralwidget)
        self.second_pattern.setEnabled(True)
        self.second_pattern.setGeometry(QtCore.QRect(320, 440, 31, 31))
        self.second_pattern.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.second_pattern.setObjectName("second_pattern")

        self.third_pattern = QtWidgets.QRadioButton(self.centralwidget)
        self.third_pattern.setEnabled(True)
        self.third_pattern.setGeometry(QtCore.QRect(520, 440, 31, 31))
        self.third_pattern.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.useless_2.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.useless_2.setObjectName("useless_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 480, 191, 41))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.text_sender = QtWidgets.QTextEdit(self.centralwidget)
        self.text_sender.setGeometry(QtCore.QRect(30, 70, 211, 31))
        self.text_sender.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.text_sender.setObjectName("text_sender")

        self.text_recipient = QtWidgets.QTextEdit(self.centralwidget)
        self.text_recipient.setGeometry(QtCore.QRect(30, 120, 211, 31))
        self.text_recipient.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.text_recipient.setObjectName("text_recipient")

        self.greeting_text = QtWidgets.QTextEdit(self.centralwidget)
        self.greeting_text.setGeometry(QtCore.QRect(30, 170, 371, 131))
        self.greeting_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.greeting_text.setObjectName("greeting_text")

        self.success = QtWidgets.QLabel(self.centralwidget)
        self.success.setEnabled(False)
        self.success.setGeometry(QtCore.QRect(440, 0, 191, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.success.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.success.setFont(font)
        self.success.setMouseTracking(False)
        self.success.setObjectName("success")

        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setEnabled(False)
        self.error.setGeometry(QtCore.QRect(470, 270, 121, 21))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.error.setPalette(palette)

        self.error_length = QtWidgets.QLabel(self.centralwidget)
        self.error_length.setEnabled(False)
        self.error_length.setGeometry(QtCore.QRect(30, 310, 371, 21))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.error_length.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.error_length.setFont(font)
        self.error_length.setMouseTracking(False)
        self.error_length.setObjectName("error_length")

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error.setFont(font)
        self.error.setMouseTracking(False)
        self.error.setObjectName("error")

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

        self.pushButton.clicked.connect(self.main_f)

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
        self.useless_2.setText(
            _translate("Christmas_card_maker", "* звездочкой помеченны поля, обязательные к заполнению"))
        self.pushButton.setText(_translate("Christmas_card_maker", "СГЕНЕРИРОВАТЬ!"))
        self.error.setText(_translate("Christmas_card_maker", "Введите текст!!!"))
        self.error_length.setText(_translate("Christmas_card_maker", "Превышен лимит символов."))
        self.success.setText(_translate("Christmas_card_maker", "sucsessfully :)"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Christmas_card_maker = QtWidgets.QMainWindow()
    ui = Ui_Christmas_card_maker()
    ui.setupUi(Christmas_card_maker)
    Christmas_card_maker.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
