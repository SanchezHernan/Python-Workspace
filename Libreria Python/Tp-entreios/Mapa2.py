# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mapa2.ui'
#
# Created: Sat Nov 04 23:03:38 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, uic

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

class Ui_Mapa2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(699, 590)
        Dialog.setMinimumSize(QtCore.QSize(699, 590))
        Dialog.setMaximumSize(QtCore.QSize(699, 590))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Blanc/Desktop/Band.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 0, 681, 581))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblTitulo = QtGui.QLabel(self.widget)
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
        self.webView = QtWebKit.QWebView(self.widget)
        self.webView.setMinimumSize(QtCore.QSize(679, 468))
        self.webView.setMaximumSize(QtCore.QSize(679, 468))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.webView)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.BCerrar = QtGui.QPushButton(self.widget)
        self.BCerrar.setObjectName(_fromUtf8("BCerrar"))
        self.verticalLayout.addWidget(self.BCerrar)
        """size = "&size=679x468"
        zoom = "&zoom=7"
        center = "center=Villa Dominguez Entre Rios"
        imgformat = "&format=png"
        maptype="&maptype=roadmap"
        sensor = "&sensor=false"
        self.webView.load(QtCore.QUrl("https://maps.googleapis.com/maps/api/staticmap?"+center+size+zoom+imgformat+maptype+sensor))
        print("https://maps.googleapis.com/maps/api/staticmap?"+center+size+zoom+imgformat+maptype+sensor)
        """    
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Rutas", None))
        self.lblTitulo.setText(_translate("Dialog", "Ruta de Ciudades", None))
        self.BCerrar.setText(_translate("Dialog", "Cerrar", None))
        
    

from PyQt4 import QtWebKit
