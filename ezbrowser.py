# GUI 
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import (Qt, pyqtSignal, QThread, pyqtSlot, QCoreApplication)
from browser import *

import sys

class Main(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.btn_search.clicked.connect(self.url_load)

    def url_load(self):
        url = ""
        url = self.txt_url.text()
        self.browser.setSource(QtCore.QUrl(url))
        
app = QtWidgets.QApplication([])
application = Main()
application.show()
sys.exit(app.exec())