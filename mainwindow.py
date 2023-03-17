from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self): # Reservar memoria para mostrar ventana
        super(MainWindow, self).__init__() # Llama al constructor de QMainWindow para reservar memoria
        # Lo anterior es una clase hija
        ui = Ui_MainWindow()
        ui.setupUi(self)

        ui.pushButton.clicked.connect(self.click_agregar)

    @Slot( )
    def click_agregar(self):
        print("click")
