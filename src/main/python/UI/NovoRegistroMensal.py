# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/UI/NovoRegistroMensal.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NovoRegistroMensal(object):
    def setupUi(self, NovoRegistroMensal):
        NovoRegistroMensal.setObjectName("NovoRegistroMensal")
        NovoRegistroMensal.resize(605, 440)
        self.gridLayout_2 = QtWidgets.QGridLayout(NovoRegistroMensal)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.salvar = QtWidgets.QPushButton(NovoRegistroMensal)
        self.salvar.setMaximumSize(QtCore.QSize(100, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/img/svg/checkmark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salvar.setIcon(icon)
        self.salvar.setObjectName("salvar")
        self.gridLayout_2.addWidget(self.salvar, 2, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(NovoRegistroMensal)
        self.groupBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.mes = QtWidgets.QLineEdit(self.groupBox)
        self.mes.setObjectName("mes")
        self.gridLayout.addWidget(self.mes, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ano = QtWidgets.QLineEdit(self.groupBox)
        self.ano.setObjectName("ano")
        self.gridLayout.addWidget(self.ano, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.cancelar = QtWidgets.QPushButton(NovoRegistroMensal)
        self.cancelar.setMaximumSize(QtCore.QSize(100, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/img/svg/export.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon1)
        self.cancelar.setObjectName("cancelar")
        self.gridLayout_2.addWidget(self.cancelar, 2, 5, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(NovoRegistroMensal)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.adicionarConta = QtWidgets.QPushButton(self.groupBox_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/img/svg/add_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adicionarConta.setIcon(icon2)
        self.adicionarConta.setObjectName("adicionarConta")
        self.horizontalLayout_2.addWidget(self.adicionarConta)
        self.editarConta = QtWidgets.QPushButton(self.groupBox_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/img/svg/edit_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editarConta.setIcon(icon3)
        self.editarConta.setObjectName("editarConta")
        self.horizontalLayout_2.addWidget(self.editarConta)
        self.removerConta = QtWidgets.QPushButton(self.groupBox_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/img/svg/remove_image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removerConta.setIcon(icon4)
        self.removerConta.setObjectName("removerConta")
        self.horizontalLayout_2.addWidget(self.removerConta)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.contas = QtWidgets.QTableWidget(self.groupBox_2)
        self.contas.setObjectName("contas")
        self.contas.setColumnCount(5)
        self.contas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.contas.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.contas)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 6)
        self.groupBox_3 = QtWidgets.QGroupBox(NovoRegistroMensal)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.adicionarEmprestimo = QtWidgets.QPushButton(self.groupBox_3)
        self.adicionarEmprestimo.setIcon(icon2)
        self.adicionarEmprestimo.setObjectName("adicionarEmprestimo")
        self.horizontalLayout.addWidget(self.adicionarEmprestimo)
        self.editarEmprestimo = QtWidgets.QPushButton(self.groupBox_3)
        self.editarEmprestimo.setIcon(icon3)
        self.editarEmprestimo.setObjectName("editarEmprestimo")
        self.horizontalLayout.addWidget(self.editarEmprestimo)
        self.removerEmprestimo = QtWidgets.QPushButton(self.groupBox_3)
        self.removerEmprestimo.setIcon(icon4)
        self.removerEmprestimo.setObjectName("removerEmprestimo")
        self.horizontalLayout.addWidget(self.removerEmprestimo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.emprestimos = QtWidgets.QTableWidget(self.groupBox_3)
        self.emprestimos.setObjectName("emprestimos")
        self.emprestimos.setColumnCount(5)
        self.emprestimos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.emprestimos.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.emprestimos)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 1, 1, 5)
        self.gerarRelatorio = QtWidgets.QPushButton(NovoRegistroMensal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/img/svg/neutral_trading.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gerarRelatorio.setIcon(icon5)
        self.gerarRelatorio.setObjectName("gerarRelatorio")
        self.gridLayout_2.addWidget(self.gerarRelatorio, 2, 4, 1, 1)

        self.retranslateUi(NovoRegistroMensal)
        QtCore.QMetaObject.connectSlotsByName(NovoRegistroMensal)

    def retranslateUi(self, NovoRegistroMensal):
        _translate = QtCore.QCoreApplication.translate
        NovoRegistroMensal.setWindowTitle(_translate("NovoRegistroMensal", "Novo Registro Mensal"))
        self.salvar.setText(_translate("NovoRegistroMensal", "Salvar"))
        self.groupBox.setTitle(_translate("NovoRegistroMensal", "Registro Mensal"))
        self.label.setText(_translate("NovoRegistroMensal", "Mês"))
        self.label_2.setText(_translate("NovoRegistroMensal", "Ano"))
        self.cancelar.setText(_translate("NovoRegistroMensal", "Fechar"))
        self.groupBox_2.setTitle(_translate("NovoRegistroMensal", "Contas"))
        self.adicionarConta.setText(_translate("NovoRegistroMensal", "Adicionar"))
        self.editarConta.setText(_translate("NovoRegistroMensal", "Editar"))
        self.removerConta.setText(_translate("NovoRegistroMensal", "Remover"))
        item = self.contas.horizontalHeaderItem(0)
        item.setText(_translate("NovoRegistroMensal", "Id"))
        item = self.contas.horizontalHeaderItem(1)
        item.setText(_translate("NovoRegistroMensal", "Descrição"))
        item = self.contas.horizontalHeaderItem(2)
        item.setText(_translate("NovoRegistroMensal", "Tipo de Conta"))
        item = self.contas.horizontalHeaderItem(3)
        item.setText(_translate("NovoRegistroMensal", "Valor"))
        item = self.contas.horizontalHeaderItem(4)
        item.setText(_translate("NovoRegistroMensal", "Pagante"))
        self.groupBox_3.setTitle(_translate("NovoRegistroMensal", "Empréstimos e Outros Valores"))
        self.adicionarEmprestimo.setText(_translate("NovoRegistroMensal", "Adicionar"))
        self.editarEmprestimo.setText(_translate("NovoRegistroMensal", "Editar"))
        self.removerEmprestimo.setText(_translate("NovoRegistroMensal", "Remover"))
        item = self.emprestimos.horizontalHeaderItem(0)
        item.setText(_translate("NovoRegistroMensal", "Id"))
        item = self.emprestimos.horizontalHeaderItem(1)
        item.setText(_translate("NovoRegistroMensal", "Descrição"))
        item = self.emprestimos.horizontalHeaderItem(2)
        item.setText(_translate("NovoRegistroMensal", "De"))
        item = self.emprestimos.horizontalHeaderItem(3)
        item.setText(_translate("NovoRegistroMensal", "Para"))
        item = self.emprestimos.horizontalHeaderItem(4)
        item.setText(_translate("NovoRegistroMensal", "Valor"))
        self.gerarRelatorio.setText(_translate("NovoRegistroMensal", "Gerar Relatório"))


from . import ImageResources
