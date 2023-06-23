import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from resources.main_ui import Ui_MainWindow
import APIData as apd
import LocalDataFireFox as ff
import LocalDataChrome as gc
import generalAPI_data as gapd

from datetime import datetime


class TwitchInfo(qtw.QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_Message.setText("Message: Select Browser or API options")

        self.pushButton_FetchAPI.clicked.connect(self.runAPI)
        self.pushButton_FF.clicked.connect(self.firefoxdata)
        self.pushButton_GC.clicked.connect(self.googlechromedata)
        self.pushButton_GeneralAPI.clicked.connect(self.generalAPI)
        self.pushButton_ExportFile.clicked.connect(self.exportTE)

    @qtc.Slot()
    def runAPI(self):
        print("fetching API data...")
        self.label_Message.setText("Message: Fetching User API information...")
        items = [
            "User ID", "User Details",
            # "Game Details"
            "Follower count", "User follows", "Followers", "Video Clip Details",
            "Channel information", "Channel teams", "User chat color",
            "User chat settings",  # "User extensions",
        ]
        self.listWidget.clear()
        self.listWidget.addItems(items)
        self.label_Message.setText("Message: Select File from List to view or export all in the outputs folder")
        self.pushButton_ViewFile.clicked.connect(self.extractAPI)
        self.pushButton_ExportFiles.clicked.connect(self.exportAPI)

    @qtc.Slot()
    def firefoxdata(self):
        print("fetching local firefox data...")
        self.label_Message.setText("Message: Fetching local Mozilla Firefox data...")
        items = [
            "local storage - data", "local storage - database",
            "cache - caches", "cache - entries", "cache - request_headers",
            "cache - response_headers", "cache - response_url_lists",
            "cache - security_info", "cache - sqlite_sequence",
            "cache - storage", "idb - database", "idb - file", "idb - index_data",
            "idb - object_data", "idb - object_store", "idb - object_store_index",
        ]
        self.listWidget.clear()
        self.listWidget.addItems(items)
        self.label_Message.setText("Message: Select File from List to view or export all in the outputs folder")
        self.pushButton_ViewFile.clicked.connect(self.extractFF)
        self.pushButton_ExportFiles.clicked.connect(self.exportFF)

    @qtc.Slot()
    def googlechromedata(self):
        print("fetching local chrome data...")
        self.label_Message.setText("Message: Fetching local Google Chrome data...")

        items = ["Session Storage - twitch.tv", "Local Storage - twitch.tv", "Local Storage - gql.twitch.tv", "Local Storage - passport.twitch.tv"]
        self.listWidget.clear()
        self.listWidget.addItems(items)
        self.label_Message.setText("Message: Select File from List to view or export all in the outputs folder")
        self.pushButton_ViewFile.clicked.connect(self.extractGC)
        self.pushButton_ExportFiles.clicked.connect(self.exportGC)

    @qtc.Slot()
    def generalAPI(self):
        print("fetching general twitch API data...")
        self.label_Message.setText("Message: Fetching general API information...")

        items = ["Top 20 games", "Global Emotes", "Top 20 Streams",
                 "Top 20 Soundtrack Playlists", "Global Chat Badges",
                 "Global Cheermotes",
                 ]
        self.listWidget.clear()
        self.listWidget.addItems(items)
        self.label_Message.setText("Message: Select File from List to view or export all in the outputs folder")
        self.pushButton_ViewFile.clicked.connect(self.extractGAPI)
        self.pushButton_ExportFiles.clicked.connect(self.exportGAPI)

    @qtc.Slot()
    def extractFF(self):
        self.label_Message.setText("Message: Fetching data...")
        choice = self.listWidget.currentItem().text()
        print(choice)
        content = ff.extraction(choice)
        self.textEdit.clear()
        self.textEdit.setText(content)
        self.label_Message.setText("Message: Data displayed")

    @qtc.Slot()
    def extractGC(self):
        self.label_Message.setText("Message: Fetching data...")
        choice = self.listWidget.currentItem().text()
        print(choice)
        content = gc.extraction(choice)
        self.textEdit.clear()
        self.textEdit.setText(content)
        self.label_Message.setText("Message: Data displayed")

    @qtc.Slot()
    def extractAPI(self):
        self.label_Message.setText("Message: Fetching data...")
        choice = self.listWidget.currentItem().text()
        user = self.lineEdit_twitchUsername.text()
        print(choice)
        content = apd.extraction(choice, user)
        self.textEdit.clear()
        self.textEdit.setText(content)
        self.label_Message.setText("Message: Data displayed")

    @qtc.Slot()
    def extractGAPI(self):
        self.label_Message.setText("Message: Fetching data...")
        choice = self.listWidget.currentItem().text()
        user = self.lineEdit_twitchUsername.text()
        print(choice)
        content = gapd.extraction(choice, user)
        self.textEdit.clear()
        self.textEdit.setText(content)
        self.label_Message.setText("Message: Data displayed")

    @qtc.Slot()
    def exportTE(self):
        print("exporting textedit to file")
        self.label_Message.setText("Message: Exporting to .txt file in outputs folder")
        choice = self.listWidget.currentItem().text()
        data = self.textEdit.toPlainText()
        now = now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")

        with open('../outputs/' + choice + '_' + dt_string + '.txt', 'w') as f:
            f.write(data)
            f.flush()
            f.close()
            print("exported")
            self.label_Message.setText("Message: Export Complete! .txt file in the outputs folder")

    @qtc.Slot()
    def exportFF(self):
        print("exporting all items in listwidget to files")
        self.label_Message.setText("Message: Exporting all items to .txt file in outputs folder")
        items = [self.listWidget.item(x).text() for x in range(self.listWidget.count())]
        print(items)
        for i in items:
            user = self.lineEdit_twitchUsername.text()
            content = ff.extraction(i)
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
            with open('../outputs/' + i + '_' + dt_string + '.txt', 'w') as f:
                if content:
                    f.write(content)
                else:
                    f.write("empty record")
                f.flush()
                f.close()
        print("exported")
        self.label_Message.setText("Message: Export Complete! .txt files in the outputs folder")


    @qtc.Slot()
    def exportGC(self):
        print("exporting all items in listwidget to files")
        self.label_Message.setText("Message: Exporting all items to .txt file in outputs folder")
        items = [self.listWidget.item(x).text() for x in range(self.listWidget.count())]
        print(items)
        for i in items:
            user = self.lineEdit_twitchUsername.text()
            content = gc.extraction(i)
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
            with open('../outputs/' + i + '_' + dt_string + '.txt', 'w') as f:
                if content:
                    f.write(content)
                else:
                    f.write("empty record")
                f.flush()
                f.close()
        print("exported")
        self.label_Message.setText("Message: Export Complete! .txt files in the outputs folder")

    @qtc.Slot()
    def exportAPI(self):
        print("exporting all items in listwidget to files")
        self.label_Message.setText("Message: Exporting all items to .txt file in outputs folder")

        items = [self.listWidget.item(x).text() for x in range(self.listWidget.count())]
        print(items)
        for i in items:
            user = self.lineEdit_twitchUsername.text()
            content = apd.extraction(i, user)
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
            with open('../outputs/' + i + '_' + dt_string + '.txt', 'w') as f:
                if content:
                    f.write(content)
                else:
                    f.write("empty record")
                f.flush()
                f.close()
        print("exported")
        self.label_Message.setText("Message: Export Complete! .txt files in the outputs folder")

    @qtc.Slot()
    def exportGAPI(self):
        print("exporting all items in listwidget to files")
        self.label_Message.setText("Message: Exporting all items to .txt file in outputs folder")

        items = [self.listWidget.item(x).text() for x in range(self.listWidget.count())]
        print(items)
        for i in items:
            user = self.lineEdit_twitchUsername.text()
            content = gapd.extraction(i, user)
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
            with open('../outputs/' + i + '_' + dt_string + '.txt', 'w') as f:
                if content:
                    f.write(content)
                else:
                    f.write("empty record")
                f.flush()
                f.close()
        print("exported")
        self.label_Message.setText("Message: Export Complete! .txt files in the outputs folder")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = TwitchInfo()
    window.show()

    sys.exit(app.exec())
