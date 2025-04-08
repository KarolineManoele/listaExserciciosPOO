class Produto:
    def _init_(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def alterarPreco(self, novoPreco):
        if novoPreco > 0:
            self.preco = novoPreco
        else:
            print("Erro: O preço deve ser maior que zero.")

    def vender(self, quantidade):
        if quantidade > self.estoque:
            print("Erro: Estoque insuficiente!")
        elif quantidade <= 0:
            print("Erro: A quantidade deve ser positiva!")
        else:
            self.estoque -= quantidade

    def reabastecer(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
        else:
            print("Erro: A quantidade deve ser positiva!")

    def exibirDetalhes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: {self.preco:.2f}")
        print(f"Estoque: {self.estoque}")

    def _str_(self):
        return f"Produto: {self.nome}"


p = Produto("Caderno", 15.50, 10)
print(p)
p.alterarPreco(-5)
p.alterarPreco(20)
p.vender(5)
p.vender(10)
p.reabastecer(15)
p.exibirDetalhes()