# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/UI/NovaConta.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NovaConta(object):
    def setupUi(self, NovaConta):
        NovaConta.setObjectName("NovaConta")
        NovaConta.resize(400, 162)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/svg/money_transfer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NovaConta.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(NovaConta)
        self.gridLayout.setObjectName("gridLayout")
        self.valor = QtWidgets.QLineEdit(NovaConta)
        self.valor.setObjectName("valor")
        self.gridLayout.addWidget(self.valor, 3, 1, 1, 2)
        self.tipoConta = QtWidgets.QComboBox(NovaConta)
        self.tipoConta.setObjectName("tipoConta")
        self.gridLayout.addWidget(self.tipoConta, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(NovaConta)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pagante = QtWidgets.QComboBox(NovaConta)
        self.pagante.setObjectName("pagante")
        self.gridLayout.addWidget(self.pagante, 2, 1, 1, 2)
        self.cancelar = QtWidgets.QPushButton(NovaConta)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/svg/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon1)
        self.cancelar.setObjectName("cancelar")
        self.gridLayout.addWidget(self.cancelar, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(NovaConta)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.salvar = QtWidgets.QPushButton(NovaConta)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/img/svg/checkmark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salvar.setIcon(icon2)
        self.salvar.setObjectName("salvar")
        self.gridLayout.addWidget(self.salvar, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(NovaConta)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(NovaConta)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.descricao = QtWidgets.QLineEdit(NovaConta)
        self.descricao.setObjectName("descricao")
        self.gridLayout.addWidget(self.descricao, 1, 1, 1, 2)

        self.retranslateUi(NovaConta)
        QtCore.QMetaObject.connectSlotsByName(NovaConta)

    def retranslateUi(self, NovaConta):
        _translate = QtCore.QCoreApplication.translate
        NovaConta.setWindowTitle(_translate("NovaConta", "Nova Conta"))
        self.valor.setInputMask(_translate("NovaConta", "R\\$9999,99"))
        self.label_3.setText(_translate("NovaConta", "Pagante"))
        self.cancelar.setText(_translate("NovaConta", "Cancelar"))
        self.label.setText(_translate("NovaConta", "Valor"))
        self.salvar.setText(_translate("NovaConta", "Salvar"))
        self.label_2.setText(_translate("NovaConta", "Tipo de Conta"))
        self.label_4.setText(_translate("NovaConta", "Descrição"))


from . import ImageResources
