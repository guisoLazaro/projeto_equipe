contador = True
while(contador == True):
    print("Digite algo para a contagem de caracteres:")
    texto = input()
    tamanho = len(texto)
    print("A quantidade de caracteres desse texto é igual á:", tamanho)
    print("Deseja continuar o programa?:")
    print("(Para interromper o programa digite não)")
    print("(Para continuar digite qualquer outra coisa)")
    resposta = input()
    if(resposta == 'nao' or resposta == 'não'):
      print("Ok")
      contador = False