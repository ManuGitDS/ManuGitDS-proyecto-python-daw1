# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cursos.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 400)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_userOn = QLabel(self.centralwidget)
        self.label_userOn.setObjectName(u"label_userOn")
        self.label_userOn.setGeometry(QRect(680, 20, 151, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_userOn.setFont(font)
        self.label_userOn.setStyleSheet(u"QLabel {\n"
"background-color: transparent;\n"
"color:rgb(0, 84, 166);\n"
"}")
        self.label_title_cursos = QLabel(self.centralwidget)
        self.label_title_cursos.setObjectName(u"label_title_cursos")
        self.label_title_cursos.setGeometry(QRect(20, 50, 811, 81))
        font1 = QFont()
        font1.setFamilies([u"Snap ITC"])
        font1.setPointSize(42)
        font1.setItalic(True)
        self.label_title_cursos.setFont(font1)
        self.label_title_cursos.setStyleSheet(u"background-color:transparent;\n"
"color: rgba(0, 0, 0, 0.3); ")
        self.label_title_cursos.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_back_cursos = QPushButton(self.centralwidget)
        self.btn_back_cursos.setObjectName(u"btn_back_cursos")
        self.btn_back_cursos.setGeometry(QRect(20, 20, 51, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_back_cursos.setFont(font2)
        self.btn_back_cursos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_cursos.setMouseTracking(True)
        self.btn_back_cursos.setTabletTracking(False)
        self.btn_back_cursos.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_back_cursos.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(0, 84, 166);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:white;\n"
"color:rgb(0, 84, 166);\n"
"}\n"
"QPushButton:pressed  {\n"
"background-color: rgb(0, 84, 166);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.search_listView_cursos = QTableView(self.centralwidget)
        self.search_listView_cursos.setObjectName(u"search_listView_cursos")
        self.search_listView_cursos.setGeometry(QRect(20, 140, 801, 221))
        self.search_listView_cursos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid black;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_userOn.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_title_cursos.setText(QCoreApplication.translate("MainWindow", u"CURSOS", None))
        self.btn_back_cursos.setText(QCoreApplication.translate("MainWindow", u"Atras", None))
    # retranslateUi

