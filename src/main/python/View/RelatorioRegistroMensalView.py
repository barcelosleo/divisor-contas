from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import pyqtSlot

from UI.RelatorioRegistroMensal import Ui_RelatorioRegistroMensal

from Model.RegistroMensal import RegistroMensal
from Model.TipoConta import TipoConta
from Model.Morador import Morador
from Model.Conta import Conta
from Model.Emprestimo import Emprestimo

class RelatorioRegistroMensalView(QDialog, Ui_RelatorioRegistroMensal):
    def __init__(self, *args, **kwargs):
        super(RelatorioRegistroMensalView, self).__init__()
        self.setupUi(self)
        self.setModal(True)

        self.sair.clicked.connect(self.close)

        self.contas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.totais.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.emprestimos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.contas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.totais.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.emprestimos.setEditTriggers(QAbstractItemView.NoEditTriggers)


        self.__registroMensal = RegistroMensal.get_by_id(kwargs['registro_mensal_id'])
        self.__contas = Conta.select().where(Conta.registro_mensal_id == self.__registroMensal.id)
        self.__emprestimos = Emprestimo.select().where(Emprestimo.registro_mensal_id == self.__registroMensal.id)
        self.__moradores = Morador.select().where(Morador.deleted == False)
        self.__totais = []

        self.__adjustHeaders()
        self.titulo.setText(self.titulo.text().replace('mes_ano', self.__registroMensal.data.strftime('%m/%Y')))
        self.__tabelaContas()
        self.__tabelaEmprestimos()
        self.__tabelaTotais()

    def __adjustHeaders(self):
        header = self.contas.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        header = self.emprestimos.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        header = self.totais.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

    def __tabelaContas(self):
        total = 0
        for conta in self.__contas:
            rowIndex = self.contas.rowCount()
            self.contas.insertRow(rowIndex)

            self.contas.setItem(rowIndex, 0, QTableWidgetItem(f"R${conta.valor}"))
            self.contas.setItem(rowIndex, 1, QTableWidgetItem(TipoConta.get_by_id(conta.tipo_conta_id).nome))
            self.contas.setItem(rowIndex, 2, QTableWidgetItem(conta.descricao))
            self.contas.setItem(rowIndex, 3, QTableWidgetItem(Morador.get_by_id(conta.morador_id).nome if conta.morador_id else "Não Paga"))
            total += conta.valor

        self.__totais = [{'total_por_pessoa': total / len(self.__moradores)}] * len(self.__moradores)
        self.totalLabel.setText(self.totalLabel.text().replace('valor', str(total).replace('.', ',')))

    def __tabelaEmprestimos(self):
        for emprestimo in self.__emprestimos:
            rowIndex = self.emprestimos.rowCount()
            self.emprestimos.insertRow(rowIndex)
            self.emprestimos.setItem(rowIndex, 0, QTableWidgetItem(emprestimo.descricao))
            self.emprestimos.setItem(rowIndex, 1, QTableWidgetItem(Morador.get_by_id(emprestimo.de_id).nome))
            self.emprestimos.setItem(rowIndex, 2, QTableWidgetItem(Morador.get_by_id(emprestimo.para_id).nome))
            self.emprestimos.setItem(rowIndex, 3, QTableWidgetItem(f"R${emprestimo.valor}"))

    def __tabelaTotais(self):
        i = 0
        for morador in self.__moradores:
            self.__totais[i]['total_pessoa'] = self.__totais[i]['total_por_pessoa']
            self.__totais[i]['total_pessoa_pago'] = 0
            emprestimos_de = Emprestimo.select().where(Emprestimo.de_id == morador.id & Emprestimo.registro_mensal_id == self.__registroMensal.id)
            emprestimos_para = Emprestimo.select().where(Emprestimo.para_id == morador.id & Emprestimo.registro_mensal_id == self.__registroMensal.id)
            contas = Conta().select().where(Conta.morador_id == morador.id & Conta.registro_mensal_id == self.__registroMensal.id)

            for emprestimo in emprestimos_de:
                self.__totais[i]['total_pessoa'] += emprestimo.valor

            for emprestimo in emprestimos_para:
                self.__totais[i]['total_pessoa'] -= emprestimo.valor

            for conta in contas:
                self.__totais[i]['total_pessoa_pago'] += conta.valor
                self.__totais[i]['total_pessoa'] -= conta.valor

            rowIndex = self.totais.rowCount()
            self.totais.insertRow(rowIndex)
            self.totais.setItem(rowIndex, 0, QTableWidgetItem(morador.nome))
            self.totais.setItem(rowIndex, 1, QTableWidgetItem(f"R${round(self.__totais[i]['total_por_pessoa'], 2)}"))
            self.totais.setItem(rowIndex, 2, QTableWidgetItem(f"R${round(self.__totais[i]['total_pessoa_pago'], 2)}"))
            self.totais.setItem(rowIndex, 3, QTableWidgetItem(f"R${round(self.__totais[i]['total_pessoa'], 2)}"))

            i += 1
