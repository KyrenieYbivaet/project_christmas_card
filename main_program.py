from program import Ui_Christmas_card_maker
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


class main_pr:
    def main_f(self):
        greeting_text = self.greeting_text.toPlainText()
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

                    if self.x_sender.value() == '-1' and self.y_sender.value() == '-1':
                        self.add_sender(1600, 900, color, font_sender, draw)

                    elif self.x_sender.value() != '-1' and self.y_sender.value() != '-1':
                        self.add_sender(int(self.x_sender.value()), int(self.y_sender.value()), color, font_sender, draw)

                    elif self.x_sender.value() != '-1':
                        self.add_sender(int(self.x_sender.value()), 900, color, font_sender, draw)

                    elif self.y_sender.value() != '-1':
                        self.add_sender(1600, int(self.y_sender.value()), color, font_sender, draw)

                    if self.x_recipient.value() == '-1' and self.y_recipient.value() == '-1':
                        self.add_recipient(1600, 800, color, font_recipient, draw)

                    elif self.x_recipient.value() != '-1' and self.y_recipient.value() != '-1':
                        self.add_sender(int(self.x_recipient.value()), int(self.y_recipient.value()), color, font_sender, draw)

                    elif self.x_recipient.value() != '-1':
                        self.add_sender(int(self.x_recipient.value()), 900, color, font_sender, draw)

                    elif self.y_recipient.value() != '-1':
                        self.add_sender(1600, int(self.y_recipient.value()), color, font_sender, draw)

                    if self.x_greeting.value() == '-1' and self.y_greeting.value() == '-1':
                        self.add_greeting(600, 200, color, font_greeting, draw)

                    elif self.x_greeting.value() != '-1' and self.y_greeting.value() != '-1':
                        self.add_sender(int(self.x_greeting.value()), int(self.y_greeting.value()), color, font_sender, draw)

                    elif self.x_greeting.value() != '-1':
                        self.add_sender(int(self.x_greeting.value()), 900, color, font_sender, draw)

                    elif self.y_greeting.value() != '-1':
                        self.add_sender(1600, int(self.y_greeting.value()), color, font_sender, draw)
                    print('flex')
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

                    if self.x_sender.value() == '-1' and self.y_sender.value() == '-1':
                        self.add_sender(350, 365, color, font_sender, draw)

                    elif self.x_sender.value() != '-1' and self.y_sender.value() != '-1':
                        self.add_sender(int(self.x_sender.value()), int(self.y_sender.value()), color, font_sender, draw)

                    elif self.x_sender.value() != '-1':
                        self.add_sender(int(self.x_sender.value()), 365, color, font_sender, draw)

                    elif self.y_sender.value() != '-1':
                        self.add_sender(350, int(self.y_sender.value()), color, font_sender, draw)

                    if self.x_recipient.value() == '-1' and self.y_recipient.value() == '-1':
                        self.add_recipient(0, 0, color, font_recipient, draw)

                    elif self.x_recipient.value() != '-1' and self.y_recipient.value() != '-1':
                        self.add_sender(int(self.x_recipient.value()), int(self.y_recipient.value()), color, font_sender, draw)

                    elif self.x_recipient.value() != '-1':
                        self.add_sender(int(self.x_recipient.value()), 0, color, font_sender, draw)

                    elif self.y_recipient.value() != '-1':
                        self.add_sender(0, int(self.y_recipient.value()), color, font_sender, draw)

                    if self.x_greeting.value() == '-1' and self.y_greeting.value() == '-1':
                        self.add_greeting(150, 265, color, font_greeting, draw)

                    elif self.x_greeting.value() != '-1' and self.y_greeting.value() != '-1':
                        self.add_sender(int(self.x_greeting.value()), int(self.y_greeting.value()), color, font_sender, draw)

                    elif self.x_greeting.value() != '-1':
                        self.add_sender(int(self.x_greeting.value()), 265, color, font_sender, draw)

                    elif self.y_greeting.value() != '-1':
                        self.add_sender(150, int(self.y_greeting.value()), color, font_sender, draw)

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

                    if self.x_sender.value() == '-1' and self.y_sender.value() == '-1':
                        self.add_sender(650, 950, color, font_sender, draw)

                    elif self.x_sender.value() != '-1' and self.y_sender.value() != '-1':
                        self.add_sender(int(self.x_sender.value()), int(self.y_sender.value()), color, font_sender, draw)

                    elif self.x_sender.value() != '-1':
                        self.add_sender(int(self.x_sender.value()), 950, color, font_sender, draw)

                    elif self.y_sender.value() != '-1':
                        self.add_sender(650, int(self.y_sender.value()), color, font_sender, draw)

                    if self.x_recipient.value() == '-1' and self.y_recipient.value() == '-1':
                        self.add_recipient(0, 0, color, font_recipient, draw)

                    elif self.x_recipient.value() != '-1' and self.y_recipient.value() != '-1':
                        self.add_sender(int(self.x_recipient.value()), int(self.y_recipient.value()), color, font_sender, draw)

                    elif self.x_recipient.value() != '-1':
                        self.add_sender(int(self.x_recipient.value()), 0, color, font_sender, draw)

                    elif self.y_recipient.value() != '-1':
                        self.add_sender(0, int(self.y_recipient.value()), color, font_sender, draw)

                    if self.x_greeting.value() == '-1' and self.y_greeting.value() == '-1':
                        self.add_greeting(150, 265, color, font_greeting, draw)

                    elif self.x_greeting.value() != '-1' and self.y_greeting.value() != '-1':
                        self.add_sender(int(self.x_greeting.value()), int(self.y_greeting.value()), color, font_sender, draw)

                    elif self.x_greeting.value() != '-1':
                        self.add_sender(int(self.x_greeting.value()), 265, color, font_sender, draw)

                    elif self.y_greeting.value() != '-1':
                        self.add_sender(150, int(self.y_greeting.value()), color, font_sender, draw)

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


main_pr()

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