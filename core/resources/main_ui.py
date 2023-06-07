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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)
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
        self.pushButton_FetchAPI = QPushButton(self.Main)
        self.pushButton_FetchAPI.setObjectName(u"pushButton_FetchAPI")
        self.pushButton_FetchAPI.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_FetchAPI, 0, 5, 2, 1)

        self.pushButton_FF = QPushButton(self.Main)
        self.pushButton_FF.setObjectName(u"pushButton_FF")
        self.pushButton_FF.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_FF, 1, 0, 1, 1)

        self.listWidget = QListWidget(self.Main)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 3)

        self.textEdit = QTextEdit(self.Main)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 2, 3, 1, 5)

        self.lineEdit_twitchUsername = QLineEdit(self.Main)
        self.lineEdit_twitchUsername.setObjectName(u"lineEdit_twitchUsername")

        self.gridLayout.addWidget(self.lineEdit_twitchUsername, 0, 4, 2, 1)

        self.pushButton_GC = QPushButton(self.Main)
        self.pushButton_GC.setObjectName(u"pushButton_GC")
        self.pushButton_GC.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_GC, 1, 1, 1, 1)

        self.pushButton_ViewFile = QPushButton(self.Main)
        self.pushButton_ViewFile.setObjectName(u"pushButton_ViewFile")

        self.gridLayout.addWidget(self.pushButton_ViewFile, 3, 1, 1, 1)

        self.pushButton_ExportFiles = QPushButton(self.Main)
        self.pushButton_ExportFiles.setObjectName(u"pushButton_ExportFiles")
        self.pushButton_ExportFiles.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_ExportFiles, 3, 2, 1, 1)

        self.label_2 = QLabel(self.Main)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.label = QLabel(self.Main)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 3, 2, 1)

        self.pushButton_GeneralAPI = QPushButton(self.Main)
        self.pushButton_GeneralAPI.setObjectName(u"pushButton_GeneralAPI")
        self.pushButton_GeneralAPI.setEnabled(True)
        self.pushButton_GeneralAPI.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.pushButton_GeneralAPI, 0, 7, 2, 1)

        self.pushButton_ExportFile = QPushButton(self.Main)
        self.pushButton_ExportFile.setObjectName(u"pushButton_ExportFile")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ExportFile.sizePolicy().hasHeightForWidth())
        self.pushButton_ExportFile.setSizePolicy(sizePolicy)
        self.pushButton_ExportFile.setMinimumSize(QSize(0, 0))
        self.pushButton_ExportFile.setMaximumSize(QSize(100, 30))

        self.gridLayout.addWidget(self.pushButton_ExportFile, 3, 7, 1, 1, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.Main, 0, 0, 1, 1)

        QWidget.setTabOrder(self.pushButton_FF, self.pushButton_GC)
        QWidget.setTabOrder(self.pushButton_GC, self.lineEdit_twitchUsername)
        QWidget.setTabOrder(self.lineEdit_twitchUsername, self.listWidget)
        QWidget.setTabOrder(self.listWidget, self.pushButton_ViewFile)
        QWidget.setTabOrder(self.pushButton_ViewFile, self.pushButton_ExportFiles)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Twitch-InfoViewer", None))
        self.pushButton_FetchAPI.setText(QCoreApplication.translate("MainWindow", u"Fetch from API", None))
        self.pushButton_FF.setText(QCoreApplication.translate("MainWindow", u"Mozilla Firefox", None))
        self.lineEdit_twitchUsername.setText("")
        self.pushButton_GC.setText(QCoreApplication.translate("MainWindow", u"Google Chrome", None))
        self.pushButton_ViewFile.setText(QCoreApplication.translate("MainWindow", u"View Selected Data", None))
        self.pushButton_ExportFiles.setText(QCoreApplication.translate("MainWindow", u"Export files", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Browser to extract data from:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter Twitch Username:", None))
        self.pushButton_GeneralAPI.setText(QCoreApplication.translate("MainWindow", u"Get General API Data", None))
        self.pushButton_ExportFile.setText(QCoreApplication.translate("MainWindow", u"Export file", None))
    # retranslateUi

