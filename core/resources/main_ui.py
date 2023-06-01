# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import core.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        MainWindow.setMaximumSize(QSize(900, 600))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/twitch-info.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_FF = QPushButton(self.centralwidget)
        self.pushButton_FF.setObjectName(u"pushButton_FF")
        self.pushButton_FF.setGeometry(QRect(20, 30, 100, 30))
        self.pushButton_FF.setMaximumSize(QSize(100, 30))
        self.pushButton_GC = QPushButton(self.centralwidget)
        self.pushButton_GC.setObjectName(u"pushButton_GC")
        self.pushButton_GC.setGeometry(QRect(130, 30, 100, 30))
        self.pushButton_GC.setMaximumSize(QSize(100, 30))
        self.pushButton_FetchAPI = QPushButton(self.centralwidget)
        self.pushButton_FetchAPI.setObjectName(u"pushButton_FetchAPI")
        self.pushButton_FetchAPI.setGeometry(QRect(760, 20, 100, 30))
        self.pushButton_FetchAPI.setMaximumSize(QSize(100, 30))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 70, 321, 461))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(370, 70, 491, 461))
        self.pushButton_ExportFiles = QPushButton(self.centralwidget)
        self.pushButton_ExportFiles.setObjectName(u"pushButton_ExportFiles")
        self.pushButton_ExportFiles.setGeometry(QRect(230, 540, 100, 30))
        self.pushButton_ExportFiles.setMaximumSize(QSize(100, 30))
        self.lineEdit_twitchUsername = QLineEdit(self.centralwidget)
        self.lineEdit_twitchUsername.setObjectName(u"lineEdit_twitchUsername")
        self.lineEdit_twitchUsername.setGeometry(QRect(570, 20, 181, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 20, 141, 31))
        self.pushButton_ExportFile = QPushButton(self.centralwidget)
        self.pushButton_ExportFile.setObjectName(u"pushButton_ExportFile")
        self.pushButton_ExportFile.setGeometry(QRect(760, 540, 100, 30))
        self.pushButton_ExportFile.setMaximumSize(QSize(100, 30))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 0, 211, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Twitch-InfoViewer", None))
        self.pushButton_FF.setText(QCoreApplication.translate("MainWindow", u"Mozilla Firefox", None))
        self.pushButton_GC.setText(QCoreApplication.translate("MainWindow", u"Google Chrome", None))
        self.pushButton_FetchAPI.setText(QCoreApplication.translate("MainWindow", u"Fetch from API", None))
        self.pushButton_ExportFiles.setText(QCoreApplication.translate("MainWindow", u"Export files", None))
        self.lineEdit_twitchUsername.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter Twitch Username:", None))
        self.pushButton_ExportFile.setText(QCoreApplication.translate("MainWindow", u"Export file", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Browser to extract data from:", None))
    # retranslateUi

