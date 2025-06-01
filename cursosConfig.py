from PySide6.QtWidgets import QApplication, QHeaderView,QMessageBox, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget,QListView,QTableView 
from conexionDB import Conexion
from cursos import Ui_MainWindow
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtCore import QStringListModel


class Cursos(Ui_MainWindow,QMainWindow):
     def __init__(self,categoria,usuario):
          QMainWindow.__init__(self)
          self.setupUi(self)
          self.label_userOn.setText(categoria+usuario)
          self.btn_back_cursos.clicked.connect(self.__backBtn_clicked)
          self.__cargarDatos()
          self.usuario = usuario
          self.categoria = categoria


     def __cargarDatos(self):
        self.con = Conexion().conexion() 
        self.cur = self.con.cursor() 
        query = "SELECT * FROM cursos"
        consutla = self.cur.execute(query)
        resultado = consutla.fetchall()

        self.tabla = QStandardItemModel()# Configurar el modelo para el QTableView
        self.tabla.clear()# Limpiar cualquier contenido previo en el modelo
        self.tabla.setHorizontalHeaderLabels(["ID_Curso", "Nombre curso", "Descripcion","ID_Profesor"])
        self.search_listView_cursos.setModel(self.tabla)# Asignar el modelo a la QTableView
        self.search_listView_cursos.verticalHeader().hide()
        # Ajustar el modo de redimensionamiento de las secciones
        self.search_listView_cursos.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.search_listView_cursos.horizontalHeader().setStretchLastSection(True)
        self.search_listView_cursos.setColumnWidth(0, 170)
        self.search_listView_cursos.setColumnWidth(1, 170)
        self.search_listView_cursos.setColumnWidth(2, 170)
        self.search_listView_cursos.setColumnWidth(3, 100)
        self.search_listView_cursos.setColumnWidth(4, 100)
        listado = []
        for row in resultado:
            listado.append(row)
            
        for row in listado:
                row_items = [QStandardItem(str(item)) for item in row]
                self.tabla.appendRow(row_items)

     def __backBtn_clicked(self):
         self.__backBtn(self.categoria,self.usuario)

     def __backBtn(self,categoria,usuario):
        from principalConfig import MainWindow
        self.main = MainWindow(categoria,usuario)
        self.main.show()
        self.close()