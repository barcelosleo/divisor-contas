# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/UI/ListarTipoContas.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListarTipoContas(object):
    def setupUi(self, ListarTipoContas):
        ListarTipoContas.setObjectName("ListarTipoContas")
        ListarTipoContas.resize(543, 343)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/svg/manager.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ListarTipoContas.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(ListarTipoContas)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.atualizar = QtWidgets.QPushButton(ListarTipoContas)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/svg/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atualizar.setIcon(icon1)
        self.atualizar.setObjectName("atualizar")
        self.horizontalLayout.addWidget(self.atualizar)
        self.adicionar = QtWidgets.QPushButton(ListarTipoContas)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/img/svg/add_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adicionar.setIcon(icon2)
        self.adicionar.setObjectName("adicionar")
        self.horizontalLayout.addWidget(self.adicionar)
        self.editarRegistro = QtWidgets.QPushButton(ListarTipoContas)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/img/svg/edit_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editarRegistro.setIcon(icon3)
        self.editarRegistro.setObjectName("editarRegistro")
        self.horizontalLayout.addWidget(self.editarRegistro)
        self.removerRegistro = QtWidgets.QPushButton(ListarTipoContas)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/img/svg/remove_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removerRegistro.setIcon(icon4)
        self.removerRegistro.setObjectName("removerRegistro")
        self.horizontalLayout.addWidget(self.removerRegistro)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tiposContas = QtWidgets.QTableWidget(ListarTipoContas)
        self.tiposContas.setObjectName("tiposContas")
        self.tiposContas.setColumnCount(3)
        self.tiposContas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tiposContas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tiposContas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tiposContas.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tiposContas)
        self.sair = QtWidgets.QPushButton(ListarTipoContas)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/img/svg/export.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon5)
        self.sair.setObjectName("sair")
        self.verticalLayout.addWidget(self.sair)

        self.retranslateUi(ListarTipoContas)
        QtCore.QMetaObject.connectSlotsByName(ListarTipoContas)

    def retranslateUi(self, ListarTipoContas):
        _translate = QtCore.QCoreApplication.translate
        ListarTipoContas.setWindowTitle(_translate("ListarTipoContas", "Lista de Tipos de Contas"))
        self.atualizar.setText(_translate("ListarTipoContas", "Atualizar"))
        self.adicionar.setText(_translate("ListarTipoContas", "Adicionar"))
        self.editarRegistro.setText(_translate("ListarTipoContas", "Editar"))
        self.removerRegistro.setText(_translate("ListarTipoContas", "Remover"))
        item = self.tiposContas.horizontalHeaderItem(0)
        item.setText(_translate("ListarTipoContas", "Id"))
        item = self.tiposContas.horizontalHeaderItem(1)
        item.setText(_translate("ListarTipoContas", "Nome"))
        item = self.tiposContas.horizontalHeaderItem(2)
        item.setText(_translate("ListarTipoContas", "Data de Inclusão"))
        self.sair.setText(_translate("ListarTipoContas", "Fechar"))


from . import ImageResources
