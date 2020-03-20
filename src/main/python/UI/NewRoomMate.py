# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/UI/NewRoomMate.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewRoomMate(object):
    def setupUi(self, NewRoomMate):
        NewRoomMate.setObjectName("NewRoomMate")
        NewRoomMate.resize(400, 101)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/svg/businessman.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewRoomMate.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(NewRoomMate)
        self.gridLayout.setObjectName("gridLayout")
        self.salvarMorador = QtWidgets.QPushButton(NewRoomMate)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/svg/checkmark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salvarMorador.setIcon(icon1)
        self.salvarMorador.setObjectName("salvarMorador")
        self.gridLayout.addWidget(self.salvarMorador, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(NewRoomMate)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cancelarNovoMorador = QtWidgets.QPushButton(NewRoomMate)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/img/svg/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelarNovoMorador.setIcon(icon2)
        self.cancelarNovoMorador.setObjectName("cancelarNovoMorador")
        self.gridLayout.addWidget(self.cancelarNovoMorador, 1, 2, 1, 1)
        self.nomeMorador = QtWidgets.QLineEdit(NewRoomMate)
        self.nomeMorador.setObjectName("nomeMorador")
        self.gridLayout.addWidget(self.nomeMorador, 0, 1, 1, 2)

        self.retranslateUi(NewRoomMate)
        QtCore.QMetaObject.connectSlotsByName(NewRoomMate)

    def retranslateUi(self, NewRoomMate):
        _translate = QtCore.QCoreApplication.translate
        NewRoomMate.setWindowTitle(_translate("NewRoomMate", "Novo Morador"))
        self.salvarMorador.setText(_translate("NewRoomMate", "Salvar"))
        self.label.setText(_translate("NewRoomMate", "Nome"))
        self.cancelarNovoMorador.setText(_translate("NewRoomMate", "Cancelar"))


from . import ImageResources
