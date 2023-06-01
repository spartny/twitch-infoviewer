/********************************************************************************
** Form generated from reading UI file 'main.ui'
**
** Created by: Qt User Interface Compiler version 6.5.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAIN_UI_H
#define MAIN_UI_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QPushButton *pushButton_FF;
    QPushButton *pushButton_GC;
    QPushButton *pushButton_FetchAPI;
    QListWidget *listWidget;
    QTableWidget *tableWidget;
    QPushButton *pushButton_ExportFiles;
    QLineEdit *lineEdit_twitchUsername;
    QLabel *label;
    QPushButton *pushButton_ExportFile;
    QLabel *label_2;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(900, 600);
        MainWindow->setMinimumSize(QSize(900, 600));
        MainWindow->setMaximumSize(QSize(900, 600));
        QFont font;
        font.setFamilies({QString::fromUtf8("Arial")});
        font.setPointSize(10);
        MainWindow->setFont(font);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icon/twitch-info.png"), QSize(), QIcon::Normal, QIcon::Off);
        MainWindow->setWindowIcon(icon);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        pushButton_FF = new QPushButton(centralwidget);
        pushButton_FF->setObjectName("pushButton_FF");
        pushButton_FF->setGeometry(QRect(20, 30, 100, 30));
        pushButton_FF->setMaximumSize(QSize(100, 30));
        pushButton_GC = new QPushButton(centralwidget);
        pushButton_GC->setObjectName("pushButton_GC");
        pushButton_GC->setGeometry(QRect(130, 30, 100, 30));
        pushButton_GC->setMaximumSize(QSize(100, 30));
        pushButton_FetchAPI = new QPushButton(centralwidget);
        pushButton_FetchAPI->setObjectName("pushButton_FetchAPI");
        pushButton_FetchAPI->setGeometry(QRect(760, 20, 100, 30));
        pushButton_FetchAPI->setMaximumSize(QSize(100, 30));
        listWidget = new QListWidget(centralwidget);
        listWidget->setObjectName("listWidget");
        listWidget->setGeometry(QRect(20, 70, 321, 461));
        tableWidget = new QTableWidget(centralwidget);
        tableWidget->setObjectName("tableWidget");
        tableWidget->setGeometry(QRect(370, 70, 491, 461));
        pushButton_ExportFiles = new QPushButton(centralwidget);
        pushButton_ExportFiles->setObjectName("pushButton_ExportFiles");
        pushButton_ExportFiles->setGeometry(QRect(230, 540, 100, 30));
        pushButton_ExportFiles->setMaximumSize(QSize(100, 30));
        lineEdit_twitchUsername = new QLineEdit(centralwidget);
        lineEdit_twitchUsername->setObjectName("lineEdit_twitchUsername");
        lineEdit_twitchUsername->setGeometry(QRect(570, 20, 181, 31));
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setGeometry(QRect(430, 20, 141, 31));
        pushButton_ExportFile = new QPushButton(centralwidget);
        pushButton_ExportFile->setObjectName("pushButton_ExportFile");
        pushButton_ExportFile->setGeometry(QRect(760, 540, 100, 30));
        pushButton_ExportFile->setMaximumSize(QSize(100, 30));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(20, 0, 211, 31));
        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "Twitch-InfoViewer", nullptr));
        pushButton_FF->setText(QCoreApplication::translate("MainWindow", "Mozilla Firefox", nullptr));
        pushButton_GC->setText(QCoreApplication::translate("MainWindow", "Google Chrome", nullptr));
        pushButton_FetchAPI->setText(QCoreApplication::translate("MainWindow", "Fetch from API", nullptr));
        pushButton_ExportFiles->setText(QCoreApplication::translate("MainWindow", "Export files", nullptr));
        lineEdit_twitchUsername->setText(QString());
        label->setText(QCoreApplication::translate("MainWindow", "Enter Twitch Username:", nullptr));
        pushButton_ExportFile->setText(QCoreApplication::translate("MainWindow", "Export file", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Select Browser to extract data from:", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAIN_UI_H
