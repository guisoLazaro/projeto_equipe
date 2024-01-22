continuar = True

while continuar:
    opcao = input("Escolha uma opção: 1- Contar caractere, incluindo espaços. 2- Contar palavras presentes na grase. 3- Encerrar")
    if opcao == '1':
        frase = input("Digite a frase: ")
        contCaractere = len(frase)
        print(f"Número de caracteres: {contCaractere}")

    elif opcao == '2':
        frase = input("Digite a frase: ")
        numPalavras = len(frase.split())
        print(f"Número de palavras: {numPalavras}")
    elif opcao == '3':
        print("Programa encerrado.")
        continuar = False
    else:
        print("Tente outra opção")


