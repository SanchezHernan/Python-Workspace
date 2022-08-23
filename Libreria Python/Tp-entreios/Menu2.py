# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu2.ui'
#
# Created: Sun Nov 05 20:55:04 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(639, 432)
        MainWindow.setMinimumSize(QtCore.QSize(639, 432))
        MainWindow.setMaximumSize(QtCore.QSize(639, 432))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 401))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblTitulo = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Perpetua Titling MT"))
        font.setPointSize(15)
        font.setItalic(True)
        font.setUnderline(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setObjectName(_fromUtf8("lblTitulo"))
        self.verticalLayout.addWidget(self.lblTitulo)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea = QtGui.QScrollArea(self.layoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 617, 284))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.Lista = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.Lista.setGeometry(QtCore.QRect(0, 0, 621, 281))
        self.Lista.setObjectName(_fromUtf8("Lista"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.BAgVert = QtGui.QPushButton(self.layoutWidget)
        self.BAgVert.setObjectName(_fromUtf8("BAgVert"))
        self.horizontalLayout.addWidget(self.BAgVert)
        self.BAgArista = QtGui.QPushButton(self.layoutWidget)
        self.BAgArista.setObjectName(_fromUtf8("BAgArista"))
        self.horizontalLayout.addWidget(self.BAgArista)
        self.BVerMapa = QtGui.QPushButton(self.layoutWidget)
        self.BVerMapa.setObjectName(_fromUtf8("BVerMapa"))
        self.horizontalLayout.addWidget(self.BVerMapa)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Principal", None))
        self.lblTitulo.setText(_translate("MainWindow", "Mapa de ciudades de Entre Ríos", None))
        self.BAgVert.setText(_translate("MainWindow", "Agregar Ciudad", None))
        self.BAgArista.setText(_translate("MainWindow", "Agregar Arista", None))
        self.BVerMapa.setText(_translate("MainWindow", "Ver Mapa", None))

