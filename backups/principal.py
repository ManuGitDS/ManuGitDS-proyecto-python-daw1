# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 400)
        font = QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(59, 30, 731, 194))
        self.label.setMaximumSize(QSize(740, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Snap ITC"])
        font1.setPointSize(36)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet(u"background-color:transparent;\n"
"")
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(1)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(0)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.TextEditable)
        self.btn_searchProfesor = QPushButton(self.centralwidget)
        self.btn_searchProfesor.setObjectName(u"btn_searchProfesor")
        self.btn_searchProfesor.setGeometry(QRect(59, 250, 161, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_searchProfesor.setFont(font2)
        self.btn_searchProfesor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_searchProfesor.setStyleSheet(u"\n"
"QPushButton {\n"
"border:1px solid black;\n"
"border-radius: 10px;\n"
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
        self.btn_addProfesor = QPushButton(self.centralwidget)
        self.btn_addProfesor.setObjectName(u"btn_addProfesor")
        self.btn_addProfesor.setGeometry(QRect(249, 250, 161, 41))
        self.btn_addProfesor.setFont(font2)
        self.btn_addProfesor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_addProfesor.setStyleSheet(u"QPushButton {\n"
"border:1px solid black;\n"
"border-radius: 10px;\n"
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
        self.btn_searchAlumno = QPushButton(self.centralwidget)
        self.btn_searchAlumno.setObjectName(u"btn_searchAlumno")
        self.btn_searchAlumno.setGeometry(QRect(439, 250, 161, 41))
        self.btn_searchAlumno.setFont(font2)
        self.btn_searchAlumno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_searchAlumno.setStyleSheet(u"QPushButton {\n"
"border:1px solid black;\n"
"border-radius: 10px;\n"
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
        self.btn_addAlumno = QPushButton(self.centralwidget)
        self.btn_addAlumno.setObjectName(u"btn_addAlumno")
        self.btn_addAlumno.setGeometry(QRect(629, 250, 161, 41))
        self.btn_addAlumno.setFont(font2)
        self.btn_addAlumno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_addAlumno.setStyleSheet(u"QPushButton {\n"
"border:1px solid black;\n"
"border-radius: 10px;\n"
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>APP GESTORA<br/>DEL<br/>INSTITUT LES SALINES</p></body></html>", None))
        self.btn_searchProfesor.setText(QCoreApplication.translate("MainWindow", u"Buscar profesor", None))
        self.btn_addProfesor.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir profesor", None))
        self.btn_searchAlumno.setText(QCoreApplication.translate("MainWindow", u"Buscar Alumno", None))
        self.btn_addAlumno.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adirAlumno", None))
    # retranslateUi

