from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget,QListView,QTableView 
from addAlumno import Ui_addAlumnoWindow
from conexionDB import Conexion

class AddAlumnoWindow(Ui_addAlumnoWindow,QMainWindow,Conexion):
    def __init__(self,categoria,usuario):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.btn_back_alumno_add.clicked.connect(self.__back_clicked)
        self.btn_confirm_alumno.clicked.connect(self.__insert)
        self.addErrorMsgAlumno.setText("")

        self.label_userOn.setText(categoria + usuario)
        self.usuario = usuario
        self.categoria = categoria
       

    def __insert(self):
        nombre = self.input_alumnoAddName.text()
        primerApellido = self.input_alumnoAddFirstName.text()
        segundoApellido = self.input_alumnoAddSecondName.text()
        usuario = self.input_alumnoAddUserID.text()
        password = self.input_alumnoAddPassword.text()
        confirmPass = self.input_alumnoAddConfirmPassword.text()
        self.con = Conexion().conexion() 
        self.cur = self.con.cursor() 

        if not (nombre and primerApellido and segundoApellido and usuario and password and confirmPass):
            self.addErrorMsgAlumno.setText("Todos los campos son obligatorios")
        else:
            querySelect = "SELECT 1 FROM alumnos WHERE usuario = ?"
            consulta2 = self.cur.execute(querySelect, (usuario,))
            resultado2 = consulta2.fetchone()
            if resultado2:
                self.addErrorMsgAlumno.setText("El usuario ya existe, prueba otro nombre de usuario")
            else:     
                if password == confirmPass:
                    query = "INSERT INTO alumnos VALUES (NULL,?,?,?,?,?)"
                    self.cur.execute(query, (nombre,primerApellido,segundoApellido,usuario,password))
                    self.con.commit()
                    if self.cur.rowcount > 0:
                        self.addErrorMsgAlumno.setText("Alumno añadido correctamente")
                    else:
                        self.addErrorMsgAlumno.setText("Hubo un problema al añadir el alumno")
                else:
                    self.addErrorMsgAlumno.setText("Las contraseñas no coinciden")
        self.cur.close()
    def __back_clicked(self):
        self.__back(self.categoria,self.usuario)

    def __back(self,categoria,usuario):
        from principalConfig import MainWindow
        self.main = MainWindow(categoria,usuario) #Llama la ventana que quiero abrir
        self.main.show() # muestra la ventana
        self.close()

        
    
