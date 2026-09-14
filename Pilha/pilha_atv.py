class Pilha:
    def __init__(self):
        self.items = []

    def fechamento(self, item):
        if item == ')':
            return '('
        elif item == ']':
            return '['
        elif item == '}':
            return '{'
        else:
            return None

    def balanceada(self, expressao):
        for caractere in expressao:
            if caractere in '([{':
                self.items.append(caractere)
            elif caractere in ')]}':
                if not self.items or self.items[-1] != self.fechamento(caractere):
                    return False
                self.items.pop()
        return len(self.items) == 0

    def entrada(self):
        expressao = input("Digite uma expressão: ")
        if self.balanceada(expressao):
            print("Expressão balanceada!")
        else:
            print("Expressão não balanceada!")


entrada = Pilha()
entrada.entrada()


