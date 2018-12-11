from PIL import Image, ImageDraw, ImageFont
from shutil import copy
import os
import shutil





def adding_text():
    if True:                                                  # ЕСЛИ ВЫБРАН ПЕРВЫЙ ШАБЛОН
        text_recipient = 'flex'                                   # Добавить текст получателя, полученный из приложения  !!!
        text_sender = 'flex'                                      # Добавить текст отправителя, полученный из приложения !!!

        shutil.copy('pattern_1.jpg', 'Christmas_card.jpg')

        font = ImageFont.truetype("main_font.otf", 100)
        img = Image.open('Christmas_card.jpg')
        draw = ImageDraw.Draw(img)
        if len(text_recipient) != 0:
            draw.text((0, 0), text_recipient, (255, 255, 255), font=font)    # ВЫБРАТЬ МЕСТО ДЛЯ ПОЛУЧАТЕЛЯ
        if len(text_sender) != 0:
            draw.text((0, 0), text_sender, (255, 255, 255), font=font)       # ВЫБРАТЬ МЕСТО ДЛЯ ОТРАВИТЕЛЯ

        img.save("Christmas_card.jpg")


adding_text()
