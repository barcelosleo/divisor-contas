from Model.Morador import Morador
from Model.TipoConta import TipoConta
from Model.RegistroMensal import RegistroMensal
from Model.Emprestimo import Emprestimo
from Model.Conta import Conta

def migrate():
    try:
        Morador.create_table()
        print(f'Tabela "Morador" criada com sucesso!')
    except peewee.OperationalError:
        print(f'Tabela "Morador" já existe!')

    try:
        TipoConta.create_table()
        print(f'Tabela "TipoConta" criada com sucesso!')
    except peewee.OperationalError:
        print(f'Tabela "TipoConta" já existe!')

    try:
        RegistroMensal.create_table()
        print(f'Tabela "RegistroMensal" criada com sucesso!')
    except peewee.OperationalError:
        print(f'Tabela "RegistroMensal" já existe!')

    try:
        Emprestimo.create_table()
        print(f'Tabela "Emprestimo" criada com sucesso!')
    except peewee.OperationalError:
        print(f'Tabela "Emprestimo" já existe!')

    try:
        Conta.create_table()
        print(f'Tabela "Conta" criada com sucesso!')
    except peewee.OperationalError:
        print(f'Tabela "Conta" já existe!')


if __name__ == '__main__':
    migrate()