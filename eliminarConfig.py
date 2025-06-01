from eliminar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget,QListView,QTableView 
from conexionDB import Conexion

class Eliminar(Ui_MainWindow,QMainWindow):
      
      def __init__(self,categoria,usuario):
         QMainWindow.__init__(self)
         self.setupUi(self)
         self.label_userOn.setText(categoria+usuario)
         
         self.btn_eliminar.clicked.connect(self.__deleteBtn)
         self.btn_back_eliminar.clicked.connect(self.__backBtn_clicked)

         self.usuario = usuario
         self.categoria = categoria

      def __deleteBtn(self):
         self.con = Conexion().conexion() 
         self.cur = self.con.cursor()
         deleteUser = self.input_eliminar.text()

         selectQuery = selectQuery = """SELECT usuario, 'profesores' AS origen FROM profesores WHERE usuario = ? 
                                    UNION SELECT usuario, 'alumnos' AS origen FROM alumnos WHERE usuario = ? """
         self.cur.execute(selectQuery, (deleteUser,deleteUser, ))
         resultado = self.cur.fetchone()

         if resultado:
            confirm = self.showConfirmDialog("Confirmar eliminación", f"¿Estás seguro de que quieres eliminar al usuario {deleteUser}?")
            if confirm == QMessageBox.Yes:
                  usuario = resultado[0]
                  tabla_origen = resultado[1]
                  if tabla_origen == 'profesores':
                     deleteQuery = "DELETE FROM profesores WHERE usuario = ?"
                  elif tabla_origen == 'alumnos':
                     deleteQuery = "DELETE FROM alumnos WHERE usuario = ?"

                  self.cur.execute(deleteQuery, (usuario,))
                  self.con.commit()
                  self.showAlert("Eliminación exitosa", "El usuario ha sido eliminado.")
            else:
               self.showAlert("Eliminación cancelada", "La eliminación del usuario ha sido cancelada.")
         else:
            self.showAlert("Usuario no encontrado", "El usuario no existe en la base de datos.")
         self.cur.close()    

      def __backBtn_clicked(self):
         self.__backBtn(self.categoria,self.usuario)

      def __backBtn(self,categoria,usuario):
         from principalConfig import MainWindow
         self.main = MainWindow(categoria,usuario)
         self.main.show()
         self.close()
      def showAlert(self, title, message):  # Método showAlert agregado
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

      def showConfirmDialog(self, title, message): # Añadido método para mostrar el cuadro de diálogo de confirmación
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return msgBox.exec() # Devolver el resultado de la ejecución del cuadro de diálogo