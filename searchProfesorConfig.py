from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit,QTableWidget, QHeaderView, QLabel, QMainWindow, QWidget,QListView,QTableView 
from searchProfesor import Ui_SearchProfWindow
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtCore import QStringListModel
from conexionDB import Conexion

class SearchprofesorWindow(Ui_SearchProfWindow,QMainWindow,Conexion):
    def __init__(self,categoria,usuario):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.label_userOn.setText(categoria+usuario)
        self.usuario = usuario
        self.categoria = categoria
        
        self.btn_back_alumno_search.clicked.connect(self.__back_clicked)
        self.input_search_profesor.text()
        self.btn_search_profesor.clicked.connect(self.__searchprofesor)
        self.btn_listarProfesor.clicked.connect(self.__searchAllprofesor)
    
        
        


    def __searchprofesor(self):
        nombre = self.input_search_profesor.text()
        nombre = nombre.lower()
        self.con = Conexion().conexion() #Establece la conexion
        self.cur = self.con.cursor() #Genera el cursor
        # Genera la consulta SQL
        query = "SELECT nombre,primer_apellido,segundo_apellido,usuario,password FROM profesores WHERE LOWER(nombre) = ? OR LOWER(primer_apellido) = ? OR LOWER(segundo_apellido) = ?"
        consutla = self.cur.execute(query,(nombre,nombre,nombre,))
        resultado = consutla.fetchall()
        listado = []
        for row in resultado:
            print(row)
            if row[0].lower() == nombre or row[1].lower() == nombre or row[2].lower() == nombre:
                listado.append(row)

        if len(listado) > 0 :
            self.tabla = QStandardItemModel()# Configurar el modelo para el QTableView
            self.tabla.clear()# Limpiar cualquier contenido previo en el modelo
            self.tabla.setHorizontalHeaderLabels(["Nombre", "Primer Apellido", "Segundo Apellido","ID Usuario","Password"])
            self.search_listView_profesor_2.setModel(self.tabla)# Asignar el modelo a la QTableView
            self.search_listView_profesor_2.verticalHeader().hide()
            # Ajustar el modo de redimensionamiento de las secciones
            self.search_listView_profesor_2.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
            self.search_listView_profesor_2.horizontalHeader().setStretchLastSection(True)
            self.search_listView_profesor_2.setColumnWidth(0, 170)
            self.search_listView_profesor_2.setColumnWidth(1, 170)
            self.search_listView_profesor_2.setColumnWidth(2, 170)
            self.search_listView_profesor_2.setColumnWidth(3, 100)
            self.search_listView_profesor_2.setColumnWidth(4, 100)

            # Iterar sobre los datos de query y agregarlos al modelo
            for row in listado:
                row_items = [QStandardItem(str(item)) for item in row]
                self.tabla.appendRow(row_items)


        else:
            msg = QStringListModel(["Sin resultados"])
            self.search_listView_profesor_2.setModel(msg)
        self.input_search_profesor.setText("")
        self.cur.close()
    def __searchAllprofesor(self):
        self.con = Conexion().conexion() 
        self.cur = self.con.cursor() 
        query = self.cur.execute("SELECT nombre,primer_apellido,segundo_apellido,usuario,password FROM profesores").fetchall()   #Genero la query

        self.tabla = QStandardItemModel()# Configurar el modelo para el QTableView
        self.tabla.clear()# Limpiar cualquier contenido previo en el modelo
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Primer Apellido", "Segundo Apellido","ID Usuario","Password"])
        self.search_listView_profesor_2.setModel(self.tabla)# Asignar el modelo a la QTableView
        self.search_listView_profesor_2.verticalHeader().hide()# Esconde el índice vertical de las lineas
        # Ajustar el modo de redimensionamiento de las secciones
        self.search_listView_profesor_2.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.search_listView_profesor_2.horizontalHeader().setStretchLastSection(True)
        self.search_listView_profesor_2.setColumnWidth(0, 170)
        self.search_listView_profesor_2.setColumnWidth(1, 170)
        self.search_listView_profesor_2.setColumnWidth(2, 170)
        self.search_listView_profesor_2.setColumnWidth(3, 100)
        self.search_listView_profesor_2.setColumnWidth(4, 100)

        # Itera sobre los datos de query y agregarlos al modelo
        for row in query:
            row_items = [QStandardItem(str(item)) for item in row]
            self.tabla.appendRow(row_items)
        self.cur.close()

        '''tabla = QTableWidget()
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)'''

        '''listaprofesor = []
        for linea in query:
            listaprofesor.append(" ".join(map(str,linea)))# " ".join convierte la lista en un string separados por espacios
            #map recorre cada elemento de la lista y le agrega la funcion str a cada uno de ellos
        modelo = QStringListModel(listaprofesor)
        self.search_listView_profesor.setModel(modelo)'''
    
        
         

    def __back_clicked(self):
        self.__back(self.categoria,self.usuario)
        
    def __back(self,categoria,usuario):
        from principalConfig import MainWindow
        self.main = MainWindow(categoria,usuario) #Llama la ventana que quiero abrir
        self.main.show() # muestra la ventana
        self.close()

       

