# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchAlumnoWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_SearchAlumnoWindow(object):
    def setupUi(self, SearchAlumnoWindow):
        if not SearchAlumnoWindow.objectName():
            SearchAlumnoWindow.setObjectName(u"SearchAlumnoWindow")
        SearchAlumnoWindow.resize(840, 400)
        SearchAlumnoWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(SearchAlumnoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_search_alumno = QLineEdit(self.centralwidget)
        self.input_search_alumno.setObjectName(u"input_search_alumno")
        self.input_search_alumno.setGeometry(QRect(200, 110, 221, 40))
        font = QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.input_search_alumno.setFont(font)
        self.input_search_alumno.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_search_alumno.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.search_listView_alumno = QListView(self.centralwidget)
        self.search_listView_alumno.setObjectName(u"search_listView_alumno")
        self.search_listView_alumno.setGeometry(QRect(10, 190, 811, 181))
        font1 = QFont()
        font1.setPointSize(12)
        self.search_listView_alumno.setFont(font1)
        self.search_listView_alumno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid black;\n"
"")
        self.label_search_alumno = QLabel(self.centralwidget)
        self.label_search_alumno.setObjectName(u"label_search_alumno")
        self.label_search_alumno.setGeometry(QRect(10, 110, 191, 40))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_search_alumno.setFont(font2)
        self.label_search_alumno.setStyleSheet(u"background-color:transparent;")
        self.label_search_alumno.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_listarAlumno = QPushButton(self.centralwidget)
        self.btn_listarAlumno.setObjectName(u"btn_listarAlumno")
        self.btn_listarAlumno.setGeometry(QRect(600, 110, 221, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.btn_listarAlumno.setFont(font3)
        self.btn_listarAlumno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_listarAlumno.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.btn_listarAlumno.setStyleSheet(u"QPushButton {\n"
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
        self.label_title_alumno = QLabel(self.centralwidget)
        self.label_title_alumno.setObjectName(u"label_title_alumno")
        self.label_title_alumno.setGeometry(QRect(10, 10, 811, 81))
        font4 = QFont()
        font4.setFamilies([u"Snap ITC"])
        font4.setPointSize(42)
        font4.setItalic(True)
        self.label_title_alumno.setFont(font4)
        self.label_title_alumno.setStyleSheet(u"background-color:transparent;\n"
"color: rgba(0, 0, 0, 0.3); ")
        self.label_title_alumno.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_search_alumno = QPushButton(self.centralwidget)
        self.btn_search_alumno.setObjectName(u"btn_search_alumno")
        self.btn_search_alumno.setGeometry(QRect(430, 110, 141, 40))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(False)
        self.btn_search_alumno.setFont(font5)
        self.btn_search_alumno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search_alumno.setMouseTracking(True)
        self.btn_search_alumno.setTabletTracking(False)
        self.btn_search_alumno.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_search_alumno.setStyleSheet(u"QPushButton {\n"
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
        self.btn_back_alumno_search = QPushButton(self.centralwidget)
        self.btn_back_alumno_search.setObjectName(u"btn_back_alumno_search")
        self.btn_back_alumno_search.setGeometry(QRect(10, 10, 51, 31))
        self.btn_back_alumno_search.setFont(font5)
        self.btn_back_alumno_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_alumno_search.setMouseTracking(True)
        self.btn_back_alumno_search.setTabletTracking(False)
        self.btn_back_alumno_search.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_back_alumno_search.setStyleSheet(u"QPushButton {\n"
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
        SearchAlumnoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SearchAlumnoWindow)
        self.statusbar.setObjectName(u"statusbar")
        SearchAlumnoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchAlumnoWindow)

        QMetaObject.connectSlotsByName(SearchAlumnoWindow)
    # setupUi

    def retranslateUi(self, SearchAlumnoWindow):
        SearchAlumnoWindow.setWindowTitle(QCoreApplication.translate("SearchAlumnoWindow", u"MainWindow", None))
        self.input_search_alumno.setText("")
        self.input_search_alumno.setPlaceholderText("")
        self.label_search_alumno.setText(QCoreApplication.translate("SearchAlumnoWindow", u"Nombre o Apellido:", None))
        self.btn_listarAlumno.setText(QCoreApplication.translate("SearchAlumnoWindow", u"Listar todos los Alumnos", None))
        self.label_title_alumno.setText(QCoreApplication.translate("SearchAlumnoWindow", u"BUSCAR ALUMNOS", None))
        self.btn_search_alumno.setText(QCoreApplication.translate("SearchAlumnoWindow", u"Buscar", None))
        self.btn_back_alumno_search.setText(QCoreApplication.translate("SearchAlumnoWindow", u"Atras", None))
    # retranslateUi

