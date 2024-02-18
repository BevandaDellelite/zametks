from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import json
import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_none)


    if os.path.exists("tarassasok.json") and os.path.getsize("tarassasok.json"):
        with open("tarassasok.json", "r") as file:
            self.notes = json.load(file)
            self.ui.listWidget.addItems(self.notes.keys())


    def add_none(self): 
        text, ok = QInputDialog.getText(self,"Додати замітку","введіть текст")
        if ok:
            self.ui.listWidget.addItem(text)

app = QApplication([])

ex = Widget()
ex.show()
app.exec_()