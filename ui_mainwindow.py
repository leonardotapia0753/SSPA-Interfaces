# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.widget_2)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.id_lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.origen_lineEdit = QLineEdit(self.widget_2)
        self.origen_lineEdit.setObjectName(u"origen_lineEdit")
        self.origen_lineEdit.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.origen_lineEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

        self.destino_lineEdit = QLineEdit(self.widget_2)
        self.destino_lineEdit.setObjectName(u"destino_lineEdit")
        self.destino_lineEdit.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.destino_lineEdit, 2, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.peso_spinBox = QSpinBox(self.widget_2)
        self.peso_spinBox.setObjectName(u"peso_spinBox")
        self.peso_spinBox.setTabletTracking(False)

        self.gridLayout_3.addWidget(self.peso_spinBox, 3, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.agregar_inicio_pushButton = QPushButton(self.widget)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")
        self.agregar_inicio_pushButton.setTabletTracking(False)

        self.verticalLayout_3.addWidget(self.agregar_inicio_pushButton)

        self.agregar_final_pushButton = QPushButton(self.widget)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")
        self.agregar_final_pushButton.setTabletTracking(False)

        self.verticalLayout_3.addWidget(self.agregar_final_pushButton)

        self.mostrar_pushButton = QPushButton(self.widget)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")
        self.mostrar_pushButton.setTabletTracking(False)

        self.verticalLayout_3.addWidget(self.mostrar_pushButton)


        self.verticalLayout_4.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.widget_3)

        self.salida = QPlainTextEdit(self.groupBox)
        self.salida.setObjectName(u"salida")
        self.salida.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.salida.sizePolicy().hasHeightForWidth())
        self.salida.setSizePolicy(sizePolicy1)
        self.salida.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.salida.setAcceptDrops(True)
        self.salida.setReadOnly(True)

        self.horizontalLayout.addWidget(self.salida)


        self.horizontalLayout_5.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Vuelo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"id:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Detino:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.salida.setPlainText("")
    # retranslateUi

