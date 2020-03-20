from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5.QtCore import pyqtSlot

from UI.MainWindow import Ui_MainWindow
from .ListarMoradoresView import ListarMoradoresView
from .ListarTipoContasView import ListarTipoContasView
from .NovoMoradorView import NovoMoradorView
from .NovoTipoContaView import NovoTipoContaView
from .NovoRegistroMensalView import NovoRegistroMensalView
from .RelatorioRegistroMensalView import RelatorioRegistroMensalView
from Model.RegistroMensal import RegistroMensal
from Model.Conta import Conta
from Model.Emprestimo import Emprestimo

class MainWindowView(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindowView, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.editarRegistro.setEnabled(False)
        self.removerRegistro.setEnabled(False)
        self.gerarRelatorio.setEnabled(False)
        self.registrosMensais.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.addMorador.triggered.connect(self.__novoMorador)
        self.listarMoradores.triggered.connect(self.__listMoradores)
        self.addTipoConta.triggered.connect(self.__novoTipoConta)
        self.listarTipoConta.triggered.connect(self.__listTipoContas)
        self.novoRegistro.clicked.connect(self.__adicionar)
        self.registrosMensais.itemSelectionChanged.connect(self.__registroMensalClicado)
        self.editarRegistro.clicked.connect(self.__editar)
        self.removerRegistro.clicked.connect(self.__remover)
        self.gerarRelatorio.clicked.connect(self.__gerarRelatorio)

        self.registro_mensal_id = None

        self.__atualizar()

    @pyqtSlot()
    def __registroMensalClicado(self):
        r = self.registrosMensais.currentRow()
        if r > -1:
            self.registro_mensal_id = int(self.registrosMensais.item(r, 0).text())
            self.editarRegistro.setEnabled(True)
            self.gerarRelatorio.setEnabled(True)
            self.removerRegistro.setEnabled(True)
        else:
            self.registro_mensal_id = None
            self.editarRegistro.setEnabled(False)
            self.gerarRelatorio.setEnabled(False)
            self.removerRegistro.setEnabled(False)

    @pyqtSlot()
    def __novoMorador(self):
        self.novoMoradorDialog = NovoMoradorView(self)
        self.novoMoradorDialog.show()

    @pyqtSlot()
    def __listMoradores(self):
        self.listarMoradorDialog = ListarMoradoresView(self)
        self.listarMoradorDialog.show()

    @pyqtSlot()
    def __novoTipoConta(self):
        self.novoTipoContaDialog = NovoTipoContaView(self)
        self.novoTipoContaDialog.show()

    @pyqtSlot()
    def __listTipoContas(self):
        self.listarTipoContasDialog = ListarTipoContasView(self)
        self.listarTipoContasDialog.show()

    @pyqtSlot()
    def __adicionar(self):
        self.novoRegistroMensalDialog = NovoRegistroMensalView(self)
        self.novoRegistroMensalDialog.salvo.connect(self.__atualizar)
        self.novoRegistroMensalDialog.show()

    @pyqtSlot()
    def __editar(self):
        self.editarRegistroMensalDialog = NovoRegistroMensalView(self, registro_mensal_id=self.registro_mensal_id)
        self.editarRegistroMensalDialog.salvo.connect(self.__atualizar)
        self.editarRegistroMensalDialog.show()

    @pyqtSlot()
    def __remover(self):
        if self.registro_mensal_id:
            resposta = QMessageBox.question(self, 'Exclusão de Registro Mensal', 'Realmente deseja excluir o registro mensal e todas as contas e empréstimos atrelados a ele?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if resposta == QMessageBox.Yes:
                Conta.delete().where(Conta.registro_mensal_id == self.registro_mensal_id).execute()
                Emprestimo.delete().where(Emprestimo.registro_mensal_id == self.registro_mensal_id).execute()
                RegistroMensal.delete_by_id(self.registro_mensal_id)

            self.__atualizar()

    @pyqtSlot()
    def __ver(self):
        pass

    @pyqtSlot()
    def __atualizar(self):
        self.registrosMensais.setRowCount(0)
        registrosMensais = RegistroMensal.select()
        self.__fillTable(registrosMensais)

    def __fillTable(self, registrosMensais):
        if registrosMensais:
            for registroMensal in registrosMensais:
                rowPosition = self.registrosMensais.rowCount()
                self.registrosMensais.insertRow(rowPosition)

                self.registrosMensais.setItem(rowPosition, 0, QTableWidgetItem(str(registroMensal.id)))
                self.registrosMensais.setItem(rowPosition, 1, QTableWidgetItem(str(registroMensal.data.strftime('%m/%Y'))))
                self.registrosMensais.setItem(rowPosition, 2, QTableWidgetItem(str(registroMensal.total)))
                self.registrosMensais.setItem(rowPosition, 3, QTableWidgetItem(str(round(registroMensal.total / registroMensal.numero_pessoas, 2))))

        header = self.registrosMensais.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)


    def __gerarRelatorio(self):
        self.relatorioDialog = RelatorioRegistroMensalView(self, registro_mensal_id = self.registro_mensal_id)
        self.relatorioDialog.show()