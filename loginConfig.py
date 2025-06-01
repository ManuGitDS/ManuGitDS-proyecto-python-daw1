from login import Ui_formLogin as log
from conexionDB import Conexion
from principalConfig import MainWindow
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget

import sys

class Login(QMainWindow,log,Conexion):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.userDefault_label_2.setText("Usuario: Invitado")
        # self.passwordDefault_label.setText()
        self.login_mensaje_error.setText("")# VAMOS POR MINUTOS 46:35 DEL VIDEO
        #self.input_login_usuario.connect(self.__inputUser)
        # self.input_login_password.connect(self.__inputPassword)
        self.btn_login_acceder.clicked.connect(self.__btnAcces) #asigna llamada a funcion al boton
        #self.login_mensaje_error.connect(self.__errorMessage)
    # def __errorMessage(self): 
        
    def __btnAcces(self):
        if len(self.input_login_usuario.text()) < 1:
            self.login_mensaje_error.setText("Ingrese un usuario válido")
            self.input_login_usuario.setFocus()
        elif len(self.input_login_password.text()) < 1: 
            self.login_mensaje_error.setText("Ingrese una contraseña válida")
            
            self.input_login_password.setFocus()
        else:
            nombre = self.input_login_usuario.text().lower()
            password = self.input_login_password.text()
            self.input_login_password.setText("")
            self.input_login_usuario.setText("")
            self.login_mensaje_error.setText("")
            self.consultaCredenciales(nombre,password)

    def consultaCredenciales(self,usuario,password):
            self.con = Conexion().conexion() #Establece la conexion
            self.cur = self.con.cursor() #Genera el cursor
            # Genera la consulta SQL
            query = """SELECT usuario, 'profesores' AS origen FROM profesores WHERE usuario = ? AND password = ? 
                 UNION SELECT usuario, 'alumnos' AS origen FROM alumnos WHERE usuario = ? AND password = ?""" #Genero la query
            
            # Ejecuta la consulta SQL
            self.cur.execute(query, (usuario, password,usuario, password))# Ejecuta la query y guardo el resultado
            resultado = self.cur.fetchone()# Guarda el valor del resultado (si no se ve algo asi <sqlite3.Cursor object at 0x000002A5FC58E840>)
            self.cur.close()

            if resultado:
                if resultado[1]=='profesores':
                    categoria = "Profesor: "
                else:
                    categoria = "Alumno: "
                self.main = MainWindow(categoria,usuario) #Llama la ventana que quiero abrir
                self.main.show() # muestra la ventana
                self.close() # cierra la ventana

            else: 
                self.login_mensaje_error.setText("Usuario o Contraseña incorrecta")
            
#programa principal
if __name__ == "__main__":
    #inicio de la aplicacion grafica
    app = QApplication(sys.argv)
    v = Login()  
    sys.exit(app.exec())