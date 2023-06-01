import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from core.resources.main_ui import Ui_MainWindow


class TwitchInfo(qtw.QWidget, Ui_MainWindow):
    def __int__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = TwitchInfo()
    window.show()

    sys.exit(app.exec())
