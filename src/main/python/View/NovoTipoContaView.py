from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from datetime import date

from UI.NovoTipoConta import Ui_NovoTipoConta
from Model.TipoConta import TipoConta

class NovoTipoContaView(QDialog, Ui_NovoTipoConta):
    salvo = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(NovoTipoContaView, self).__init__()
        self.setupUi(self)
        self.setModal(True)
        self.salvar.setEnabled(False)

        self.tipoConta = None

        self.cancelar.clicked.connect(self.close)
        self.salvar.clicked.connect(self.__salvar)
        self.nomeTipoConta.textChanged.connect(self.__checkText)

        if 'tipo_conta_id' in kwargs:
            self.tipoConta = TipoConta.get_by_id(kwargs['tipo_conta_id'])
            self.nomeTipoConta.setText(self.tipoConta.nome)
            self.salvar.setEnabled(False)
            self.setWindowTitle(f"Editando Tipo de Conta: {self.tipoConta.nome}")

    @pyqtSlot()
    def __checkText(self):
        if not self.nomeTipoConta.text():
            self.salvar.setEnabled(False)
        else:
            self.salvar.setEnabled(True)

    @pyqtSlot()
    def __salvar(self):
        if self.tipoConta:
            self.tipoConta.nome = self.nomeTipoConta.text()
            self.tipoConta.save()
        else:
            TipoConta.create(nome=self.nomeTipoConta.text(), data=date.today().strftime('%Y-%m-%d'))

        self.salvo.emit()
        self.close()