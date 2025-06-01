# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchProfWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QWidget)

class Ui_SearchProfWindow(object):
    def setupUi(self, SearchProfWindow):
        if not SearchProfWindow.objectName():
            SearchProfWindow.setObjectName(u"SearchProfWindow")
        SearchProfWindow.resize(840, 400)
        SearchProfWindow.setMouseTracking(False)
        SearchProfWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(SearchProfWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_search_profesor = QLabel(self.centralwidget)
        self.label_search_profesor.setObjectName(u"label_search_profesor")
        self.label_search_profesor.setGeometry(QRect(10, 110, 191, 40))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_search_profesor.setFont(font)
        self.label_search_profesor.setStyleSheet(u"background-color:transparent;")
        self.label_search_profesor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_listarProfesor = QPushButton(self.centralwidget)
        self.btn_listarProfesor.setObjectName(u"btn_listarProfesor")
        self.btn_listarProfesor.setGeometry(QRect(600, 110, 221, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_listarProfesor.setFont(font1)
        self.btn_listarProfesor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_listarProfesor.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.btn_listarProfesor.setStyleSheet(u"QPushButton {\n"
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
        self.input_search_profesor = QLineEdit(self.centralwidget)
        self.input_search_profesor.setObjectName(u"input_search_profesor")
        self.input_search_profesor.setGeometry(QRect(200, 110, 221, 40))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setItalic(False)
        self.input_search_profesor.setFont(font2)
        self.input_search_profesor.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_search_profesor.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.btn_search_profesor = QPushButton(self.centralwidget)
        self.btn_search_profesor.setObjectName(u"btn_search_profesor")
        self.btn_search_profesor.setGeometry(QRect(430, 110, 141, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.btn_search_profesor.setFont(font3)
        self.btn_search_profesor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_search_profesor.setMouseTracking(True)
        self.btn_search_profesor.setTabletTracking(False)
        self.btn_search_profesor.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_search_profesor.setStyleSheet(u"QPushButton {\n"
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
        self.label_title_profesor = QLabel(self.centralwidget)
        self.label_title_profesor.setObjectName(u"label_title_profesor")
        self.label_title_profesor.setGeometry(QRect(10, 30, 811, 81))
        font4 = QFont()
        font4.setFamilies([u"Snap ITC"])
        font4.setPointSize(40)
        font4.setItalic(True)
        self.label_title_profesor.setFont(font4)
        self.label_title_profesor.setStyleSheet(u"background-color:transparent;\n"
"color: rgba(0, 0, 0, 0.3); ")
        self.label_title_profesor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_back_alumno_search = QPushButton(self.centralwidget)
        self.btn_back_alumno_search.setObjectName(u"btn_back_alumno_search")
        self.btn_back_alumno_search.setGeometry(QRect(10, 10, 51, 31))
        self.btn_back_alumno_search.setFont(font3)
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
        self.search_listView_profesor_2 = QTableView(self.centralwidget)
        self.search_listView_profesor_2.setObjectName(u"search_listView_profesor_2")
        self.search_listView_profesor_2.setGeometry(QRect(20, 170, 801, 201))
        self.search_listView_profesor_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid black;\n"
"")
        self.label_userOn = QLabel(self.centralwidget)
        self.label_userOn.setObjectName(u"label_userOn")
        self.label_userOn.setGeometry(QRect(670, 10, 151, 31))
        self.label_userOn.setFont(font1)
        self.label_userOn.setStyleSheet(u"QLabel {\n"
"background-color: transparent;\n"
"color:rgb(0, 84, 166);\n"
"}")
        SearchProfWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SearchProfWindow)
        self.statusbar.setObjectName(u"statusbar")
        SearchProfWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchProfWindow)

        QMetaObject.connectSlotsByName(SearchProfWindow)
    # setupUi

    def retranslateUi(self, SearchProfWindow):
        SearchProfWindow.setWindowTitle(QCoreApplication.translate("SearchProfWindow", u"MainWindow", None))
        self.label_search_profesor.setText(QCoreApplication.translate("SearchProfWindow", u"Nombre o Apellido:", None))
        self.btn_listarProfesor.setText(QCoreApplication.translate("SearchProfWindow", u"Listar todos los profesores", None))
        self.input_search_profesor.setText("")
        self.input_search_profesor.setPlaceholderText("")
        self.btn_search_profesor.setText(QCoreApplication.translate("SearchProfWindow", u"Buscar", None))
        self.label_title_profesor.setText(QCoreApplication.translate("SearchProfWindow", u"BUSCAR PROFESORES", None))
        self.btn_back_alumno_search.setText(QCoreApplication.translate("SearchProfWindow", u"Atras", None))
        self.label_userOn.setText(QCoreApplication.translate("SearchProfWindow", u"Usuario:", None))
    # retranslateUi

