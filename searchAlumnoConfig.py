from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit,QHeaderView, QLabel, QMainWindow, QWidget,QListView,QTableView 
from searchAlumno import Ui_SearchAlumnoWindow
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtCore import QStringListModel
from conexionDB import Conexion

class SearchAlumnoWindow(Ui_SearchAlumnoWindow,QMainWindow,Conexion):
    def __init__(self,categoria,usuario):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.label_userOn.setText(categoria + usuario)
        self.usuario = usuario
        self.categoria = categoria
        
        self.btn_back_alumno_search.clicked.connect(self.__back_clicked)
        self.input_search_alumno.text()
        self.btn_search_alumno.clicked.connect(self.__searchAlumno)
        self.btn_listarAlumno.clicked.connect(self.__searchAllAlumno)
    

    def __searchAlumno(self):
        nombre = self.input_search_alumno.text()
        nombre = nombre.lower()
        self.con = Conexion().conexion() #Establece la conexion
        self.cur = self.con.cursor() #Genera el cursor
        # Genera la consulta SQL
        query = "SELECT nombre,primer_apellido,segundo_apellido,usuario,password FROM alumnos WHERE LOWER(nombre) = ? OR LOWER(primer_apellido) = ? OR LOWER(segundo_apellido) = ?"
        consutla = self.cur.execute(query,(nombre,nombre,nombre,))
        resultado = consutla.fetchall()
        listado = []
        for row in resultado:
            if row[0].lower() == nombre or row[1].lower() == nombre or row[2].lower() == nombre:
                listado.append(row)

        if len(listado) > 0 :
            self.tabla = QStandardItemModel()# Configurar el modelo para el QTableView
            self.tabla.clear()# Limpiar cualquier contenido previo en el modelo
            self.tabla.setHorizontalHeaderLabels(["Nombre", "Primer Apellido", "Segundo Apellido","ID Usuario","Password"])
            self.search_listView_alumno.setModel(self.tabla)# Asignar el modelo a la QTableView
            self.search_listView_alumno.verticalHeader().hide()
            # Ajustar el modo de redimensionamiento de las secciones
            self.search_listView_alumno.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
            self.search_listView_alumno.horizontalHeader().setStretchLastSection(True)
            self.search_listView_alumno.setColumnWidth(0, 170)
            self.search_listView_alumno.setColumnWidth(1, 170)
            self.search_listView_alumno.setColumnWidth(2, 170)
            self.search_listView_alumno.setColumnWidth(3, 100)
            self.search_listView_alumno.setColumnWidth(4, 100)

            for row in listado:
                row_items = [QStandardItem(str(item)) for item in row]
                self.tabla.appendRow(row_items)


        else:
            msg = QStringListModel(["Sin resultados"])
            self.search_listView_alumno.setModel(msg)
        self.input_search_alumno.setText("")
        self.cur.close()
    def __searchAllAlumno(self):
        self.con = Conexion().conexion() 
        self.cur = self.con.cursor() 
        query = self.cur.execute("SELECT nombre,primer_apellido,segundo_apellido,usuario,password FROM alumnos").fetchall()   #Genero la query
       
        self.tabla = QStandardItemModel()# Configurar el modelo para el QTableView
        self.tabla.clear()# Limpiar cualquier contenido previo en el modelo
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Primer Apellido", "Segundo Apellido","ID Usuario","Password"])
        self.search_listView_alumno.setModel(self.tabla)# Asignar el modelo a la QTableView
        self.search_listView_alumno.verticalHeader().hide()# Esconde el índice vertical de las lineas
        self.search_listView_alumno.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.search_listView_alumno.horizontalHeader().setStretchLastSection(True)
        self.search_listView_alumno.setColumnWidth(0, 170)
        self.search_listView_alumno.setColumnWidth(1, 170)
        self.search_listView_alumno.setColumnWidth(2, 170)
        self.search_listView_alumno.setColumnWidth(3, 100)
        self.search_listView_alumno.setColumnWidth(4, 100)

        for row in query:
            row_items = [QStandardItem(str(item)) for item in row]
            self.tabla.appendRow(row_items)
        self.cur.close()
        
         

    def __back_clicked(self):
        self.__back(self.categoria,self.usuario)
        
    def __back(self,categoria,usuario):
        from principalConfig import MainWindow
        self.main = MainWindow(categoria,usuario) #Llama la ventana que quiero abrir
        self.main.show() # muestra la ventana
        self.close()



       

