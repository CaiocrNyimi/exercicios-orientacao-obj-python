class ContaBancaria():

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = int(saldo)
        self._ativo = False

    def __str__(self):
        return f'Nome do titular: {self.titular} | Saldo da conta: R${self.saldo} | Conta ativa: {self._ativo}'
    
    def ativar_conta(cls, conta):
        conta._ativo = True
    
conta1 = ContaBancaria('Ayrton Senna', 1988)
print(conta1)
ContaBancaria.ativar_conta(None, conta1)
print(conta1)




class ContaBancaria2:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

        @property
        def titular (self):
            return self._titular
        
        @property 
        def saldo (self):
            return self._saldo
        
conta2 = ContaBancaria2('Renato Russo', 1989)
print(f'Titular da conta: {conta2._titular} | Saldo: R${conta2._saldo} | Ativo: {conta2._ativo}')




class ClienteBanco():

    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

cliente1 = ClienteBanco("Ana", 30, "Rua Z", "123.456.789-10", "Arquiteta")
cliente2 = ClienteBanco("Luiza", 25, "Rua Y", "987.654.321-23", "Estudante")
cliente3 = ClienteBanco("Pedro", 40, "Rua X", "111.222.333-45", "Motorista")

class ClienteBanco:

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria2(titular, saldo_inicial)
        return conta

conta_cliente1 = ClienteBanco.criar_conta('Ana', 2000)
print(f"Conta de {conta_cliente1._titular} criada com saldo inicial de R${conta_cliente1._saldo}")