import sys

from PySide6.QtCore import QSize, Qt, QFile, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    app = QApplication(sys.argv)

    ui_file = QFile("main.ui")
    ui_file.open(QFile.ReadOnly)
    ui_file = QFile(ui_file)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())    
