from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt

from Model.Morador import Morador
from Model.TipoConta import TipoConta

from UI.NovaConta import Ui_NovaConta

class NovaContaView(QDialog, Ui_NovaConta):
    salvo = pyqtSignal(dict)
    def __init__(self, *args, **kwargs):
        super(NovaContaView, self).__init__()
        self.setupUi(self)
        self.setModal(True)
        self.salvar.setEnabled(False)

        self.cancelar.clicked.connect(self.close)
        self.salvar.clicked.connect(self.__salvar)

        self.moradores = Morador.select().where(Morador.deleted == False)
        self.tiposConta = TipoConta.select()

        self.pagante.addItem('Não pago', None)

        for morador in self.moradores:
            self.pagante.addItem(morador.nome, morador.id)

        for tipoConta in self.tiposConta:
            self.tipoConta.addItem(tipoConta.nome, tipoConta.id)

        self.conta_id = None

        self.tipoConta.currentIndexChanged.connect(self.__validar)
        self.valor.textChanged.connect(self.__validar)
        self.descricao.textChanged.connect(self.__validar)

        if 'dados_conta' in kwargs:
            self.conta_id = kwargs['dados_conta']['id']
            self.tipoConta.setCurrentIndex(self.tipoConta.findData(kwargs['dados_conta']['tipo_conta_id']))
            self.pagante.setCurrentIndex(self.pagante.findData(kwargs['dados_conta']['pagante_id']))
            self.descricao.setText(kwargs['dados_conta']['descricao'])
            self.valor.setText(f"R${str(kwargs['dados_conta']['valor']).replace('.', ',')}")
            self.salvar.setEnabled(True)
            self.cancelar.setVisible(False)
            self.setWindowTitle('Editando Conta')

    def keyPressEvent(self, event):
        if not event.key() == Qt.Key_Escape:
            super(NovaContaView, self).keyPressEvent(event)

    def __pegaValor(self):
        valor = self.valor.text().replace('R$', '')
        valor = valor.replace(',', '.')
        if valor != '.':
            return float(valor)

        return 0

    @pyqtSlot()
    def __validar(self):
        if self.__pegaValor() <= 0 or not self.tipoConta.currentData():
            self.salvar.setEnabled(False)
        else:
            self.salvar.setEnabled(True)

    @pyqtSlot()
    def __salvar(self):
        tipo_conta_id = self.tipoConta.currentData()
        pagante_id = self.pagante.currentData()
        valor = self.__pegaValor()
        descricao = self.descricao.text()
        self.salvo.emit({
            'id': self.conta_id,
            'tipo_conta_id': tipo_conta_id,
            'pagante_id': pagante_id,
            'valor': valor,
            'descricao': descricao
        })

        self.close()