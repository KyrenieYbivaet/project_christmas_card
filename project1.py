import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main1.ui', self)
        pixmap = QPixmap('lights.png')
        self.label.setPixmap(pixmap)
        self.initUI()

    def initUI(self):
        label_p = QLabel(self)





app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
