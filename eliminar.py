# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eliminar.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 400)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_eliminar = QLabel(self.centralwidget)
        self.title_eliminar.setObjectName(u"title_eliminar")
        self.title_eliminar.setGeometry(QRect(60, 30, 731, 194))
        self.title_eliminar.setMaximumSize(QSize(740, 16777215))
        font = QFont()
        font.setFamilies([u"Snap ITC"])
        font.setPointSize(36)
        font.setBold(True)
        self.title_eliminar.setFont(font)
        self.title_eliminar.setAcceptDrops(False)
        self.title_eliminar.setStyleSheet(u"background-color:transparent;\n"
"color:red;")
        self.title_eliminar.setLineWidth(1)
        self.title_eliminar.setMidLineWidth(1)
        self.title_eliminar.setScaledContents(True)
        self.title_eliminar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_eliminar.setWordWrap(False)
        self.title_eliminar.setMargin(0)
        self.title_eliminar.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditable)
        self.btn_eliminar = QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(520, 260, 161, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_eliminar.setFont(font1)
        self.btn_eliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_eliminar.setStyleSheet(u"\n"
"QPushButton {\n"
"border:1px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(0, 84, 166);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:red;\n"
"color:black;\n"
"}\n"
"QPushButton:pressed  {\n"
"background-color: rgb(0, 84, 166);\n"
"color: white;\n"
"}\n"
"")
        self.label_eliminar = QLabel(self.centralwidget)
        self.label_eliminar.setObjectName(u"label_eliminar")
        self.label_eliminar.setGeometry(QRect(120, 252, 161, 51))
        self.label_eliminar.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_eliminar.setFont(font2)
        self.label_eliminar.setStyleSheet(u"background-color:transparent;")
        self.label_eliminar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_eliminar = QLineEdit(self.centralwidget)
        self.input_eliminar.setObjectName(u"input_eliminar")
        self.input_eliminar.setGeometry(QRect(290, 260, 221, 41))
        self.input_eliminar.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setItalic(False)
        self.input_eliminar.setFont(font3)
        self.input_eliminar.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_eliminar.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_eliminar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.btn_back_eliminar = QPushButton(self.centralwidget)
        self.btn_back_eliminar.setObjectName(u"btn_back_eliminar")
        self.btn_back_eliminar.setGeometry(QRect(20, 330, 51, 31))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.btn_back_eliminar.setFont(font4)
        self.btn_back_eliminar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_eliminar.setMouseTracking(True)
        self.btn_back_eliminar.setTabletTracking(False)
        self.btn_back_eliminar.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_back_eliminar.setStyleSheet(u"QPushButton {\n"
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
        self.label_userOn.setGeometry(QRect(670, 20, 151, 31))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_userOn.setFont(font5)
        self.label_userOn.setStyleSheet(u"QLabel {\n"
"background-color: transparent;\n"
"color:rgb(0, 84, 166);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.input_eliminar, self.btn_eliminar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_eliminar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>ELIMINAR</p><p>PROFESOR/ALUMNO</p></body></html>", None))
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar Usuario:", None))
        self.input_eliminar.setText("")
        self.input_eliminar.setPlaceholderText("")
        self.btn_back_eliminar.setText(QCoreApplication.translate("MainWindow", u"Atras", None))
        self.label_userOn.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
    # retranslateUi

