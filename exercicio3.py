class Trabalhador:
    def _init_(self, codigo, primeiroNome, ultimoNome, diaNasc, mesNasc, anoNasc, diaContrat, mesContrat, anoContrat, salarioBase):
        self.codigo = codigo
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome
        self.dataNascimento = (diaNasc, mesNasc, anoNasc)
        self.dataContratacao = (diaContrat, mesContrat, anoContrat)
        self.salarioBase = salarioBase

    def calcularIdade(self, anoAtual):
        return anoAtual - self.dataNascimento[2]

    def calcularTempoEmpresa(self, anoAtual):
        return anoAtual - self.dataContratacao[2]

    def aplicarAumento(self, anoAtual):
        tempoEmpresa = self.calcularTempoEmpresa(anoAtual)
        if tempoEmpresa < 5:
            self.salarioBase *= 1.02
        elif tempoEmpresa < 10:
            self.salarioBase *= 1.05
        else:
            self.salarioBase *= 1.10

    def exibirDetalhes(self, anoAtual):
        print(f"Código: {self.codigo}")
        print(f"Primeiro Nome: {self.primeiroNome}")
        print(f"Último Nome: {self.ultimoNome}")
        print(f"Idade: {self.calcularIdade(anoAtual)}")
        print(f"Tempo na Empresa: {self.calcularTempoEmpresa(anoAtual)} anos")
        print(f"Salário Atual: €{self.salarioBase:.2f}")


# Teste
trabalhador1 = Trabalhador('001', 'Ana', 'Silva', 15, 5, 1985, 10, 3, 2010, 3000)
trabalhador2 = Trabalhador('002', 'Carlos', 'Santos', 20, 8, 1990, 5, 6, 2015, 4000)

anoAtual = 2025

trabalhador1.aplicarAumento(anoAtual)
trabalhador1.exibirDetalhes(anoAtual)

trabalhador2.aplicarAumento(anoAtual)
trabalhador2.exibirDetalhes(anoAtual)