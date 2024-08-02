class ClienteBanco:
    def __init__(self, titular, saldo, cpf, telefone, cep):
        self.titular = titular
        self.saldo = saldo
        self.cpf = cpf
        self.telefone = telefone
        self.cep = cep
        self.ativo = False

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f} | CPF: {self.cpf} | Telefone: {self.telefone} | CEP: {self.cep}"

    @classmethod
    def criar_cliente(cls, titular, saldo, cpf, telefone, cep):
        return cls(titular, saldo, cpf, telefone, cep)

# Instanciando 3 objetos da classe ClienteBanco
cliente1 = ClienteBanco("Maria", 5000, "12345678989", "999999999", "12345-000")
cliente2 = ClienteBanco("João", 4000, "98765432198", "888888888", "54321-000")
cliente3 = ClienteBanco.criar_cliente("Pedro", 6000, "12345678998", "777777777", "98765-000")

print(cliente1)
print(cliente2)
print(cliente3)
