# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addAlumnoWindow.ui'
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

class Ui_addAlumnoWindow(object):
    def setupUi(self, addAlumnoWindow):
        if not addAlumnoWindow.objectName():
            addAlumnoWindow.setObjectName(u"addAlumnoWindow")
        addAlumnoWindow.resize(840, 400)
        addAlumnoWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(addAlumnoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_alumnoAddUserID = QLabel(self.centralwidget)
        self.label_alumnoAddUserID.setObjectName(u"label_alumnoAddUserID")
        self.label_alumnoAddUserID.setGeometry(QRect(480, 110, 111, 31))
        self.label_alumnoAddUserID.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_alumnoAddUserID.setFont(font)
        self.label_alumnoAddUserID.setStyleSheet(u"background-color:transparent;")
        self.label_alumnoAddUserID.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_alumnoAddFirstName = QLineEdit(self.centralwidget)
        self.input_alumnoAddFirstName.setObjectName(u"input_alumnoAddFirstName")
        self.input_alumnoAddFirstName.setGeometry(QRect(160, 160, 221, 31))
        self.input_alumnoAddFirstName.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setItalic(False)
        self.input_alumnoAddFirstName.setFont(font1)
        self.input_alumnoAddFirstName.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_alumnoAddFirstName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_title_alumno = QLabel(self.centralwidget)
        self.label_title_alumno.setObjectName(u"label_title_alumno")
        self.label_title_alumno.setGeometry(QRect(10, 20, 811, 81))
        font2 = QFont()
        font2.setFamilies([u"Snap ITC"])
        font2.setPointSize(42)
        font2.setItalic(True)
        self.label_title_alumno.setFont(font2)
        self.label_title_alumno.setStyleSheet(u"background-color:transparent;\n"
"color: rgba(0, 0, 0, 0.3); ")
        self.label_title_alumno.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_alumnoAddSecondName = QLineEdit(self.centralwidget)
        self.input_alumnoAddSecondName.setObjectName(u"input_alumnoAddSecondName")
        self.input_alumnoAddSecondName.setGeometry(QRect(590, 160, 221, 31))
        self.input_alumnoAddSecondName.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(False)
        self.input_alumnoAddSecondName.setFont(font3)
        self.input_alumnoAddSecondName.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_alumnoAddSecondName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_alumnoAddFirstName = QLabel(self.centralwidget)
        self.label_alumnoAddFirstName.setObjectName(u"label_alumnoAddFirstName")
        self.label_alumnoAddFirstName.setGeometry(QRect(0, 160, 161, 31))
        self.label_alumnoAddFirstName.setMaximumSize(QSize(16777215, 16777215))
        self.label_alumnoAddFirstName.setFont(font)
        self.label_alumnoAddFirstName.setStyleSheet(u"background-color:transparent;")
        self.label_alumnoAddFirstName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_alumnoAddSecondName = QLabel(self.centralwidget)
        self.label_alumnoAddSecondName.setObjectName(u"label_alumnoAddSecondName")
        self.label_alumnoAddSecondName.setGeometry(QRect(410, 160, 181, 31))
        self.label_alumnoAddSecondName.setMaximumSize(QSize(16777215, 16777215))
        self.label_alumnoAddSecondName.setFont(font)
        self.label_alumnoAddSecondName.setStyleSheet(u"background-color:transparent;")
        self.label_alumnoAddSecondName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_alumnoAddConfirmPassword_2 = QLabel(self.centralwidget)
        self.label_alumnoAddConfirmPassword_2.setObjectName(u"label_alumnoAddConfirmPassword_2")
        self.label_alumnoAddConfirmPassword_2.setGeometry(QRect(390, 210, 201, 31))
        self.label_alumnoAddConfirmPassword_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_alumnoAddConfirmPassword_2.setFont(font)
        self.label_alumnoAddConfirmPassword_2.setStyleSheet(u"background-color:transparent;")
        self.label_alumnoAddConfirmPassword_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addErrorMsgAlumno = QLabel(self.centralwidget)
        self.addErrorMsgAlumno.setObjectName(u"addErrorMsgAlumno")
        self.addErrorMsgAlumno.setGeometry(QRect(190, 270, 471, 41))
        self.addErrorMsgAlumno.setFont(font)
        self.addErrorMsgAlumno.setStyleSheet(u"background-color:transparent;\n"
"color:red;")
        self.addErrorMsgAlumno.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_alumnoAddPassword = QLineEdit(self.centralwidget)
        self.input_alumnoAddPassword.setObjectName(u"input_alumnoAddPassword")
        self.input_alumnoAddPassword.setGeometry(QRect(160, 210, 221, 31))
        self.input_alumnoAddPassword.setMaximumSize(QSize(16777215, 16777215))
        self.input_alumnoAddPassword.setFont(font1)
        self.input_alumnoAddPassword.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_alumnoAddPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_alumnoAddPassword = QLabel(self.centralwidget)
        self.label_alumnoAddPassword.setObjectName(u"label_alumnoAddPassword")
        self.label_alumnoAddPassword.setGeometry(QRect(60, 210, 101, 31))
        self.label_alumnoAddPassword.setMaximumSize(QSize(16777215, 16777215))
        self.label_alumnoAddPassword.setFont(font)
        self.label_alumnoAddPassword.setStyleSheet(u"background-color:transparent;")
        self.label_alumnoAddPassword.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_alumnoAddUserID = QLineEdit(self.centralwidget)
        self.input_alumnoAddUserID.setObjectName(u"input_alumnoAddUserID")
        self.input_alumnoAddUserID.setGeometry(QRect(590, 110, 221, 31))
        self.input_alumnoAddUserID.setMaximumSize(QSize(16777215, 16777215))
        self.input_alumnoAddUserID.setFont(font3)
        self.input_alumnoAddUserID.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_alumnoAddUserID.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.input_alumnoAddName = QLineEdit(self.centralwidget)
        self.input_alumnoAddName.setObjectName(u"input_alumnoAddName")
        self.input_alumnoAddName.setGeometry(QRect(160, 110, 221, 31))
        self.input_alumnoAddName.setMaximumSize(QSize(16777215, 16777215))
        self.input_alumnoAddName.setFont(font1)
        self.input_alumnoAddName.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_alumnoAddName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.input_alumnoAddConfirmPassword = QLineEdit(self.centralwidget)
        self.input_alumnoAddConfirmPassword.setObjectName(u"input_alumnoAddConfirmPassword")
        self.input_alumnoAddConfirmPassword.setGeometry(QRect(590, 210, 221, 31))
        self.input_alumnoAddConfirmPassword.setMaximumSize(QSize(16777215, 16777215))
        self.input_alumnoAddConfirmPassword.setFont(font3)
        self.input_alumnoAddConfirmPassword.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_alumnoAddConfirmPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_alumnoAddName = QLabel(self.centralwidget)
        self.label_alumnoAddName.setObjectName(u"label_alumnoAddName")
        self.label_alumnoAddName.setGeometry(QRect(70, 110, 91, 31))
        self.label_alumnoAddName.setMaximumSize(QSize(16777215, 16777215))
        self.label_alumnoAddName.setFont(font)
        self.label_alumnoAddName.setStyleSheet(u"background-color:transparent;")
        self.label_alumnoAddName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_confirm_alumno = QPushButton(self.centralwidget)
        self.btn_confirm_alumno.setObjectName(u"btn_confirm_alumno")
        self.btn_confirm_alumno.setGeometry(QRect(310, 320, 221, 40))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.btn_confirm_alumno.setFont(font4)
        self.btn_confirm_alumno.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirm_alumno.setMouseTracking(True)
        self.btn_confirm_alumno.setTabletTracking(False)
        self.btn_confirm_alumno.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_confirm_alumno.setStyleSheet(u"QPushButton {\n"
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
        self.btn_back_alumno_add = QPushButton(self.centralwidget)
        self.btn_back_alumno_add.setObjectName(u"btn_back_alumno_add")
        self.btn_back_alumno_add.setGeometry(QRect(10, 330, 51, 31))
        self.btn_back_alumno_add.setFont(font4)
        self.btn_back_alumno_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_alumno_add.setMouseTracking(True)
        self.btn_back_alumno_add.setTabletTracking(False)
        self.btn_back_alumno_add.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_back_alumno_add.setStyleSheet(u"QPushButton {\n"
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
        self.label_userOn.setGeometry(QRect(670, 10, 151, 31))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_userOn.setFont(font5)
        self.label_userOn.setStyleSheet(u"QLabel {\n"
"background-color: transparent;\n"
"color:rgb(0, 84, 166);\n"
"}")
        addAlumnoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(addAlumnoWindow)
        self.statusbar.setObjectName(u"statusbar")
        addAlumnoWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.input_alumnoAddName, self.input_alumnoAddUserID)
        QWidget.setTabOrder(self.input_alumnoAddUserID, self.input_alumnoAddFirstName)
        QWidget.setTabOrder(self.input_alumnoAddFirstName, self.input_alumnoAddSecondName)
        QWidget.setTabOrder(self.input_alumnoAddSecondName, self.input_alumnoAddPassword)
        QWidget.setTabOrder(self.input_alumnoAddPassword, self.input_alumnoAddConfirmPassword)
        QWidget.setTabOrder(self.input_alumnoAddConfirmPassword, self.btn_confirm_alumno)

        self.retranslateUi(addAlumnoWindow)

        QMetaObject.connectSlotsByName(addAlumnoWindow)
    # setupUi

    def retranslateUi(self, addAlumnoWindow):
        addAlumnoWindow.setWindowTitle(QCoreApplication.translate("addAlumnoWindow", u"MainWindow", None))
        self.label_alumnoAddUserID.setText(QCoreApplication.translate("addAlumnoWindow", u"Usuario ID:", None))
        self.input_alumnoAddFirstName.setText("")
        self.input_alumnoAddFirstName.setPlaceholderText("")
        self.label_title_alumno.setText(QCoreApplication.translate("addAlumnoWindow", u"A\u00d1ADIR ALUMNO", None))
        self.input_alumnoAddSecondName.setText("")
        self.input_alumnoAddSecondName.setPlaceholderText("")
        self.label_alumnoAddFirstName.setText(QCoreApplication.translate("addAlumnoWindow", u"Primer Apellido:", None))
        self.label_alumnoAddSecondName.setText(QCoreApplication.translate("addAlumnoWindow", u"Segundo Apellido:", None))
        self.label_alumnoAddConfirmPassword_2.setText(QCoreApplication.translate("addAlumnoWindow", u"Confirmar password:", None))
        self.addErrorMsgAlumno.setText(QCoreApplication.translate("addAlumnoWindow", u"ERROR", None))
        self.input_alumnoAddPassword.setText("")
        self.input_alumnoAddPassword.setPlaceholderText("")
        self.label_alumnoAddPassword.setText(QCoreApplication.translate("addAlumnoWindow", u"Password:", None))
        self.input_alumnoAddUserID.setText("")
        self.input_alumnoAddUserID.setPlaceholderText("")
        self.input_alumnoAddName.setText("")
        self.input_alumnoAddName.setPlaceholderText("")
        self.input_alumnoAddConfirmPassword.setText("")
        self.input_alumnoAddConfirmPassword.setPlaceholderText("")
        self.label_alumnoAddName.setText(QCoreApplication.translate("addAlumnoWindow", u"Nombre:", None))
        self.btn_confirm_alumno.setText(QCoreApplication.translate("addAlumnoWindow", u"Confirmar", None))
        self.btn_back_alumno_add.setText(QCoreApplication.translate("addAlumnoWindow", u"Atras", None))
        self.label_userOn.setText(QCoreApplication.translate("addAlumnoWindow", u"Usuario:", None))
    # retranslateUi

