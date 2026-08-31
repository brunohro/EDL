class no:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.proximo = None


class Lista:

    def __init__(self): # (a) Construtor
        self.cabeca = None
        self.tamanho = 0

    
    def ObterProximo(self, no): # (b) ObterProximo
        return no.proximo

   
    def ObterValor(self, no):  # (c) ObterValor
        return (no.valor1, no.valor2)

    
    def AlterarNo(self, no, valor1, valor2): # (d) AlterarNo
        no.valor1 = valor1
        no.valor2 = valor2

    
    def Tamanho(self): # (e) Tamanho
        return self.tamanho

    
    def Existe(self, no): # (f) Existe
        atual = self.cabeca

        while atual is not None:
            if atual == no:
                return True

            atual = atual.proximo

        return False

    
    def mostrarALL(self): # (g) mostrarALL
        elementos = []
        atual = self.cabeca

        while atual is not None:
            elementos.append((atual.valor1, atual.valor2))
            atual = atual.proximo

        return elementos

    
    def Buscar(self, valor1): # (h) Buscar
        atual = self.cabeca

        while atual is not None:
            if atual.valor1 == valor1:
                return True

            atual = atual.proximo

        return False

    
    def Inserir(self, valor1, valor2): # (i) Inserir
        novo_no = no(valor1, valor2)

        if self.cabeca is None or self.cabeca.valor1 > valor1:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no

        else:
            atual = self.cabeca
        
            while (
                atual.proximo is not None
                and atual.proximo.valor1 < valor1
            ):
                atual = atual.proximo

            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

        self.tamanho += 1

    
    def Excluir(self, valor1): # (j) Excluir

        if self.cabeca is None:
            return False

        if self.cabeca.valor1 == valor1:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return True

        atual = self.cabeca

        while (
            atual.proximo is not None
            and atual.proximo.valor1 != valor1
        ):
            atual = atual.proximo

        if atual.proximo is None:
            return False

        atual.proximo = atual.proximo.proximo
        self.tamanho -= 1

        return True

    
    def __del__(self): # (k) Destrutor
        atual = self.cabeca

        while atual is not None:
            proximo = atual.proximo
            atual.proximo = None
            atual = proximo

        self.cabeca = None
        self.tamanho = 0


#2. Implemente uma fun ̧c ̃ao main para manipular todas as implementa ̧c ̃oes criadas no item anterior

def main():

    lista = Lista()

    lista.Inserir(3, 30)
    lista.Inserir(1, 10)
    lista.Inserir(2, 20)

    print("Todos os elementos:")
    print(lista.mostrarALL())

    print("\nTamanho da lista:")
    print(lista.Tamanho())

    no_teste = lista.cabeca.proximo

    print("\nO nó existe na lista?")
    print(lista.Existe(no_teste))

    # Obter valor
    print("\nValores do nó:")
    print(lista.ObterValor(no_teste))

    # Obter próximo
    proximo = lista.ObterProximo(no_teste)

    print("\nPróximo nó:")
    if proximo is not None:
        print(lista.ObterValor(proximo))
    else:
        print("Não existe próximo nó.")

    # Buscar
    print("\nBuscar nó com valor1 = 3:")
    print(lista.Buscar(3))

    # Alterar
    lista.AlterarNo(no_teste, 4, 40)

    print("\nApós alterar o nó:")
    print(lista.mostrarALL())

    # Excluir
    lista.Excluir(1)

    print("\nApós excluir o nó com valor1 = 1:")
    print(lista.mostrarALL())

    print("\nTamanho final:")
    print(lista.Tamanho())

main()