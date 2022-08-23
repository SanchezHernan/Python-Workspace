# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CargarVert.ui'
#
# Created: Sun Nov 05 15:08:32 2017
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

class Ui_DialogVert(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(470, 418)
        Dialog.setMinimumSize(QtCore.QSize(470, 418))
        Dialog.setMaximumSize(QtCore.QSize(470, 418))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/C:/Users/Blanc/Desktop/Band.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 401))
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
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineTel = QtGui.QLineEdit(self.layoutWidget)
        self.lineTel.setObjectName(_fromUtf8("lineTel"))
        self.gridLayout.addWidget(self.lineTel, 10, 1, 1, 1)
        self.lblTel = QtGui.QLabel(self.layoutWidget)
        self.lblTel.setObjectName(_fromUtf8("lblTel"))
        self.gridLayout.addWidget(self.lblTel, 10, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        
        
        
        
        self.lblCiud = QtGui.QLabel(self.layoutWidget)
        self.lblCiud.setObjectName(_fromUtf8("lblCiud"))
        self.gridLayout.addWidget(self.lblCiud, 2, 0, 1, 1)
        self.lineLat = QtGui.QLineEdit(self.layoutWidget)
        self.lineLat.setObjectName(_fromUtf8("lineLat"))
        self.gridLayout.addWidget(self.lineLat, 4, 1, 1, 1)
        self.lineDirec = QtGui.QLineEdit(self.layoutWidget)
        self.lineDirec.setObjectName(_fromUtf8("lineDirec"))
        self.gridLayout.addWidget(self.lineDirec, 8, 1, 1, 1)
        self.lblDirec = QtGui.QLabel(self.layoutWidget)
        self.lblDirec.setObjectName(_fromUtf8("lblDirec"))
        self.gridLayout.addWidget(self.lblDirec, 8, 0, 1, 1)
        self.lblLong = QtGui.QLabel(self.layoutWidget)
        self.lblLong.setObjectName(_fromUtf8("lblLong"))
        self.gridLayout.addWidget(self.lblLong, 6, 0, 1, 1)
        self.lineCiud = QtGui.QLineEdit(self.layoutWidget)
        self.lineCiud.setObjectName(_fromUtf8("lineCiud"))
        self.gridLayout.addWidget(self.lineCiud, 2, 1, 1, 1)
        self.lineID = QtGui.QLineEdit(self.layoutWidget)
        self.lineID.setObjectName(_fromUtf8("lineID"))
        self.gridLayout.addWidget(self.lineID, 0, 1, 1, 1)
        self.LblLat = QtGui.QLabel(self.layoutWidget)
        self.LblLat.setObjectName(_fromUtf8("LblLat"))
        self.gridLayout.addWidget(self.LblLat, 4, 0, 1, 1)
        self.lineLong = QtGui.QLineEdit(self.layoutWidget)
        self.lineLong.setObjectName(_fromUtf8("lineLong"))
        self.gridLayout.addWidget(self.lineLong, 6, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 7, 0, 1, 1)
        self.lblID = QtGui.QLabel(self.layoutWidget)
        self.lblID.setObjectName(_fromUtf8("lblID"))
        self.gridLayout.addWidget(self.lblID, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 9, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem6 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.BAgregarVert = QtGui.QPushButton(self.layoutWidget)
        self.BAgregarVert.setObjectName(_fromUtf8("BAgregarVert"))
        self.horizontalLayout.addWidget(self.BAgregarVert)
        self.BCancelar = QtGui.QPushButton(self.layoutWidget)
        self.BCancelar.setObjectName(_fromUtf8("BCancelar"))
        self.horizontalLayout.addWidget(self.BCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lblTel.setBuddy(self.lineTel)
        self.lblCiud.setBuddy(self.lineCiud)
        self.lblDirec.setBuddy(self.lineDirec)
        self.lblLong.setBuddy(self.lineLong)
        self.LblLat.setBuddy(self.lineLat)
        self.lblID.setBuddy(self.lineID)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineID, self.lineCiud)
        Dialog.setTabOrder(self.lineCiud, self.lineLat)
        Dialog.setTabOrder(self.lineLat, self.lineLong)
        Dialog.setTabOrder(self.lineLong, self.lineDirec)
        Dialog.setTabOrder(self.lineDirec, self.lineTel)
        Dialog.setTabOrder(self.lineTel, self.BAgregarVert)
        Dialog.setTabOrder(self.BAgregarVert, self.BCancelar)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Carga Ciudad", None))
        self.lblTitulo.setText(_translate("Dialog", "Cargar Ciudad", None))
        self.lblTel.setText(_translate("Dialog", "&Teléfono: ", None))
        self.lblCiud.setText(_translate("Dialog", "&Ciudad:", None))
        self.lblDirec.setText(_translate("Dialog", "&Dirección:", None))
        self.lblLong.setText(_translate("Dialog", "L&ongitud:", None))
        self.LblLat.setText(_translate("Dialog", "&Latitud:", None))
        self.lblID.setText(_translate("Dialog", "&ID Ciudad:", None))
        self.BAgregarVert.setText(_translate("Dialog", "Agregar Ciudad", None))
        self.BCancelar.setText(_translate("Dialog", "Cancelar", None))

"""import iconos_rc"""
