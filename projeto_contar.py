frase = input ("Insira um texto/palavra: ")

numero_letras_contar_espacos = len(frase)
print(f'Número de letras com espaços é: {numero_letras_contar_espacos}')

numero_letras_contar_sem_espacos = len(frase)-frase.count(" ")
print(f'Número de letras com espaços é: {numero_letras_contar_sem_espacos}')