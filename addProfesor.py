# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addProfWindow.ui'
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

class Ui_addProfWindow(object):
    def setupUi(self, addProfWindow):
        if not addProfWindow.objectName():
            addProfWindow.setObjectName(u"addProfWindow")
        addProfWindow.resize(840, 400)
        addProfWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QWidget(addProfWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_profAddName = QLineEdit(self.centralwidget)
        self.input_profAddName.setObjectName(u"input_profAddName")
        self.input_profAddName.setGeometry(QRect(160, 110, 221, 31))
        self.input_profAddName.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.input_profAddName.setFont(font)
        self.input_profAddName.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_profAddName.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_profAddName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_profAddName = QLabel(self.centralwidget)
        self.label_profAddName.setObjectName(u"label_profAddName")
        self.label_profAddName.setGeometry(QRect(70, 110, 91, 31))
        self.label_profAddName.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_profAddName.setFont(font1)
        self.label_profAddName.setStyleSheet(u"background-color:transparent;")
        self.label_profAddName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title_profesor = QLabel(self.centralwidget)
        self.label_title_profesor.setObjectName(u"label_title_profesor")
        self.label_title_profesor.setGeometry(QRect(10, 20, 811, 81))
        font2 = QFont()
        font2.setFamilies([u"Snap ITC"])
        font2.setPointSize(42)
        font2.setItalic(True)
        self.label_title_profesor.setFont(font2)
        self.label_title_profesor.setStyleSheet(u"background-color:transparent;\n"
"color: rgba(0, 0, 0, 0.3); ")
        self.label_title_profesor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_confirm_profesor = QPushButton(self.centralwidget)
        self.btn_confirm_profesor.setObjectName(u"btn_confirm_profesor")
        self.btn_confirm_profesor.setGeometry(QRect(310, 320, 221, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.btn_confirm_profesor.setFont(font3)
        self.btn_confirm_profesor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirm_profesor.setMouseTracking(True)
        self.btn_confirm_profesor.setTabletTracking(False)
        self.btn_confirm_profesor.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.btn_confirm_profesor.setStyleSheet(u"QPushButton {\n"
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
        self.input_profAddFirstName = QLineEdit(self.centralwidget)
        self.input_profAddFirstName.setObjectName(u"input_profAddFirstName")
        self.input_profAddFirstName.setGeometry(QRect(160, 160, 221, 31))
        self.input_profAddFirstName.setMaximumSize(QSize(16777215, 16777215))
        self.input_profAddFirstName.setFont(font)
        self.input_profAddFirstName.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_profAddFirstName.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_profAddFirstName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_profAddFirstName = QLabel(self.centralwidget)
        self.label_profAddFirstName.setObjectName(u"label_profAddFirstName")
        self.label_profAddFirstName.setGeometry(QRect(0, 160, 161, 31))
        self.label_profAddFirstName.setMaximumSize(QSize(16777215, 16777215))
        self.label_profAddFirstName.setFont(font1)
        self.label_profAddFirstName.setStyleSheet(u"background-color:transparent;")
        self.label_profAddFirstName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_profAddSecondName = QLineEdit(self.centralwidget)
        self.input_profAddSecondName.setObjectName(u"input_profAddSecondName")
        self.input_profAddSecondName.setGeometry(QRect(590, 160, 221, 31))
        self.input_profAddSecondName.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setItalic(False)
        self.input_profAddSecondName.setFont(font4)
        self.input_profAddSecondName.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_profAddSecondName.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_profAddSecondName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_profAddSecondName = QLabel(self.centralwidget)
        self.label_profAddSecondName.setObjectName(u"label_profAddSecondName")
        self.label_profAddSecondName.setGeometry(QRect(410, 160, 181, 31))
        self.label_profAddSecondName.setMaximumSize(QSize(16777215, 16777215))
        self.label_profAddSecondName.setFont(font1)
        self.label_profAddSecondName.setStyleSheet(u"background-color:transparent;")
        self.label_profAddSecondName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_profAddUserID = QLineEdit(self.centralwidget)
        self.input_profAddUserID.setObjectName(u"input_profAddUserID")
        self.input_profAddUserID.setGeometry(QRect(590, 110, 221, 31))
        self.input_profAddUserID.setMaximumSize(QSize(16777215, 16777215))
        self.input_profAddUserID.setFont(font4)
        self.input_profAddUserID.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_profAddUserID.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_profAddUserID.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_profAddUserID = QLabel(self.centralwidget)
        self.label_profAddUserID.setObjectName(u"label_profAddUserID")
        self.label_profAddUserID.setGeometry(QRect(480, 110, 111, 31))
        self.label_profAddUserID.setMaximumSize(QSize(16777215, 16777215))
        self.label_profAddUserID.setFont(font1)
        self.label_profAddUserID.setStyleSheet(u"background-color:transparent;")
        self.label_profAddUserID.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_profAddPassword = QLineEdit(self.centralwidget)
        self.input_profAddPassword.setObjectName(u"input_profAddPassword")
        self.input_profAddPassword.setGeometry(QRect(160, 210, 221, 31))
        self.input_profAddPassword.setMaximumSize(QSize(16777215, 16777215))
        self.input_profAddPassword.setFont(font)
        self.input_profAddPassword.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_profAddPassword.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_profAddPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_profAddPassword = QLabel(self.centralwidget)
        self.label_profAddPassword.setObjectName(u"label_profAddPassword")
        self.label_profAddPassword.setGeometry(QRect(60, 210, 101, 31))
        self.label_profAddPassword.setMaximumSize(QSize(16777215, 16777215))
        self.label_profAddPassword.setFont(font1)
        self.label_profAddPassword.setStyleSheet(u"background-color:transparent;")
        self.label_profAddPassword.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_profAddConfirmPassword = QLineEdit(self.centralwidget)
        self.input_profAddConfirmPassword.setObjectName(u"input_profAddConfirmPassword")
        self.input_profAddConfirmPassword.setGeometry(QRect(590, 210, 221, 31))
        self.input_profAddConfirmPassword.setMaximumSize(QSize(16777215, 16777215))
        self.input_profAddConfirmPassword.setFont(font4)
        self.input_profAddConfirmPassword.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_profAddConfirmPassword.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_profAddConfirmPassword.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_profAddConfirmPassword_2 = QLabel(self.centralwidget)
        self.label_profAddConfirmPassword_2.setObjectName(u"label_profAddConfirmPassword_2")
        self.label_profAddConfirmPassword_2.setGeometry(QRect(390, 210, 201, 31))
        self.label_profAddConfirmPassword_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_profAddConfirmPassword_2.setFont(font1)
        self.label_profAddConfirmPassword_2.setStyleSheet(u"background-color:transparent;")
        self.label_profAddConfirmPassword_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addErrorMsgProf = QLabel(self.centralwidget)
        self.addErrorMsgProf.setObjectName(u"addErrorMsgProf")
        self.addErrorMsgProf.setGeometry(QRect(190, 270, 471, 41))
        self.addErrorMsgProf.setFont(font1)
        self.addErrorMsgProf.setStyleSheet(u"background-color:transparent;\n"
"color:red;")
        self.addErrorMsgProf.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_back_profesor_add = QPushButton(self.centralwidget)
        self.btn_back_profesor_add.setObjectName(u"btn_back_profesor_add")
        self.btn_back_profesor_add.setGeometry(QRect(10, 329, 51, 31))
        self.btn_back_profesor_add.setFont(font3)
        self.btn_back_profesor_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back_profesor_add.setMouseTracking(True)
        self.btn_back_profesor_add.setTabletTracking(False)
        self.btn_back_profesor_add.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_back_profesor_add.setStyleSheet(u"QPushButton {\n"
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
        addProfWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(addProfWindow)
        self.statusbar.setObjectName(u"statusbar")
        addProfWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.input_profAddName, self.input_profAddUserID)
        QWidget.setTabOrder(self.input_profAddUserID, self.input_profAddFirstName)
        QWidget.setTabOrder(self.input_profAddFirstName, self.input_profAddSecondName)
        QWidget.setTabOrder(self.input_profAddSecondName, self.input_profAddPassword)
        QWidget.setTabOrder(self.input_profAddPassword, self.input_profAddConfirmPassword)
        QWidget.setTabOrder(self.input_profAddConfirmPassword, self.btn_confirm_profesor)

        self.retranslateUi(addProfWindow)

        QMetaObject.connectSlotsByName(addProfWindow)
    # setupUi

    def retranslateUi(self, addProfWindow):
        addProfWindow.setWindowTitle(QCoreApplication.translate("addProfWindow", u"MainWindow", None))
        self.input_profAddName.setText("")
        self.input_profAddName.setPlaceholderText("")
        self.label_profAddName.setText(QCoreApplication.translate("addProfWindow", u"Nombre:", None))
        self.label_title_profesor.setText(QCoreApplication.translate("addProfWindow", u"A\u00d1ADIR PROFESOR", None))
        self.btn_confirm_profesor.setText(QCoreApplication.translate("addProfWindow", u"Confirmar", None))
        self.input_profAddFirstName.setText("")
        self.input_profAddFirstName.setPlaceholderText("")
        self.label_profAddFirstName.setText(QCoreApplication.translate("addProfWindow", u"Primer Apellido:", None))
        self.input_profAddSecondName.setText("")
        self.input_profAddSecondName.setPlaceholderText("")
        self.label_profAddSecondName.setText(QCoreApplication.translate("addProfWindow", u"Segundo Apellido:", None))
        self.input_profAddUserID.setText("")
        self.input_profAddUserID.setPlaceholderText("")
        self.label_profAddUserID.setText(QCoreApplication.translate("addProfWindow", u"Usuario ID:", None))
        self.input_profAddPassword.setText("")
        self.input_profAddPassword.setPlaceholderText("")
        self.label_profAddPassword.setText(QCoreApplication.translate("addProfWindow", u"Password:", None))
        self.input_profAddConfirmPassword.setText("")
        self.input_profAddConfirmPassword.setPlaceholderText("")
        self.label_profAddConfirmPassword_2.setText(QCoreApplication.translate("addProfWindow", u"Confirmar password:", None))
        self.addErrorMsgProf.setText(QCoreApplication.translate("addProfWindow", u"ERROR", None))
        self.btn_back_profesor_add.setText(QCoreApplication.translate("addProfWindow", u"Atras", None))
        self.label_userOn.setText(QCoreApplication.translate("addProfWindow", u"Usuario:", None))
    # retranslateUi

