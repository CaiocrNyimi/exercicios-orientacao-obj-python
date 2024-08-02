class ContaBancaria2:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Sr {self._titular}, seu saldo é {self._saldo}"

    @property
    def titular(self):
        return self._titular

conta4 = ContaBancaria2("José", 3000)
print(f"Titular da conta: {conta4.titular}")
print(conta4)