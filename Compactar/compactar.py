def compactar(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, "rb") as arquivo:
        dados = arquivo.read()

    codigos = {
        ord("A"): 0b00,
        ord("C"): 0b01,
        ord("G"): 0b10,
        ord("T"): 0b11
    }

    compactado = bytearray()

    byte_atual = 0
    quantidade_bits = 0
    quantidade_nucleotideos = 0

    for nucleotideo in dados:

        if nucleotideo not in codigos:
            continue

        valor = codigos[nucleotideo]

        byte_atual = (byte_atual << 2) | valor
        quantidade_bits += 2
        quantidade_nucleotideos += 1

        # Quando completar 8 bits
        if quantidade_bits == 8:
            compactado.append(byte_atual)

            byte_atual = 0
            quantidade_bits = 0

    # Completa o último byte, caso necessário
    if quantidade_bits > 0:
        byte_atual <<= (8 - quantidade_bits)
        compactado.append(byte_atual)

    with open(arquivo_saida, "wb") as arquivo:

        arquivo.write(
            quantidade_nucleotideos.to_bytes(8, byteorder="big")
        )

        arquivo.write(compactado)

    print("\nArquivo compactado com sucesso!")
    print("Tamanho original:", len(dados), "bytes")
    print("Tamanho compactado:", len(compactado) + 8, "bytes")


def descompactar(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, "rb") as arquivo:
        dados = arquivo.read()

    # Recupera a quantidade original
    quantidade_nucleotideos = int.from_bytes(
        dados[:8],
        byteorder="big"
    )

    dados_compactados = dados[8:]
    nucleotideos = {
        0b00: ord("A"),
        0b01: ord("C"),
        0b10: ord("G"),
        0b11: ord("T")
    }

    resultado = bytearray()

    quantidade_lida = 0

    for byte in dados_compactados:

        # Cada byte possui quatro nucleotídeos
        for deslocamento in (6, 4, 2, 0):

            valor = (byte >> deslocamento) & 0b11

            resultado.append(nucleotideos[valor])

            quantidade_lida += 1

            if quantidade_lida == quantidade_nucleotideos:
                break

        if quantidade_lida == quantidade_nucleotideos:
            break

    with open(arquivo_saida, "wb") as arquivo:
        arquivo.write(resultado)

    print("\nArquivo descompactado com sucesso!")
    print("Tamanho descompactado:", len(resultado), "bytes")


def menu():
    while True:

        print("\n===== COMPACTADOR DE DNA =====")
        print("1 - Compactar arquivo")
        print("2 - Descompactar arquivo")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            entrada = input("Arquivo de entrada: ")
            saida = input("Arquivo compactado: ")

            compactar(entrada, saida)

        elif opcao == "2":

            entrada = input("Arquivo compactado: ")
            saida = input("Arquivo descompactado: ")

            descompactar(entrada, saida)

        elif opcao == "3":

            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")
menu()