from PySide6.QtWidgets import QApplication,QHeaderView, QMessageBox, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget,QListView,QTableView 
from conexionDB import Conexion
from matricula import Ui_matricula_MainWindow
from PySide6.QtGui import QStandardItemModel,QStandardItem
from PySide6.QtCore import QStringListModel

class Matriculas(Ui_matricula_MainWindow,QMainWindow):
    def __init__(self,categoria,usuario):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.label_userOn.setText(categoria+usuario)
        self.btn_back_matriculas.clicked.connect(self.__backBtn_clicked)
        self.__cargarDatos()
        self.usuario = usuario
        self.categoria = categoria

    def __cargarDatos(self):
        self.con = Conexion().conexion() 
        self.cur = self.con.cursor() 
        query = "SELECT * FROM inscripciones"
        consutla = self.cur.execute(query)
        resultado = consutla.fetchall()

        self.tabla = QStandardItemModel()# Configurar el modelo para el QTableView
        self.tabla.clear()# Limpiar cualquier contenido previo en el modelo
        self.tabla.setHorizontalHeaderLabels(["ID_inscripcion", "ID_alumno", "ID_Curso","Fecha Inscripcion"])
        self.search_listView_matricula.setModel(self.tabla)# Asignar el modelo a la QTableView
        self.search_listView_matricula.verticalHeader().hide()
        # Ajustar el modo de redimensionamiento de las secciones
        self.search_listView_matricula.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.search_listView_matricula.horizontalHeader().setStretchLastSection(True)
        self.search_listView_matricula.setColumnWidth(0, 170)
        self.search_listView_matricula.setColumnWidth(1, 170)
        self.search_listView_matricula.setColumnWidth(2, 170)
        self.search_listView_matricula.setColumnWidth(3, 100)
        self.search_listView_matricula.setColumnWidth(4, 100)
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