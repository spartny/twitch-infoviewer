import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from resources.main_ui import Ui_MainWindow
import APIData as apd
import LocalDataFireFox as ff


class TwitchInfo(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_FetchAPI.clicked.connect(self.runAPI)
        self.pushButton_FF.clicked.connect(self.firefoxdata)
        self.pushButton_GC.clicked.connect(self.googlechromedata)

    @qtc.Slot()
    def runAPI(self):
        print("fetching API data...")
        items = [
            "User ID", "User Details", "Top 20 games",
            # "Game Details"
            "Global Emotes", "Top 20 Streams", "Top 20 Soundtrack Playlists",
            "Follower count", "User follows", "Followers", "Video Clip Details",
            "Channel information"
        ]
        self.listWidget.clear()
        self.listWidget.addItems(items)
        self.pushButton_ViewFile.clicked.connect(self.extractAPI)

    @qtc.Slot()
    def firefoxdata(self):
        print("fetching local firefox data...")
        items = ["Data", "Cache", "IDB"]
        self.listWidget.clear()
        self.listWidget.addItems(items)
        self.pushButton_ViewFile.clicked.connect(self.extractFF)

    @qtc.Slot()
    def googlechromedata(self):
        print("fetching local chrome data...")
        pass

    @qtc.Slot()
    def extractFF(self):
        choice = self.listWidget.currentItem().text()
        print(choice)
        content = ff.extraction(choice)
        self.textEdit.setText(content)

    @qtc.Slot()
    def extractAPI(self):
        choice = self.listWidget.currentItem().text()
        user = self.lineEdit_twitchUsername.text()
        print(choice)
        content = apd.extraction(choice, user)
        self.textEdit.setText(content)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = TwitchInfo()
    window.show()

    sys.exit(app.exec())
