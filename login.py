# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_formLogin(object):
    def setupUi(self, formLogin):
        if not formLogin.objectName():
            formLogin.setObjectName(u"formLogin")
        formLogin.resize(834, 492)
        font = QFont()
        font.setPointSize(12)
        font.setItalic(False)
        formLogin.setFont(font)
        formLogin.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(108, 143, 196, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3 = QLabel(formLogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(244, 250, 61, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_4 = QLabel(formLogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(219, 290, 91, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"")
        self.input_login_usuario = QLineEdit(formLogin)
        self.input_login_usuario.setObjectName(u"input_login_usuario")
        self.input_login_usuario.setGeometry(QRect(322, 257, 165, 23))
        self.input_login_usuario.setFont(font)
        self.input_login_usuario.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_login_usuario.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;\n"
"")
        self.input_login_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_login_password = QLineEdit(formLogin)
        self.input_login_password.setObjectName(u"input_login_password")
        self.input_login_password.setGeometry(QRect(322, 296, 165, 23))
        self.input_login_password.setFont(font)
        self.input_login_password.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.input_login_password.setStyleSheet(u"border-radius:8px;\n"
"border: 1px solid gray;")
        self.input_login_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_login_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(formLogin)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(322, 217, 165, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: transparent;\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_login_acceder = QPushButton(formLogin)
        self.btn_login_acceder.setObjectName(u"btn_login_acceder")
        self.btn_login_acceder.setEnabled(True)
        self.btn_login_acceder.setGeometry(QRect(330, 340, 131, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_login_acceder.setFont(font2)
        self.btn_login_acceder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login_acceder.setStyleSheet(u"QPushButton {\n"
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
        self.btn_login_acceder.setAutoDefault(False)
        self.login_mensaje_error = QLabel(formLogin)
        self.login_mensaje_error.setObjectName(u"login_mensaje_error")
        self.login_mensaje_error.setGeometry(QRect(256, 390, 321, 23))
        self.login_mensaje_error.setFont(font)
        self.login_mensaje_error.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color:transparent;")
        self.login_mensaje_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(formLogin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 731, 191))
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setPixmap(QPixmap(u"logo.png"))
        self.label.setScaledContents(True)
        self.userDefault_label_2 = QLabel(formLogin)
        self.userDefault_label_2.setObjectName(u"userDefault_label_2")
        self.userDefault_label_2.setGeometry(QRect(670, 10, 141, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.userDefault_label_2.setFont(font3)
        self.userDefault_label_2.setStyleSheet(u"background-color: transparent;\n"
"color:green;\n"
"")
        self.passwordDefault_label = QLabel(formLogin)
        self.passwordDefault_label.setObjectName(u"passwordDefault_label")
        self.passwordDefault_label.setGeometry(QRect(670, 40, 141, 21))
        self.passwordDefault_label.setFont(font3)
        self.passwordDefault_label.setStyleSheet(u"background-color: transparent;\n"
"color:green;\n"
"")

        self.retranslateUi(formLogin)

        self.btn_login_acceder.setDefault(True)


        QMetaObject.connectSlotsByName(formLogin)
    # setupUi

    def retranslateUi(self, formLogin):
        formLogin.setWindowTitle(QCoreApplication.translate("formLogin", u"Inicio de sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("formLogin", u"<html><head/><body><p><span style=\" font-weight:700;\">Usuario:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("formLogin", u"<html><head/><body><p><span style=\" font-weight:700;\">Contrase\u00f1a:</span></p></body></html>", None))
        self.input_login_usuario.setText("")
        self.input_login_usuario.setPlaceholderText(QCoreApplication.translate("formLogin", u"Nombre de usuario", None))
        self.input_login_password.setText("")
        self.input_login_password.setPlaceholderText(QCoreApplication.translate("formLogin", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("formLogin", u"<html><head/><body><p><span style=\" font-weight:700;\">Inicio de sesi\u00f3n</span></p></body></html>", None))
        self.btn_login_acceder.setText(QCoreApplication.translate("formLogin", u"Acceder", None))
        self.login_mensaje_error.setText(QCoreApplication.translate("formLogin", u"mensaje", None))
        self.label.setText("")
        self.userDefault_label_2.setText(QCoreApplication.translate("formLogin", u"Usuario: invi", None))
        self.passwordDefault_label.setText(QCoreApplication.translate("formLogin", u"Password: 1234", None))
    # retranslateUi

