class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            raise IndexError("A pilha está vazia")

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        else:
            raise IndexError("A pilha está vazia")

        
pilha = Pilha()


expressao = input("Digite uma expressão: ")

for caractere in expressao:

    if caractere == '(' or caractere == '[' or caractere == '{':
        pilha.empilhar(caractere)

    elif caractere == ')' or caractere == ']' or caractere == '}':

        if pilha.esta_vazia():
            print("Expressão não balanceada!")
            break

        abertura = pilha.desempilhar()

        if caractere == ')' and abertura != '(':
            print("Expressão não balanceada!")
            break

        if caractere == ']' and abertura != '[':
            print("Expressão não balanceada!")
            break

        if caractere == '}' and abertura != '{':
            print("Expressão não balanceada!")
            break

else:
    if pilha.esta_vazia():
        print("Expressão balanceada!")
    else:
        print("Expressão não balanceada!")       