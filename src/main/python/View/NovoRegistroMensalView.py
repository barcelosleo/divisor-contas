from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from datetime import date

from UI.NovoRegistroMensal import Ui_NovoRegistroMensal

from .NovoEmprestimoView import NovoEmprestimoView
from .NovaContaView import NovaContaView
from .RelatorioRegistroMensalView import RelatorioRegistroMensalView

from Model.Morador import Morador
from Model.TipoConta import TipoConta
from Model.Emprestimo import Emprestimo
from Model.Conta import Conta
from Model.RegistroMensal import RegistroMensal

class NovoRegistroMensalView(QDialog, Ui_NovoRegistroMensal):
    salvo = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(NovoRegistroMensalView, self).__init__()
        self.setupUi(self)
        self.setModal(True)
        self.emprestimos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.contas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.emprestimos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.contas.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.removerConta.setEnabled(False)
        self.editarConta.setEnabled(False)
        self.removerEmprestimo.setEnabled(False)
        self.editarEmprestimo.setEnabled(False)
        self.gerarRelatorio.setEnabled(False)

        self.adicionarEmprestimo.clicked.connect(self.__adicionarEmprestimo)
        self.editarEmprestimo.clicked.connect(self.__editarEmprestimo)
        self.removerEmprestimo.clicked.connect(self.__removerEmprestimo)
        self.adicionarConta.clicked.connect(self.__adicionarConta)
        self.editarConta.clicked.connect(self.__editarConta)
        self.removerConta.clicked.connect(self.__removerConta)
        self.cancelar.clicked.connect(self.close)
        self.salvar.clicked.connect(self.__salvar)
        self.emprestimos.itemSelectionChanged.connect(self.__emprestimoClicado)
        self.contas.itemSelectionChanged.connect(self.__contaClicada)
        self.gerarRelatorio.clicked.connect(self.__gerarRelatorio)

        self.mes.setText(date.today().strftime('%m'))
        self.ano.setText(date.today().strftime('%Y'))

        self.mes.textChanged.connect(self.__valida)
        self.ano.textChanged.connect(self.__valida)

        self.registroMensal = None

        self.__emprestimos = []
        self.__emprestimoSelecionadoIndex = None

        self.__contas = []
        self.__contaSelecionadaIndex = None

        self.__adjustHeaders()

        if 'registro_mensal_id' in kwargs:
            self.registroMensal = RegistroMensal.get_by_id(kwargs['registro_mensal_id'])

            self.mes.setText(self.registroMensal.data.strftime('%m'))
            self.ano.setText(self.registroMensal.data.strftime('%Y'))

        if self.registroMensal:
            self.gerarRelatorio.setEnabled(True)
            self.salvar.setEnabled(True)

        self.__atualizarContas()
        self.__atualizarEmprestimos()

    def __adjustHeaders(self):
        headerContas = self.contas.horizontalHeader()
        headerContas.setSectionResizeMode(0, QHeaderView.Stretch)
        headerContas.setSectionResizeMode(1, QHeaderView.Stretch)
        headerContas.setSectionResizeMode(2, QHeaderView.Stretch)
        headerContas.setSectionResizeMode(3, QHeaderView.Stretch)
        headerContas.setSectionResizeMode(4, QHeaderView.Stretch)

        headerEmprestimos = self.emprestimos.horizontalHeader()
        headerEmprestimos.setSectionResizeMode(0, QHeaderView.Stretch)
        headerEmprestimos.setSectionResizeMode(1, QHeaderView.Stretch)
        headerEmprestimos.setSectionResizeMode(2, QHeaderView.Stretch)
        headerEmprestimos.setSectionResizeMode(3, QHeaderView.Stretch)
        headerEmprestimos.setSectionResizeMode(4, QHeaderView.Stretch)

    def __atualizarEmprestimos(self):
        if self.registroMensal:
            emprestimos = Emprestimo.select().join(RegistroMensal).where(RegistroMensal.id == self.registroMensal.id)

            for emprestimo in emprestimos:
                emprestimo = {
                    'id': emprestimo.id,
                    'de_id': emprestimo.de_id,
                    'para_id': emprestimo.para_id,
                    'valor': emprestimo.valor,
                    'descricao': emprestimo.descricao,
                }
                if emprestimo not in self.__emprestimos:
                    self.__emprestimos.append(emprestimo)

        self.emprestimos.setRowCount(0)

        for emprestimo in self.__emprestimos:
            rowIndex = self.emprestimos.rowCount()

            self.emprestimos.insertRow(rowIndex)

            self.emprestimos.setItem(rowIndex, 0, QTableWidgetItem(str(emprestimo['id']) if emprestimo['id'] else ""))
            self.emprestimos.setItem(rowIndex, 1, QTableWidgetItem(str(emprestimo['descricao'])))
            self.emprestimos.setItem(rowIndex, 2, QTableWidgetItem(str(Morador.get_by_id(emprestimo['de_id']).nome)))
            self.emprestimos.setItem(rowIndex, 3, QTableWidgetItem(str(Morador.get_by_id(emprestimo['para_id']).nome)))
            self.emprestimos.setItem(rowIndex, 4, QTableWidgetItem(f'R$ {round(emprestimo["valor"], 2)}'))

    def __atualizarContas(self):
        if self.registroMensal:
            contas = Conta.select().join(RegistroMensal).where(RegistroMensal.id == self.registroMensal.id)

            for conta in contas:
                conta = {
                    'id': conta.id,
                    'tipo_conta_id': conta.tipo_conta_id,
                    'pagante_id': conta.morador_id,
                    'valor': conta.valor,
                    'descricao': conta.descricao
                }
                if conta not in self.__contas:
                    self.__contas.append(conta)

        self.contas.setRowCount(0)

        for conta in self.__contas:
            rowIndex = self.contas.rowCount()

            self.contas.insertRow(rowIndex)

            self.contas.setItem(rowIndex, 0, QTableWidgetItem(str(conta['id']) if conta['id'] else ""))
            self.contas.setItem(rowIndex, 1, QTableWidgetItem(str(conta['descricao'])))
            self.contas.setItem(rowIndex, 2, QTableWidgetItem(str(TipoConta.get_by_id(conta['tipo_conta_id']).nome)))
            self.contas.setItem(rowIndex, 3, QTableWidgetItem(f'R$ {round(conta["valor"], 2)}'))
            self.contas.setItem(rowIndex, 4, QTableWidgetItem(str(Morador.get_by_id(conta['pagante_id']).nome) if conta['pagante_id'] else "Não Paga"))

    def __getEmprestimoId(self):
        emprestimo_id = self.emprestimos.item(self.__emprestimoSelecionadoIndex, 0).text()
        if emprestimo_id != '':
            return int(emprestimo_id)

        return None

    def __getContaId(self):
        conta_id = self.contas.item(self.__contaSelecionadaIndex, 0).text()
        if conta_id != '':
            return int(conta_id)

        return None

    @pyqtSlot()
    def __valida(self):
        mes = int(self.mes.text()) if self.mes.text() != '' else 0
        ano = int(self.ano.text()) if self.ano.text() != '' else 0

        if (mes < 1 or mes > 12) or (ano < 1) or (len(self.__contas) == 0 and len(self.__emprestimos) == 0):
            self.salvar.setEnabled(False)
        else:
            self.salvar.setEnabled(True)

    @pyqtSlot()
    def __emprestimoClicado(self):
        r = self.emprestimos.currentRow()
        if r > -1:
            self.__emprestimoSelecionadoIndex = r
            self.editarEmprestimo.setEnabled(True)
            self.removerEmprestimo.setEnabled(True)
        else:
            self.__emprestimoSelecionadoIndex = None
            self.editarEmprestimo.setEnabled(False)
            self.removerEmprestimo.setEnabled(False)

    @pyqtSlot()
    def __contaClicada(self):
        r = self.contas.currentRow()
        if r > -1:
            self.__contaSelecionadaIndex = r
            self.editarConta.setEnabled(True)
            self.removerConta.setEnabled(True)
        else:
            self.__contaSelecionadaIndex = None
            self.editarConta.setEnabled(False)
            self.removerConta.setEnabled(False)

    @pyqtSlot()
    def __adicionarEmprestimo(self):
        self.__novoEmprestimoDialog = NovoEmprestimoView(self)
        self.__novoEmprestimoDialog.salvo.connect(self.__addEmprestimo)
        self.__novoEmprestimoDialog.show()

    @pyqtSlot(dict)
    def __addEmprestimo(self, dadosEmprestimo):
        if dadosEmprestimo['id']:
            Emprestimo.update(valor=dadosEmprestimo['valor'], descricao=dadosEmprestimo['descricao'], de_id=dadosEmprestimo['de_id'], para_id=dadosEmprestimo['para_id']).where(Emprestimo.id == dadosEmprestimo['id']).execute()
        else:
            self.__emprestimos.append(dadosEmprestimo)

        self.__atualizarEmprestimos()
        self.__valida()

    @pyqtSlot()
    def __editarEmprestimo(self):
        dadosEmprestimo = self.__emprestimos[self.__emprestimoSelecionadoIndex]
        del self.__emprestimos[self.__emprestimoSelecionadoIndex]
        self.__editarEmprestimoDialog = NovoEmprestimoView(self, dados_emprestimo=dadosEmprestimo)
        self.__editarEmprestimoDialog.salvo.connect(self.__addEmprestimo)
        self.__editarEmprestimoDialog.show()

    @pyqtSlot()
    def __removerEmprestimo(self):
        emprestimo_id = self.__getEmprestimoId()
        if emprestimo_id:
            Emprestimo.delete_by_id(emprestimo_id)

        del self.__emprestimos[self.__emprestimoSelecionadoIndex]
        self.__atualizarEmprestimos()
        self.__valida()

    @pyqtSlot()
    def __adicionarConta(self):
        self.__novaContaDialog = NovaContaView(self)
        self.__novaContaDialog.salvo.connect(self.__addConta)
        self.__novaContaDialog.show()

    @pyqtSlot(dict)
    def __addConta(self, dadosConta):
        if dadosConta['id']:
            Conta.update(valor=dadosConta['valor'], descricao=dadosConta['descricao'], morador_id=dadosConta['pagante_id'], tipo_conta_id=dadosConta['tipo_conta_id']).where(Conta.id == dadosConta['id']).execute()
        else:
            self.__contas.append(dadosConta)

        self.__atualizarContas()
        self.__valida()

    @pyqtSlot()
    def __editarConta(self):
        dadosConta = self.__contas[self.__contaSelecionadaIndex]
        del self.__contas[self.__contaSelecionadaIndex]
        self.__editarContaDialog = NovaContaView(self, dados_conta=dadosConta)
        self.__editarContaDialog.salvo.connect(self.__addConta)
        self.__editarContaDialog.show()

    @pyqtSlot()
    def __removerConta(self):
        conta_id = self.__getContaId()
        if conta_id:
            Conta.delete_by_id(conta_id)

        del self.__contas[self.__contaSelecionadaIndex]
        self.__atualizarContas()
        self.__valida()

    @pyqtSlot()
    def __salvar(self):
        if len(self.__contas) == 0 and len(self.__emprestimos) == 0:
            self.salvar.setEnabled(False)
        else:
            if self.registroMensal:
                registro_mensal = self.registroMensal
            else:
                registro_mensal = RegistroMensal.create(data=date.today().strftime('%Y-%m-%d'), total=0, numero_pessoas=0)

            total = 0
            moradores = len(Morador.select().where(Morador.deleted == False))

            for emprestimo in self.__emprestimos:
                if emprestimo['id']:
                    Emprestimo.update(valor=emprestimo['valor'], descricao=emprestimo['descricao'], de_id=emprestimo['de_id'], para_id=emprestimo['para_id']).where(Emprestimo.id == emprestimo['id']).execute()
                else:
                    Emprestimo.create(data=date.today().strftime('%Y-%m-%d'), valor=emprestimo['valor'], descricao=emprestimo['descricao'], registro_mensal_id=registro_mensal.id, de_id=emprestimo['de_id'], para_id=emprestimo['para_id'])

            for conta in self.__contas:
                total += conta['valor']
                if conta['id']:
                    Conta.update(valor=conta['valor'], descricao=conta['descricao'], morador_id=conta['pagante_id'], tipo_conta_id=conta['tipo_conta_id']).where(Conta.id == conta['id']).execute()
                else:
                    Conta.create(data=date.today().strftime('%Y-%m-%d'), valor=conta['valor'], descricao=conta['descricao'], registro_mensal_id=registro_mensal.id, morador_id=conta['pagante_id'], tipo_conta_id=conta['tipo_conta_id'])

            mes = int(self.mes.text()) if self.mes.text() != '' else 0
            ano = int(self.ano.text()) if self.ano.text() != '' else 0

            registro_mensal.data = date(ano, mes, 1)
            registro_mensal.total = total
            registro_mensal.numero_pessoas = moradores
            registro_mensal.save()

            self.__emprestimos = []
            self.__contas = []

            self.registroMensal = registro_mensal

            self.salvo.emit()
            self.__atualizarContas()
            self.__atualizarEmprestimos()
            self.gerarRelatorio.setEnabled(True)

    @pyqtSlot()
    def __gerarRelatorio(self):
        self.relatorioMensal = RelatorioRegistroMensalView(self, registro_mensal_id=self.registroMensal.id)
        self.relatorioMensal.show()