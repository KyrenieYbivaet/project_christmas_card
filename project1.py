import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QCursor
from PIL import Image, ImageFont, ImageDraw
import os
import smtplib
import mimetypes                                            # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email.mime.text import MIMEText                        # Текст/HTML
from email.mime.image import MIMEImage                      # Изображения
from email.mime.multipart import MIMEMultipart              # Многокомпонентный объект



correct = ['jpg', 'jpeg', 'png']
correct_2 = ['gmail.com', 'yandex.ru', 'mail.ru']


def attach_file(msg, filepath):  # Функция по добавлению конкретного файла к сообщению
    filename = os.path.basename(filepath)  # Получаем только имя файла
    ctype, encoding = mimetypes.guess_type(filepath)  # Определяем тип файла на основе его расширения
    maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
    with open(filepath, 'rb') as fp:
        file = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    file.add_header('Content-Disposition', 'attachment', filename=filename)  # Добавляем заголовки
    msg.attach(file)  # Присоединяем файл к сообщению

def send_email(rec, sender, password,  msg_text, file):
    addr_from = sender                         # Отправитель

    msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From']    = sender                             # Адресат
    msg['To']      = rec                               # Получатель
    msg['Subject'] = 'postcard'                              # Тема сообщения

    body = msg_text                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст

    attach_file(msg, file)
    if sender.split('@')[-1] == 'gmail.com':
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Создаем объект SMTP
        server.starttls()  # Начинаем шифрованный обмен по TLS
        server.login(addr_from, password)  # Получаем доступ
        server.send_message(msg)  # Отправляем сообщение
        server.quit()  # Выходим
    elif sender.split('@')[-1] == 'yandex.ru':
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP
        # server.starttls()                                  # Начинаем шифрованный обмен по TLS
        server.login(addr_from, password)  # Получаем доступ
        server.send_message(msg)  # Отправляем сообщение
        server.quit()  # Выходим
    elif sender.split('@')[-1] == 'mail.ru':
        server = smtplib.SMTP_SSL('smtp.mail.ru', 25)  # Создаем объект SMTP
        # server.starttls()                                  # Начинаем шифрованный обмен по TLS
        server.login(addr_from, password)  # Получаем доступ
        server.send_message(msg)  # Отправляем сообщение
        server.quit()  # Выходим


class Sender(QMainWindow):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        uic.loadUi('sender.ui', self)
        self.setWindowTitle('Postcards-helper')
        self.initui()

    def initui(self):
        self.label_rec.setText("Receiver's email")
        style = 'font-size: 30px; color: firebrick'
        self.label_rec.setStyleSheet(style)
        self.label_send.setText("Sender's email")
        self.label_send.setStyleSheet(style)
        self.label_congr.setText('Text of email')
        self.label_congr.setStyleSheet(style)
        self.label_pass.setText('Your password')
        self.label_pass.setStyleSheet(style)
        self.pushButton.setStyleSheet("QPushButton{background:#6B8E23;}")
        self.pushButton.clicked.connect(self.tap)
        cursor = QCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setCursor(cursor)

    def email_correctness(self, email):
        if '@' in email:
            if email.split('@')[-1] in correct_2:
                return True
            else:
                return False
        else:
            return False

    def tap(self):
        if self.email_correctness(self.line_rec.text()) and self.email_correctness(self.line_rec.text()):
            try:
                send_email(self.line_rec.text(), self.line_send.text(), self.line_pass.text(),
                           self.textEdit.toPlainText(), self.file_name)
                self.error_lab.setText('')
            except Exception:
                self.error_lab.setText('incorrect information')
        else:
            self.error_lab.setText('incorrect information')


class Askingemail(QMainWindow):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        uic.loadUi('email_ask.ui', self)
        self.setWindowTitle('Postcards-helper')
        self.initui()

    def initui(self):
        self.yes_Button.clicked.connect(self.yes_tap)
        self.no_Button.clicked.connect(self.no_tap)

    def yes_tap(self):
        self.dialog = Sender(self.file_name)
        self.dialog.show()
        self.close()

    def no_tap(self):
        self.close()


class Printer(QMainWindow):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        uic.loadUi('added_2.ui', self)
        self.setWindowTitle('Postcards-helper')
        self.initui()

    def initui(self):
        self.yes_Button.clicked.connect(self.yes_tap)
        self.no_Button.clicked.connect(self.no_tap)

    def yes_tap(self):
        os.startfile(self.file_name, "print")
        self.close()

    def no_tap(self):
        self.close()


class Showimg(QMainWindow):
    def __init__(self, file_name, pattern):
        super().__init__()
        uic.loadUi('added_3.ui', self)
        self.setWindowTitle('showing')
        if pattern == 'pattern_1.jpg':
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(800, 600)
            self.label = QLabel(self)
            self.label.setPixmap(pixmap)
            self.label.resize(pixmap.width(), pixmap.height())
        elif pattern == 'pattern_2.jpg':
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(600, 600)
            self.label = QLabel(self)
            self.label.setPixmap(pixmap)
            self.label.resize(600, 600)
        else:
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(700, 400)
            self.label = QLabel(self)
            self.label.setPixmap(pixmap)
            self.label.resize(pixmap.width(), pixmap.height())
        self.resize(pixmap.width(), pixmap.height())

