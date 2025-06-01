from principal import Ui_MainWindow 
from searchProfesorConfig import SearchprofesorWindow
from eliminarConfig import Eliminar
from searchAlumnoConfig import SearchAlumnoWindow
from addProfesorConfig import AddProfWindow
from addAlumnoConfig import AddAlumnoWindow
from matriculaConfig import Matriculas
from cursosConfig import Cursos
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget


class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,categoria,usuario):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.btn_searchProfesor.clicked.connect(self.__searchProfesor_clicked)
        self.btn_searchAlumno.clicked.connect(self.__searchAlumno_clicked)
        self.btn_addAlumno.clicked.connect(self.__addAlumno_clicked)
        self.btn_addProfesor.clicked.connect(self.__addProfesor_clicked)
        self.btn_eliminar.clicked.connect(self.__delete_clicked)
        self.btn_changeUser.clicked.connect(self.__changeUser)
        self.btn_matriculas.clicked.connect(self.__matriculas_clicked)
        self.btn_materias.clicked.connect(self.__materias_clicked)
        
        self.label_userOn.setText(categoria + usuario)
        self.usuario = usuario
        self.categoria = categoria



    def __matriculas_clicked(self):
            self.__matriculas(self.categoria,self.usuario)
            
    def __matriculas(self,categoria,usuario):
        self.main = Matriculas(categoria,usuario) 
        self.main.show() 
        self.close() 

    def __materias_clicked(self):
            self.__materias(self.categoria,self.usuario)
            
    def __materias(self,categoria,usuario):
        self.main = Cursos(categoria,usuario) 
        self.main.show() 
        self.close() 




    def __changeUser(self):
         from loginConfig import Login
         self.main = Login()
         self.main.show()
         self.close()

    def __delete_clicked(self):
            self.__delete(self.categoria,self.usuario)
            
    def __delete(self,categoria,usuario):
        self.main = Eliminar(categoria,usuario) 
        self.main.show() 
        self.close() 

    def __searchProfesor_clicked(self):
         self.__searchProfesor(self.categoria,self.usuario)

    def __searchProfesor(self,categoria,usuario):
        self.main = SearchprofesorWindow(categoria,usuario) #Llamo la ventana que quiero abrir
        self.main.show() # digo que la muestre
        self.close() # y aqui que la esconda

    def __searchAlumno_clicked(self):
        self.__searchAlumno(self.categoria,self.usuario)  

    def __searchAlumno(self,categoria,usuario):
        self.main = SearchAlumnoWindow(categoria,usuario) 
        self.main.show() 
        self.close() 

    def __addProfesor_clicked(self):
        self.__addProfesor(self.categoria,self.usuario) 

    def __addProfesor(self,categoria,usuario):
            self.main = AddProfWindow(categoria,usuario) 
            self.main.show() 
            self.close() 

    def __addAlumno_clicked(self):
        self.__addAlumno(self.categoria,self.usuario) 

    def __addAlumno(self,categoria,usuario):
        self.main = AddAlumnoWindow(categoria,usuario) 
        self.main.show() 
        self.close()
    
       
       