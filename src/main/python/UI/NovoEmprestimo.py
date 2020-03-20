# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/UI/NovoEmprestimo.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NovoEmprestimo(object):
    def setupUi(self, NovoEmprestimo):
        NovoEmprestimo.setObjectName("NovoEmprestimo")
        NovoEmprestimo.resize(400, 162)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/svg/money_transfer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NovoEmprestimo.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(NovoEmprestimo)
        self.gridLayout.setObjectName("gridLayout")
        self.cancelar = QtWidgets.QPushButton(NovoEmprestimo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/svg/cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon1)
        self.cancelar.setObjectName("cancelar")
        self.gridLayout.addWidget(self.cancelar, 4, 2, 1, 1)
        self.de = QtWidgets.QComboBox(NovoEmprestimo)
        self.de.setObjectName("de")
        self.gridLayout.addWidget(self.de, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(NovoEmprestimo)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(NovoEmprestimo)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(NovoEmprestimo)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.para = QtWidgets.QComboBox(NovoEmprestimo)
        self.para.setObjectName("para")
        self.gridLayout.addWidget(self.para, 2, 1, 1, 2)
        self.salvar = QtWidgets.QPushButton(NovoEmprestimo)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/img/svg/checkmark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salvar.setIcon(icon2)
        self.salvar.setObjectName("salvar")
        self.gridLayout.addWidget(self.salvar, 4, 1, 1, 1)
        self.valor = QtWidgets.QLineEdit(NovoEmprestimo)
        self.valor.setObjectName("valor")
        self.gridLayout.addWidget(self.valor, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(NovoEmprestimo)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.descricao = QtWidgets.QLineEdit(NovoEmprestimo)
        self.descricao.setObjectName("descricao")
        self.gridLayout.addWidget(self.descricao, 0, 1, 1, 2)

        self.retranslateUi(NovoEmprestimo)
        QtCore.QMetaObject.connectSlotsByName(NovoEmprestimo)

    def retranslateUi(self, NovoEmprestimo):
        _translate = QtCore.QCoreApplication.translate
        NovoEmprestimo.setWindowTitle(_translate("NovoEmprestimo", "Novo Empréstimo"))
        self.cancelar.setText(_translate("NovoEmprestimo", "Cancelar"))
        self.label_3.setText(_translate("NovoEmprestimo", "Para"))
        self.label.setText(_translate("NovoEmprestimo", "Valor"))
        self.label_2.setText(_translate("NovoEmprestimo", "De"))
        self.salvar.setText(_translate("NovoEmprestimo", "Salvar"))
        self.valor.setInputMask(_translate("NovoEmprestimo", "R\\$9999,99"))
        self.label_4.setText(_translate("NovoEmprestimo", "Descrição"))


from . import ImageResources
