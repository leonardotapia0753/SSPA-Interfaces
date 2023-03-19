from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from aeropuerto import Aeropuerto
from vuelo import Vuelo

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.aeropuerto = Aeropuerto()

        self.ui  = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)


    @Slot( )
    def action_Abrir_Archivo(self):
        #print("Abrir_Archivo")
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.aeropuerto.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo abrir el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo abrir el archivo " + ubicacion
            )

    @Slot( )
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.aeropuerto.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )

    @Slot( )
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen = self.ui.origen_lineEdit.text()
        destino = self.ui.destino_lineEdit.text()
        peso = self.ui.peso_spinBox.value()

        vuelo = Vuelo(id, origen, destino, peso)
        self.aeropuerto.agregar_inicio(vuelo)

    @Slot( )
    def click_agregar_final(self):
        id = self.ui.id_lineEdit.text()
        origen = self.ui.origen_lineEdit.text()
        destino = self.ui.destino_lineEdit.text()
        peso = self.ui.peso_spinBox.value()

        vuelo = Vuelo(id, origen, destino, peso)
        self.aeropuerto.agregar_final(vuelo)

    @Slot( )
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.aeropuerto))

