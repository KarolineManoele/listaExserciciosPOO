class ContaBancaria:
    def _init_(self, nomeTitular, saldoInicial):
        self.__saldo = saldoInicial
        self.__nomeTitular = nomeTitular

    def depositarValor(self, valorDeposito):
        if valorDeposito > 0:
            self.__saldo += valorDeposito
        else:
            print("Erro: O valor do depósito deve ser positivo!")

    def sacarValor(self, valorSaque):
        if valorSaque > self.__saldo:
            print("Erro: Saldo insuficiente!")
        elif valorSaque <= 0:
            print("Erro: O valor do saque deve ser positivo!")
        else:
            self.__saldo -= valorSaque

    def exibirSaldo(self):
        return f"{self.__saldo:.2f}"

    def getNomeTitular(self):
        return self.__nomeTitular

    def setNomeTitular(self, novoNomeTitular):
        if not novoNomeTitular.strip():
            print("Erro: Nome do titular não pode ser vazio!")
        else:
            self.__nomeTitular = novoNomeTitular

    def _str_(self):
        return f"Conta de {self.__nomeTitular}"


c1 = ContaBancaria("Alice", 1000)
print(c1)
c1.depositarValor(500)
print(c1.exibirSaldo())
c1.sacarValor(2000)
c1.sacarValor(300)
print(c1.exibirSaldo())
c1.setNomeTitular("")
c1.setNomeTitular("Lucas")
print(c1.getNomeTitular())