def check_img_name(name):
    if '.' in name:
        if name.split('.')[-1] in correct:
            return True
        else:
            return False
    else:
        return False


class Second(QMainWindow):
    def __init__(self, pattern):
        super().__init__()
        self.pattern = pattern
        self.file_name = 'postcard.jpg'

        uic.loadUi('added.ui', self)
        self.setWindowTitle('Postcards-helper')
        self.initui()
        self.dialog = Printer(self.file_name)

    def initui(self):
        self.label_rec.setText("Receiver's name")
        style = 'font-size: 30px; color: firebrick'
        self.label_rec.setStyleSheet(style)
        self.label_send.setText("Sender's name")
        self.label_send.setStyleSheet(style)
        self.label_congr.setText('Your congratulations')
        self.label_congr.setStyleSheet(style)
        self.label_save.setText('Save as')
        self.label_save.setStyleSheet(style)
        self.pushButton_show.clicked.connect(self.sh)
        self.lineEdit.setMaxLength(20)
        self.lineEdit_2.setMaxLength(20)
        self.pushButton.setStyleSheet("QPushButton{background:#6B8E23;}")
        self.pushButton_show.setStyleSheet("QPushButton{background:#6B8E23;}")
        self.pushButton.clicked.connect(self.tap)

    def sh(self):
        self.ex = Showimg(self.file_name, self.pattern)
        self.ex.show()

    def tap(self):
        if len(self.lineEdit_3.text()) > 0:
            if check_img_name(self.lineEdit_3.text()):
                self.file_name = self.lineEdit_3.text()
            else:
                self.error_lab.setText('the file will be saved as "postcard.jpg"')
                self.file_name = 'postcard.jpg'
        else:
            self.error_lab.setText('the file will be saved as "postcard.jpg"')
            self.file_name = 'postcard.jpg'
        if len(self.lineEdit.text()) == 0 or len(self.lineEdit_2.text()) == 0\
                or len(self.textEdit.toPlainText()) == 0:
            self.error_lab.setText('please, fill in the fields')
        else:
            sender = self.lineEdit_2.text()
            reciever = self.lineEdit.text()
            text = self.textEdit.toPlainText()
            if self.pattern == 'pattern_1.jpg':
                flag = False
                for i in range(len(text.split('\n'))):
                    if len(text.split('\n')[i]) > 40:
                        a = str('your string {} should be {} symbols less'.
                                format(str(i + 1), str(len(text.split('\n')[i]) - 40)))
                        self.error_lab.setText(a)
                        flag = True
                        self.error_lab.setStyleSheet('color: firebrick')
                        break
                if len(text.split('\n')) > 5:
                    self.error_lab.setText(str('cut number of string by ' +
                                               str(len(text.split('\n')) - 5)))
                    self.error_lab.setStyleSheet('color: firebrick')
                    flag = True
                if flag:
                    pass
                else:
                    self.error_lab.setText('the file will be saved as ' + self.file_name)
                    text = self.textEdit.toPlainText()
                    img = Image.open(self.pattern)
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("bubbler.ttf", 100)
                    draw.text((350, 200), 'From: ' + sender, (0, 0, 135), font=font)
                    draw.text((350, 350), 'To: ' + reciever, (0, 0, 135), font=font)
                    draw.text((1000, 490), text, (0, 0, 135), font=font)
                    img.save(self.file_name)
                    self.dialog = Printer(self.file_name)
                    self.dialog.show()
                    self.dialog_2 = Askingemail(self.file_name)
                    self.dialog_2.show()
                    self.pushButton_show.move(530, 660)
            elif self.pattern == 'pattern_2.jpg':
                flag = False
                for i in range(len(text.split('\n'))):
                    if len(text.split('\n')[i]) > 23:
                        a = str('your string {} should be {} symbols less'.
                                format(str(i + 1), str(len(text.split('\n')[i]) - 23)))
                        self.error_lab.setText(a)
                        self.error_lab.setStyleSheet('color: firebrick')
                        flag = True
                        break
                if len(text.split('\n')) > 6:
                    self.error_lab.setText(str('cut number of string by ' +
                                               str(len(text.split('\n')) - 6)))
                    self.error_lab.setStyleSheet('color: firebrick')
                    flag = True
                if flag:
                    pass
                else:
                    self.error_lab.setText('the file will be saved as ' + self.file_name)
                    text = self.textEdit.toPlainText()
                    img = Image.open(self.pattern)
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("bubbler.ttf", 230)
                    draw.text((800, 800), 'From: ' + sender, (139, 0, 0), font=font)
                    draw.text((800, 1050), 'To: ' + reciever, (139, 0, 0), font=font)
                    draw.text((1000, 1350), text, (139, 0, 0), font=font)
                    img.save(self.file_name)
                    self.dialog = Printer(self.file_name)
                    self.dialog.show()
                    self.dialog_2 = Askingemail(self.file_name)
                    self.dialog_2.show()
                    self.pushButton_show.move(530, 660)
            elif self.pattern == 'pattern_3.jpg':
                flag = False
                for i in range(len(text.split('\n'))):
                    if len(text.split('\n')[i]) > 28:
                        a = str('your string {} should be {} symbols less'.
                                format(str(i + 1), str(len(text.split('\n')[i]) - 28)))
                        self.error_lab.setText(a)
                        self.error_lab.setStyleSheet('color: firebrick')
                        flag = True
                        break
                if len(text.split('\n')) > 5:
                    self.error_lab.setText(str('cut number of string by ' +
                                               str(len(text.split('\n')) - 5)))
                    self.error_lab.setStyleSheet('color: firebrick')
                    flag = True
                if flag:
                    pass
                else:
                    self.error_lab.setText('the file will be saved as ' + self.file_name)
                    text = self.textEdit.toPlainText()
                    img = Image.open(self.pattern)
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("bubbler.ttf", 32)
                    draw.text((70, 160), 'From: ' + sender, (0, 100, 0), font=font)
                    draw.text((70, 185), 'To: ' + reciever, (0, 100, 0), font=font)
                    draw.text((118, 215), text, (0, 100, 0), font=font)
                    img.save(self.file_name)
                    self.dialog = Printer(self.file_name)
                    self.dialog.show()
                    self.dialog_2 = Askingemail(self.file_name)
                    self.dialog_2.show()
                    self.pushButton_show.move(530, 660)


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main1.ui', self)
        pixmap = QPixmap('lights.png')
        self.dialog = None
        self.label_pic.setPixmap(pixmap)
        self.pattern = ''
        self.initui()

    def error_occur(self): #printing error
        self.label_task.setStyleSheet('border-style: solid; border-width: 1px; border-color: firebrick;')
        self.error_label.setText('error->')
        style = 'font-size: 30px; color: firebrick'
        self.error_label.setStyleSheet(style)

    def clear_window(self):
        self.label_blue_ball.resize(0, 0)
        self.label_green_ball.resize(0, 0)
        self.label_red_ball.resize(0, 0)
        self.label_name.resize(0, 0)
        self.error_label.resize(0, 0)
        self.desButton.resize(0, 0)
        self.des2Button.resize(0, 0)
        self.des3Button.resize(0, 0)
        self.label_task.resize(0, 0)
        self.label_pic.resize(0, 0)
        self.label_pattern1.resize(0, 0)
        self.label_pattern2.resize(0, 0)
        self.label_pattern3.resize(0, 0)
        self.pushButton.resize(0, 0)

    def initui(self):
        self.setWindowTitle('Postcards-helper')
        pixmap_2 = QPixmap('pattern_1.jpg')
        pixmap_2pro = pixmap_2.scaled(300, 270)
        self.label_pattern1.setPixmap(pixmap_2pro)
        pixmap_3 = QPixmap('pattern_2.jpg')
        pixmap_3pro = pixmap_3.scaled(300, 270)
        self.label_pattern2.setPixmap(pixmap_3pro)
        pixmap_4 = QPixmap('pattern_3.jpg')
        pixmap_4pro = pixmap_4.scaled(300, 270)
        self.label_pattern3.setPixmap(pixmap_4pro)

        pixmap_ball_1 = QPixmap('ball-blue.png')
        pixmap_ball_1pro = pixmap_ball_1.scaled(71, 71)
        self.label_blue_ball.setPixmap(pixmap_ball_1pro)
        pixmap_ball_2 = QPixmap('ball-red.png')
        pixmap_ball_2pro = pixmap_ball_2.scaled(71, 71)
        self.label_red_ball.setPixmap(pixmap_ball_2pro)
        pixmap_ball_3 = QPixmap('ball-green.png')
        pixmap_ball_3pro = pixmap_ball_3.scaled(71, 71)
        self.label_green_ball.setPixmap(pixmap_ball_3pro)

        self.pushButton.setStyleSheet("QPushButton{background:#6B8E23;}")
        cursor = QCursor(QtCore.Qt.PointingHandCursor)
        self.pushButton.setCursor(cursor)
        self.desButton.setCursor(cursor)
        self.des2Button.setCursor(cursor)
        self.des3Button.setCursor(cursor)
        self.pushButton.clicked.connect(self.tap)

    def tap(self):
        if not self.desButton.isChecked() and not self.des2Button.isChecked() and not self.des3Button.isChecked():
            self.error_occur() #if no button pressed
        else:
            if self.desButton.isChecked():
                self.pattern = 'pattern_1.jpg'
            elif self.des2Button.isChecked():
                self.pattern = 'pattern_2.jpg'
            else:
                self.pattern = 'pattern_3.jpg'
            self.clear_window()
            self.close()
            self.dialog = Second(self.pattern)
            self.dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())