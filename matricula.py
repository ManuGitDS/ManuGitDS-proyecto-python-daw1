# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'matricula.ui'
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

class Ui_matricula_MainWindow(object):
    def setupUi(self, matricula_MainWindow):
        if not matricula_MainWindow.objectName():
            matricula_MainWindow.setObjectName(u"matricula_MainWindow")
        matricula_MainWindow.resize(840, 400)
        matricula_MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(matricula_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.search_listView_matricula = QTableView(self.centralwidget)
        self.search_listView_matricula.setObjectName(u"search_listView_matricula")
        self.search_listView_matricula.setGeometry(QRect(20, 140, 801, 221))
        self.search_listView_matricula.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid black;\n"
"")
        self.label_title_matriculas = QLabel(self.centralwidget)
        self.label_title_matriculas.setObjectName(u"label_title_matriculas")
        self.label_title_matriculas.setGeometry(QRect(20, 40, 811, 81))
        font = QFont()
        font.setFamilies([u"Snap ITC"])
        font.setPointSize(42)
        font.setItalic(True)
        self.label_title_matriculas.setFont(font)
        self.label_title_matriculas.setStyleSheet(u"background-color:transparent;\n"
"color: rgba(0, 0, 0, 0.3); ")
        self.label_title_matriculas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_back_matriculas = QPushButton(self.centralwidget)
        self.btn_back_matriculas.setObjectName(u"btn_back_matriculas")
        self.btn_back_matriculas.setGeometry(QRect(20, 10, 51, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_back_matriculas.setFont(font1)
        self.btn_back_matriculas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_matriculas.setMouseTracking(True)
        self.btn_back_matriculas.setTabletTracking(False)
        self.btn_back_matriculas.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_back_matriculas.setStyleSheet(u"QPushButton {\n"
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
        self.label_userOn = QLabel(self.centralwidget)
        self.label_userOn.setObjectName(u"label_userOn")
        self.label_userOn.setGeometry(QRect(680, 10, 151, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_userOn.setFont(font2)
        self.label_userOn.setStyleSheet(u"QLabel {\n"
"background-color: transparent;\n"
"color:rgb(0, 84, 166);\n"
"}")
        matricula_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(matricula_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        matricula_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(matricula_MainWindow)

        QMetaObject.connectSlotsByName(matricula_MainWindow)
    # setupUi

    def retranslateUi(self, matricula_MainWindow):
        matricula_MainWindow.setWindowTitle(QCoreApplication.translate("matricula_MainWindow", u"MainWindow", None))
        self.label_title_matriculas.setText(QCoreApplication.translate("matricula_MainWindow", u"MATRICULAS", None))
        self.btn_back_matriculas.setText(QCoreApplication.translate("matricula_MainWindow", u"Atras", None))
        self.label_userOn.setText(QCoreApplication.translate("matricula_MainWindow", u"Usuario:", None))
    # retranslateUi

