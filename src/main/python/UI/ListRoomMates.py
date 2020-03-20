# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/UI/ListRoomMates.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListRoomMates(object):
    def setupUi(self, ListRoomMates):
        ListRoomMates.setObjectName("ListRoomMates")
        ListRoomMates.resize(543, 343)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/svg/manager.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ListRoomMates.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(ListRoomMates)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.atualizar = QtWidgets.QPushButton(ListRoomMates)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/svg/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atualizar.setIcon(icon1)
        self.atualizar.setObjectName("atualizar")
        self.horizontalLayout.addWidget(self.atualizar)
        self.adicionarRegistro = QtWidgets.QPushButton(ListRoomMates)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/img/svg/add_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adicionarRegistro.setIcon(icon2)
        self.adicionarRegistro.setObjectName("adicionarRegistro")
        self.horizontalLayout.addWidget(self.adicionarRegistro)
        self.editarRegistro = QtWidgets.QPushButton(ListRoomMates)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/img/svg/edit_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editarRegistro.setIcon(icon3)
        self.editarRegistro.setObjectName("editarRegistro")
        self.horizontalLayout.addWidget(self.editarRegistro)
        self.removerRegistro = QtWidgets.QPushButton(ListRoomMates)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/img/svg/remove_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removerRegistro.setIcon(icon4)
        self.removerRegistro.setObjectName("removerRegistro")
        self.horizontalLayout.addWidget(self.removerRegistro)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.moradores = QtWidgets.QTableWidget(ListRoomMates)
        self.moradores.setObjectName("moradores")
        self.moradores.setColumnCount(3)
        self.moradores.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.moradores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.moradores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.moradores.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.moradores)
        self.sair = QtWidgets.QPushButton(ListRoomMates)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/img/svg/export.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon5)
        self.sair.setObjectName("sair")
        self.verticalLayout.addWidget(self.sair)

        self.retranslateUi(ListRoomMates)
        QtCore.QMetaObject.connectSlotsByName(ListRoomMates)

    def retranslateUi(self, ListRoomMates):
        _translate = QtCore.QCoreApplication.translate
        ListRoomMates.setWindowTitle(_translate("ListRoomMates", "Lista de Moradores"))
        self.atualizar.setText(_translate("ListRoomMates", "Atualizar"))
        self.adicionarRegistro.setText(_translate("ListRoomMates", "Adicionar"))
        self.editarRegistro.setText(_translate("ListRoomMates", "Editar"))
        self.removerRegistro.setText(_translate("ListRoomMates", "Remover"))
        item = self.moradores.horizontalHeaderItem(0)
        item.setText(_translate("ListRoomMates", "Id"))
        item = self.moradores.horizontalHeaderItem(1)
        item.setText(_translate("ListRoomMates", "Nome"))
        item = self.moradores.horizontalHeaderItem(2)
        item.setText(_translate("ListRoomMates", "Data de Inclusão"))
        self.sair.setText(_translate("ListRoomMates", "Fechar"))


from . import ImageResources
