from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5.QtCore import pyqtSlot
from datetime import date

from UI.ListRoomMates import Ui_ListRoomMates

from Model.Morador import Morador
from Model.Emprestimo import Emprestimo
from Model.Conta import Conta

from .NovoMoradorView import NovoMoradorView

class ListarMoradoresView(QDialog, Ui_ListRoomMates):
    def __init__(self, *args, **kwargs):
        super(ListarMoradoresView, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setModal(True)

        self.sair.clicked.connect(self.close)

        self.editarRegistro.setEnabled(False)
        self.removerRegistro.setEnabled(False)

        self.moradores.itemSelectionChanged.connect(self.__getClickedLine)
        self.moradores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.moradores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.removerRegistro.clicked.connect(self.__removerMorador)
        self.editarRegistro.clicked.connect(self.__editarMorador)
        self.adicionarRegistro.clicked.connect(self.__adicionarMorador)
        self.atualizar.clicked.connect(self.__refreshTable)

        self.id_morador = None

        self.__refreshTable()


    @pyqtSlot()
    def __refreshTable(self):
        self.moradores.setRowCount(0)
        moradores = Morador.select().where(Morador.deleted == False)
        self.__fillTable(moradores)

    def __fillTable(self, moradores):
        if moradores:
            for morador in moradores:
                rowPosition = self.moradores.rowCount()
                self.moradores.insertRow(rowPosition)

                self.moradores.setItem(rowPosition, 0, QTableWidgetItem(str(morador.id)))
                self.moradores.setItem(rowPosition, 1, QTableWidgetItem(str(morador.nome)))
                self.moradores.setItem(rowPosition, 2, QTableWidgetItem(str(morador.data.strftime('%d/%m/%Y'))))

        header = self.moradores.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

    @pyqtSlot()
    def __getClickedLine(self):
        r = self.moradores.currentRow()
        if r > -1:
            self.id_morador = int(self.moradores.item(r, 0).text())
            self.editarRegistro.setEnabled(True)
            self.removerRegistro.setEnabled(True)
        else:
            self.id_morador = None
            self.editarRegistro.setEnabled(False)
            self.removerRegistro.setEnabled(False)

    @pyqtSlot()
    def __removerMorador(self):
        if self.id_morador:
            resposta = QMessageBox.question(self, 'Exclusão de Morador', 'Realmente deseja excluir o morador?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if resposta == QMessageBox.Yes:
                temContas = Conta.select().where(Conta.morador == self.id_morador).count()
                temEmprestimos = Emprestimo.select().where(Emprestimo.de == self.id_morador | Emprestimo.para == self.id_morador).count()
                if temContas > 0 or temEmprestimos > 0:
                    QMessageBox.warning(self, 'Morador não pode ser excluído', 'Morador tem registros vinculados!', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    morador = Morador.get_by_id(self.id_morador)
                    morador.deleted = True
                    morador.save()
                self.__refreshTable()
        else:
            self.editarRegistro.setEnabled(False)
            self.removerRegistro.setEnabled(False)

    @pyqtSlot()
    def __editarMorador(self):
        if self.id_morador:
            self.editarMoradoDialog = NovoMoradorView(self, morador_id=self.id_morador)
            self.editarMoradoDialog.salvo.connect(self.__refreshTable)
            self.editarMoradoDialog.show()
        else:
            self.editarRegistro.setEnabled(False)
            self.removerRegistro.setEnabled(False)

    @pyqtSlot()
    def __adicionarMorador(self):
        self.novoMoradorDialog = NovoMoradorView(self)
        self.novoMoradorDialog.salvo.connect(self.__refreshTable)
        self.novoMoradorDialog.show()
