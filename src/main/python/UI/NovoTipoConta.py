# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/UI/NovoTipoConta.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NovoTipoConta(object):
    def setupUi(self, NovoTipoConta):
        NovoTipoConta.setObjectName("NovoTipoConta")
        NovoTipoConta.resize(400, 91)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/svg/money_transfer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NovoTipoConta.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(NovoTipoConta)
        self.gridLayout.setObjectName("gridLayout")
        self.salvar = QtWidgets.QPushButton(NovoTipoConta)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/svg/checkmark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salvar.setIcon(icon1)
        self.salvar.setObjectName("salvar")
        self.gridLayout.addWidget(self.salvar, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(NovoTipoConta)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cancelar = QtWidgets.QPushButton(NovoTipoConta)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/img/svg/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon2)
        self.cancelar.setObjectName("cancelar")
        self.gridLayout.addWidget(self.cancelar, 1, 2, 1, 1)
        self.nomeTipoConta = QtWidgets.QLineEdit(NovoTipoConta)
        self.nomeTipoConta.setObjectName("nomeTipoConta")
        self.gridLayout.addWidget(self.nomeTipoConta, 0, 1, 1, 2)

        self.retranslateUi(NovoTipoConta)
        QtCore.QMetaObject.connectSlotsByName(NovoTipoConta)

    def retranslateUi(self, NovoTipoConta):
        _translate = QtCore.QCoreApplication.translate
        NovoTipoConta.setWindowTitle(_translate("NovoTipoConta", "Novo Tipo de Conta"))
        self.salvar.setText(_translate("NovoTipoConta", "Salvar"))
        self.label.setText(_translate("NovoTipoConta", "Nome"))
        self.cancelar.setText(_translate("NovoTipoConta", "Cancelar"))


from . import ImageResources
