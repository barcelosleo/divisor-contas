from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox
from PyQt5.QtCore import pyqtSlot

from UI.ListarTipoContas import Ui_ListarTipoContas

from Model.TipoConta import TipoConta
from Model.Conta import Conta

from .NovoTipoContaView import NovoTipoContaView

class ListarTipoContasView(QDialog, Ui_ListarTipoContas):
    def __init__(self, *args, **kwargs):
        super(ListarTipoContasView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)
        self.editarRegistro.setEnabled(False)
        self.removerRegistro.setEnabled(False)

        self.sair.clicked.connect(self.close)
        self.atualizar.clicked.connect(self.__atualizar)
        self.adicionar.clicked.connect(self.__adicionar)
        self.editarRegistro.clicked.connect(self.__editar)
        self.removerRegistro.clicked.connect(self.__remover)
        self.tiposContas.itemSelectionChanged.connect(self.__getClickedLine)

        self.tiposContas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tiposContas.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.__atualizar()

    @pyqtSlot()
    def __editar(self):
        self.editarTipoContaDialog = NovoTipoContaView(self, tipo_conta_id=self.tipo_conta_id)
        self.editarTipoContaDialog.salvo.connect(self.__atualizar)
        self.editarTipoContaDialog.show()

    @pyqtSlot()
    def __remover(self):
        if self.tipo_conta_id:
            resposta = QMessageBox.question(self, 'Exclusão de Tipo de Conta', 'Realmente deseja excluir o tipo de conta?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if resposta == QMessageBox.Yes:
                temContas = Conta.select().where(Conta.tipo_conta == self.tipo_conta_id).count()
                if temContas > 0:
                    QMessageBox.warning(self, 'Tipo de Conta não pode ser excluído', 'Tipo de Conta tem registros vinculados!', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    TipoConta.delete_by_id(self.tipo_conta_id)
                self.__atualizar()
        else:
            self.editarRegistro.setEnabled(False)
            self.removerRegistro.setEnabled(False)

    @pyqtSlot()
    def __adicionar(self):
        self.adicionarTipoContaDialog = NovoTipoContaView(self)
        self.adicionarTipoContaDialog.salvo.connect(self.__atualizar)
        self.adicionarTipoContaDialog.show()

    @pyqtSlot()
    def __atualizar(self):
        self.tiposContas.setRowCount(0)
        tiposContas = TipoConta.select()
        self.__fillTable(tiposContas)

    def __fillTable(self, tiposContas):
        if tiposContas:
            for tipoConta in tiposContas:
                rowPosition = self.tiposContas.rowCount()
                self.tiposContas.insertRow(rowPosition)

                self.tiposContas.setItem(rowPosition, 0, QTableWidgetItem(str(tipoConta.id)))
                self.tiposContas.setItem(rowPosition, 1, QTableWidgetItem(str(tipoConta.nome)))
                self.tiposContas.setItem(rowPosition, 2, QTableWidgetItem(str(tipoConta.data.strftime('%d/%m/%Y'))))

        header = self.tiposContas.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

    @pyqtSlot()
    def __getClickedLine(self):
        r = self.tiposContas.currentRow()
        if r > -1:
            self.tipo_conta_id = int(self.tiposContas.item(r, 0).text())
            self.editarRegistro.setEnabled(True)
            self.removerRegistro.setEnabled(True)
        else:
            self.tipo_conta_id = None
            self.editarRegistro.setEnabled(False)
            self.removerRegistro.setEnabled(False)