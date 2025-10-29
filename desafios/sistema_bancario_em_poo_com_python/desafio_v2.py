import textwrap
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            self.historico.adicionar_transacao(Saque(valor))
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        excedeu_limite = valor > self.limite
        excedeu_saques = self.saques_realizados >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        else:
            if super().sacar(valor):
                self.saques_realizados += 1
                return True
        return False

class Historico:
    def __init__(self):
        self.transacoes = []
        self.data_abertura = datetime.now()
    def adicionar_transacao(self,
                            transacao):
        self.transacoes.append(transacao)
    def extrato(self):
        transacoes_str = ""
        for transacao in self.transacoes:
            transacoes_str += str(transacao) + "\n"
        return transacoes_str

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass
    @abstractproperty
    def valor(self):
        pass
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        conta.sacar(self.valor)
    def __str__(self):
        return f"Saque de R$ {self.valor:.2f}"
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        conta.depositar(self.valor)
    def __str__(self):
        return f"Depósito de R$ {self.valor:.2f}"
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            self.historico.adicionar_transacao(Saque(valor))
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            self.historico.adicionar_transacao(Deposito(valor))
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        return True

def menu():
    menu = """\n
    =======================
        MENU DE OPÇÕES

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    =======================
    """
    return input(textwrap.dedent(menu))

def main():
    cliente = PessoaFisica("João Silva", "01/01/1990", "123.456.789-00", "Rua A, 123")
    conta = ContaCorrente.nova_conta(cliente, "0001-01")
    cliente.adicionar_conta(conta)

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            transacao = Deposito(valor)
            cliente.realizar_transacao(conta, transacao)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            transacao = Saque(valor)
            cliente.realizar_transacao(conta, transacao)
        elif opcao == "3":
            print("\n====== EXTRATO ======")
            extrato = conta.historico.extrato()
            print(extrato if extrato else "Não foram realizadas movimentações.")
            print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
            print("=====================")
        elif opcao == "4":
            print("Encerrando o sistema. Obrigado por utilizar nosso banco!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")
            
if __name__ == "__main__":
    main()