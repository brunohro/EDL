class No:
    def __init__(self, coef, expoente):
        self.coeficiente = coef
        self.grau = expoente
        self.proximo = None


class Polinomio:
    def __init__(self):
        self.inicio = None

    def inserir(self, coeficiente, grau):
        novo_no = No(coeficiente, grau)
        
        if self.inicio is None:
            self.inicio = novo_no
            return
            
        atual = self.inicio
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no

    def ordenar(self):
        if self.inicio is None or self.inicio.proximo is None:
            return

        trocou = True
        while trocou:
            trocou = False
            atual = self.inicio
            while atual.proximo is not None:
                if atual.grau < atual.proximo.grau:
                    atual.grau, atual.proximo.grau = atual.proximo.grau, atual.grau
                    atual.coeficiente, atual.proximo.coeficiente = atual.proximo.coeficiente, atual.coeficiente
                    trocou = True
                atual = atual.proximo

    def somar_repetidos(self):
        if self.inicio is None:
            return

        atual = self.inicio
        while atual is not None:
            proximo = atual.proximo
            while proximo is not None and proximo.grau == atual.grau:
                atual.coeficiente += proximo.coeficiente
                proximo = proximo.proximo
            atual.proximo = proximo
            atual = proximo

    def remover_zeros(self):
        anterior = None
        atual = self.inicio
        
        while atual is not None:
            if atual.coeficiente == 0:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
            else:
                anterior = atual
            atual = atual.proximo

    def simplificar(self):
        self.ordenar()
        self.somar_repetidos()
        self.remover_zeros()

    def tamanho(self):
        quantidade = 0
        atual = self.inicio
        while atual:
            quantidade += 1
            atual = atual.proximo
        return quantidade

    def grau(self):
        if self.inicio is None:
            return 0
        maior_grau = self.inicio.grau
        atual = self.inicio.proximo
        while atual is not None:
            if atual.grau > maior_grau:
                maior_grau = atual.grau
            atual = atual.proximo
        return maior_grau

    def avaliar(self, valor):
        soma = 0
        atual = self.inicio
        while atual is not None:
            soma += atual.coeficiente * (valor ** atual.grau)
            atual = atual.proximo
        return soma

    def __add__(self, outro):
            novo_polinomio = Polinomio()
    
            atual = self.inicio
            while atual is not None:
                novo_polinomio.inserir(
                    atual.coeficiente,
                    atual.grau
                )
                atual = atual.proximo
    
            atual = outro.inicio
            while atual is not None:
                novo_polinomio.inserir(
                    atual.coeficiente,
                    atual.grau
                )
                atual = atual.proximo
    
            novo_polinomio.simplificar()
    
            return novo_polinomio
    
    def __sub__(self, outro):
            novo_polinomio = Polinomio()
    
            atual = self.inicio
            while atual is not None:
                novo_polinomio.inserir(
                    atual.coeficiente,
                    atual.grau
                )
                atual = atual.proximo
    
            atual = outro.inicio
            while atual is not None:
                novo_polinomio.inserir(
                    -atual.coeficiente,
                    atual.grau
                )
                atual = atual.proximo
    
            novo_polinomio.simplificar()
    
            return novo_polinomio
    
    def __mul__(self, outro):
            resultado = Polinomio()
    
            termo_a = self.inicio
    
            while termo_a is not None:
                termo_b = outro.inicio
    
                while termo_b is not None:
                    novo_coeficiente = (
                        termo_a.coeficiente * termo_b.coeficiente
                    )
    
                    novo_grau = termo_a.grau + termo_b.grau
    
                    resultado.inserir(
                        novo_coeficiente,
                        novo_grau
                    )
    
                    termo_b = termo_b.proximo
    
                termo_a = termo_a.proximo
    
            resultado.simplificar()
    
            return resultado
    
    def exibir(self):
            if self.inicio is None:
                return "0"
    
            resultado = ""
            atual = self.inicio
            primeiro = True
    
            while atual is not None:
    
                coeficiente = atual.coeficiente
                grau = atual.grau
    
                if coeficiente != 0:
    
                    if primeiro:
                        if coeficiente < 0:
                            resultado += "-"
                    else:
                        if coeficiente < 0:
                            resultado += " - "
                        else:
                            resultado += " + "
    
                    valor = abs(coeficiente)
    
                    if valor == int(valor):
                        valor = int(valor)
    
                    if grau == 0:
                        resultado += f"{valor}"
    
                    elif grau == 1:
                        if valor == 1:
                            resultado += "x"
                        else:
                            resultado += f"{valor}x"
    
                    else:
                        if valor == 1:
                            resultado += f"x^{grau}"
                        else:
                            resultado += f"{valor}x^{grau}"
    
                    primeiro = False
    
                atual = atual.proximo
    
            return resultado if resultado else "0"
    
    def __str__(self):
            return self.exibir()
    
    
def criar_polinomio(texto):
        valores = texto.split()
        polinomio = Polinomio()
    
        posicao = 0
    
        while posicao < len(valores):
            coeficiente = float(valores[posicao])
            grau = int(valores[posicao + 1])
    
            polinomio.inserir(coeficiente, grau)
    
            posicao += 2
    
        polinomio.ordenar()
    
        return polinomio
    
    
def processar_arquivo(nome_arquivo):
    
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo: #ler arquivo de entrada
            conteudo = arquivo.readlines()
    
        comandos = [] #vai receber cada linha do arquivo de entrada
        for linha in conteudo: #roda cada linha do arquivo de entrada e picota 
            linha = linha.strip()
    
            if linha:
                comandos.append(linha)
    
        indice = 0
    
        while indice < len(comandos):
    
            comando = comandos[indice].lower() #converter comando para minúsculo
            indice += 1
    
            if comando == "+": 
    
                primeiro = criar_polinomio(comandos[indice])
                indice += 1
    
                segundo = criar_polinomio(comandos[indice])
                indice += 1
    
                resposta = primeiro + segundo
    
                print(f"Resultado (+): {resposta}")
    
            elif comando == "-":
    
                primeiro = criar_polinomio(comandos[indice])
                indice += 1
    
                segundo = criar_polinomio(comandos[indice])
                indice += 1
    
                resposta = primeiro - segundo
    
                print(f"Resultado (-): {resposta}")
    
            elif comando == "*":
    
                primeiro = criar_polinomio(comandos[indice])
                indice += 1
    
                segundo = criar_polinomio(comandos[indice])
                indice += 1
    
                resposta = primeiro * segundo
    
                print(f"Resultado (*): {resposta}")
    
            elif comando == "g":
    
                polinomio = criar_polinomio(comandos[indice])
                indice += 1
    
                print(f"Grau: {polinomio.grau()}")
    
            elif comando == "t":
    
                polinomio = criar_polinomio(comandos[indice])
                indice += 1
    
                print(f"Tamanho: {polinomio.tamanho()}")
    
            elif comando == "p":
    
                polinomio = criar_polinomio(comandos[indice])
                indice += 1
    
                print(f"Polinomio: {polinomio}")
    
            elif comando == "a":
    
                valor_x = float(comandos[indice])
                indice += 1
    
                polinomio = criar_polinomio(comandos[indice])
                indice += 1
    
                resultado = polinomio.avaliar(valor_x)
    
                print(f"p({valor_x}) = {resultado}")
    
            else:
                print(f"Operacao desconhecida: '{comando}'")
    
    
if __name__ == "__main__": #ponto de entrada do programa
        import os
    
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        arquivo_entrada = os.path.join(diretorio_atual, "entrada.txt")
    
        processar_arquivo(arquivo_entrada)