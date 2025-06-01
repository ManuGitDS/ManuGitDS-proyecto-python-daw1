from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget,QListView,QTableView 
from addProfesor import Ui_addProfWindow
from conexionDB import Conexion

class AddProfWindow(Ui_addProfWindow,QMainWindow,Conexion):
    def __init__(self,categoria,usuario):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.btn_back_profesor_add.clicked.connect(self.__back_clicked)
        self.btn_confirm_profesor.clicked.connect(self.__insert)
        self.addErrorMsgProf.setText("")

        self.label_userOn.setText(categoria + usuario)
        self.usuario = usuario
        self.categoria = categoria

       

    def __insert(self):
        nombre = self.input_profAddName.text()
        primerApellido = self.input_profAddFirstName.text()
        segundoApellido = self.input_profAddSecondName.text()
        usuario = self.input_profAddUserID.text()
        password = self.input_profAddPassword.text()
        confirmPass = self.input_profAddConfirmPassword.text()
        self.con = Conexion().conexion() 
        self.cur = self.con.cursor() 

        if not (nombre and primerApellido and segundoApellido and usuario and password and confirmPass):
            self.addErrorMsgProf.setText("Todos los campos son obligatorios")
        else:
            querySelect = "SELECT 1 FROM profesores WHERE usuario = ?"
            consulta2 = self.cur.execute(querySelect, (usuario,))
            resultado2 = consulta2.fetchone()
            if resultado2:
                self.addErrorMsgProf.setText("El usuario ya existe, prueba otro nombre de usuario")
            else:     
                if password == confirmPass:
                    query = "INSERT INTO profesores VALUES (NULL,?,?,?,?,?)"
                    self.cur.execute(query, (nombre,primerApellido,segundoApellido,usuario,password))
                    self.con.commit()
                    if self.cur.rowcount > 0:
                        self.addErrorMsgProf.setText("Profesor añadido correctamente")
                    else:
                        self.addErrorMsgProf.setText("Hubo un problema al añadir el profesor")
                else:
                    self.addErrorMsgProf.setText("Las contraseñas no coinciden")
        self.cur.close()
    def __back_clicked(self):
        self.__back(self.categoria,self.usuario)

    def __back(self,categoria,usuario):
        from principalConfig import MainWindow
        self.main = MainWindow(categoria,usuario) #Llama la ventana que quiero abrir
        self.main.show() # muestra la ventana
        self.close()