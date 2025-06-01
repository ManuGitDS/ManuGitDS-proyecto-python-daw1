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
        self.label.setGeometry(QRect(59, 33, 731, 191))
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
        self.btn_searchProfesor.setGeometry(QRect(60, 220, 161, 41))
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
        self.btn_addProfesor.setGeometry(QRect(250, 220, 161, 41))
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
        self.btn_searchAlumno.setGeometry(QRect(60, 270, 161, 41))
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
        self.btn_addAlumno.setGeometry(QRect(250, 270, 161, 41))
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
        self.btn_eliminar = QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(60, 320, 731, 41))
        self.btn_eliminar.setFont(font2)
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
        self.label_userOn = QLabel(self.centralwidget)
        self.label_userOn.setObjectName(u"label_userOn")
        self.label_userOn.setGeometry(QRect(670, 10, 151, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_userOn.setFont(font3)
        self.label_userOn.setStyleSheet(u"QLabel {\n"
"background-color: transparent;\n"
"color:rgb(0, 84, 166);\n"
"}")
        self.btn_changeUser = QPushButton(self.centralwidget)
        self.btn_changeUser.setObjectName(u"btn_changeUser")
        self.btn_changeUser.setGeometry(QRect(10, 10, 141, 31))
        self.btn_changeUser.setFont(font2)
        self.btn_changeUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_changeUser.setStyleSheet(u"\n"
"QPushButton {\n"
"border:1px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(0, 84, 166);\n"
"color: black;\n"
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
        self.btn_matriculas = QPushButton(self.centralwidget)
        self.btn_matriculas.setObjectName(u"btn_matriculas")
        self.btn_matriculas.setGeometry(QRect(440, 220, 161, 91))
        self.btn_matriculas.setFont(font2)
        self.btn_matriculas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_matriculas.setStyleSheet(u"QPushButton {\n"
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
        self.btn_materias = QPushButton(self.centralwidget)
        self.btn_materias.setObjectName(u"btn_materias")
        self.btn_materias.setGeometry(QRect(630, 220, 161, 91))
        self.btn_materias.setFont(font2)
        self.btn_materias.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_materias.setStyleSheet(u"QPushButton {\n"
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
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar Profesor/Alumno", None))
        self.label_userOn.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.btn_changeUser.setText(QCoreApplication.translate("MainWindow", u"Cambiar usuario", None))
        self.btn_matriculas.setText(QCoreApplication.translate("MainWindow", u"Matriculas", None))
        self.btn_materias.setText(QCoreApplication.translate("MainWindow", u"Materias", None))
    # retranslateUi

