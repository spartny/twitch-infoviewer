import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from core.resources.main_ui import Ui_MainWindow
import APIData as apd


class TwitchInfo(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_FetchAPI.clicked.connect(self.runAPI)
        self.pushButton_FF.clicked.connect(self.firefoxdata)
        self.pushButton_GC.clicked.connect(self.googlechromedata)

    @qtc.Slot()
    def runAPI(self):
        print("fetching userid...")
        user = self.lineEdit_twitchUsername
        print(str(user))
        apd.getid(str(user))

    @qtc.Slot()
    def firefoxdata(self):
        print("fetching local firefox data...")
        pass

    @qtc.Slot()
    def googlechromedata(self):
        print("fetching local chrome data...")
        pass



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = TwitchInfo()
    window.show()

    sys.exit(app.exec())
