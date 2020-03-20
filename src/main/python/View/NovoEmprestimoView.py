from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt

from UI.NovoEmprestimo import Ui_NovoEmprestimo

from Model.Morador import Morador

class NovoEmprestimoView(QDialog, Ui_NovoEmprestimo):
    salvo = pyqtSignal(dict)
    def __init__(self, *args, **kwargs):
        super(NovoEmprestimoView, self).__init__()
        self.setupUi(self)
        self.setModal(True)
        self.salvar.setEnabled(False)

        self.cancelar.clicked.connect(self.close)
        self.salvar.clicked.connect(self.__salvar)

        self.moradores = Morador.select().where(Morador.deleted == False)

        for morador in self.moradores:
            self.de.addItem(morador.nome, morador.id)
            self.para.addItem(morador.nome, morador.id)

        self.de.currentIndexChanged.connect(self.__validar)
        self.para.currentIndexChanged.connect(self.__validar)
        self.valor.textChanged.connect(self.__validar)
        self.descricao.textChanged.connect(self.__validar)

        self.emprestimo_id = None

        if 'dados_emprestimo' in kwargs:
            self.emprestimo_id = kwargs['dados_emprestimo']['id']
            self.de.setCurrentIndex(self.de.findData(kwargs['dados_emprestimo']['de_id']))
            self.para.setCurrentIndex(self.para.findData(kwargs['dados_emprestimo']['para_id']))
            self.descricao.setText(kwargs['dados_emprestimo']['descricao'])
            self.valor.setText(f"R${str(kwargs['dados_emprestimo']['valor']).replace('.', ',')}")
            self.salvar.setEnabled(True)
            self.cancelar.setVisible(False)
            self.setWindowTitle('Editando Empréstimo')

    def keyPressEvent(self, event):
        if not event.key() == Qt.Key_Escape:
            super(NovoEmprestimoView, self).keyPressEvent(event)

    def __pegaValor(self):
        valor = self.valor.text().replace('R$', '')
        valor = valor.replace(',', '.')
        if valor != '.':
            return float(valor)

        return 0

    @pyqtSlot()
    def __validar(self):
        if self.__pegaValor() <= 0 or self.de.currentIndex() == self.para.currentIndex() or self.descricao.text() == '':
            self.salvar.setEnabled(False)
        else:
            self.salvar.setEnabled(True)

    @pyqtSlot()
    def __salvar(self):
        de_id = self.de.currentData()
        para_id = self.para.currentData()
        valor = self.__pegaValor()
        descricao = self.descricao.text()
        self.salvo.emit({
            'id': self.emprestimo_id,
            'de_id': de_id,
            'para_id': para_id,
            'valor': valor,
            'descricao': descricao
        })

        self.close()
