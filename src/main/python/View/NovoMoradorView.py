from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from datetime import date

from UI.NewRoomMate import Ui_NewRoomMate

from Model.Morador import Morador

class NovoMoradorView(QDialog, Ui_NewRoomMate):
    salvo = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(NovoMoradorView, self).__init__()
        self.setupUi(self)
        self.setModal(True)

        self.morador = None

        self.salvarMorador.setEnabled(False)

        self.cancelarNovoMorador.clicked.connect(self.close)
        self.nomeMorador.textChanged.connect(self.__checkName)
        self.salvarMorador.clicked.connect(self.__salvarMorador)

        if 'morador_id' in kwargs:
            self.morador = Morador.get_by_id(kwargs['morador_id'])
            self.nomeMorador.setText(self.morador.nome)
            self.salvarMorador.setEnabled(False)
            self.setWindowTitle(f"Editando morador: {self.morador.nome}")

    @pyqtSlot()
    def __checkName(self):
        if not self.nomeMorador.text():
            self.salvarMorador.setEnabled(False)
        else:
            self.salvarMorador.setEnabled(True)

    @pyqtSlot()
    def __salvarMorador(self):
        if self.morador:
            self.morador.nome = self.nomeMorador.text()
            self.morador.save()
        else:
            Morador.create(nome=self.nomeMorador.text(), data=date.today().strftime('%Y-%m-%d'))

        self.salvo.emit()
        self.close()