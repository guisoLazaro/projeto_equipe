pararPrograma = False
while(pararPrograma == False):
    palavra = input("Digite uma palavra ou 0 para parar: ")
    if(palavra != '0'):
        quantidadeCaracteres = len(palavra)
        quantidadePalavras = len(palavra.split())
    else:
        pararPrograma = True
        break
    print(f"Quantidade de caracteres digitados: {quantidadeCaracteres}")
    if(quantidadePalavras > 1):
        print(f"Quantidade de palavras digitadas: {quantidadePalavras}")
    else:
        print("Foi digitado somente uma palavra")
    
    
