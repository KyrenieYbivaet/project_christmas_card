# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Christmas_card_maker(object):
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
        self.first_pattern.setCheckable(True)
        self.first_pattern.setChecked(True)
        self.first_pattern.setObjectName("first_pattern")
        self.second_pattern = QtWidgets.QRadioButton(self.centralwidget)
        self.second_pattern.setGeometry(QtCore.QRect(320, 440, 31, 31))
        self.second_pattern.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.second_pattern.setObjectName("second_pattern")
        self.third_pattern = QtWidgets.QRadioButton(self.centralwidget)
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
        self.greeting_text.setPlaceholderText("")
        self.greeting_text.setObjectName("greeting_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(470, 270, 121, 21))
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
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(30, 310, 371, 21))
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
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(440, 0, 191, 21))
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
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setObjectName("label_3")
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
        self.label.setText(_translate("Christmas_card_maker", "Введите текст!!!"))
        self.label_2.setText(_translate("Christmas_card_maker", "Превышен лимит символов."))
        self.label_3.setText(_translate("Christmas_card_maker", "sucsessfully"))

