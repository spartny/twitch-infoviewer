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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import icons_rc

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
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 20))
        self.gridLayout_2 = QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Main = QWidget(MainWindow)
        self.Main.setObjectName(u"Main")
        self.gridLayout = QGridLayout(self.Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_GC = QPushButton(self.Main)
        self.pushButton_GC.setObjectName(u"pushButton_GC")
        self.pushButton_GC.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_GC, 1, 1, 1, 1)

        self.pushButton_ExportFiles = QPushButton(self.Main)
        self.pushButton_ExportFiles.setObjectName(u"pushButton_ExportFiles")
        self.pushButton_ExportFiles.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_ExportFiles, 3, 2, 1, 1)

        self.label = QLabel(self.Main)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 3, 2, 1)

        self.pushButton_ExportFile = QPushButton(self.Main)
        self.pushButton_ExportFile.setObjectName(u"pushButton_ExportFile")
        self.pushButton_ExportFile.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_ExportFile, 3, 5, 1, 1)

        self.lineEdit_twitchUsername = QLineEdit(self.Main)
        self.lineEdit_twitchUsername.setObjectName(u"lineEdit_twitchUsername")

        self.gridLayout.addWidget(self.lineEdit_twitchUsername, 0, 4, 2, 1)

        self.tableWidget = QTableWidget(self.Main)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 2, 3, 1, 3)

        self.label_2 = QLabel(self.Main)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.pushButton_FetchAPI = QPushButton(self.Main)
        self.pushButton_FetchAPI.setObjectName(u"pushButton_FetchAPI")
        self.pushButton_FetchAPI.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_FetchAPI, 0, 5, 2, 1)

        self.listWidget = QListWidget(self.Main)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 3)

        self.pushButton_FF = QPushButton(self.Main)
        self.pushButton_FF.setObjectName(u"pushButton_FF")
        self.pushButton_FF.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_FF, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.Main, 0, 0, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Twitch-InfoViewer", None))
        self.pushButton_GC.setText(QCoreApplication.translate("MainWindow", u"Google Chrome", None))
        self.pushButton_ExportFiles.setText(QCoreApplication.translate("MainWindow", u"Export files", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter Twitch Username:", None))
        self.pushButton_ExportFile.setText(QCoreApplication.translate("MainWindow", u"Export file", None))
        self.lineEdit_twitchUsername.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Browser to extract data from:", None))
        self.pushButton_FetchAPI.setText(QCoreApplication.translate("MainWindow", u"Fetch from API", None))
        self.pushButton_FF.setText(QCoreApplication.translate("MainWindow", u"Mozilla Firefox", None))
    # retranslateUi

