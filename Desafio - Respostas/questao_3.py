"""
# Questão 03
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra
podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um
algoritmo que encontre o número de pares de substrings que são anagramas.
"""

print("Identificador de anagramas pares!\n")

while True:
    contador = cont = 0
    resultado = []
    palavra = input("Digite uma palavra a ser analisada: ").strip()
    palavra = list(palavra)
    while contador < len(palavra):
        if palavra.count(palavra[contador]) > 1:
            resultado.append(palavra[contador])
            if resultado.count(palavra[contador]) > 2:
                resultado.pop()
            index_1 = palavra.index(palavra[contador])
            index_2 = palavra.index(palavra[contador], contador)
            while cont < 2:
                if index_2 - index_1 > 1:
                    resultado.append("".join(palavra[index_1 + cont:index_2 + cont]))
                    cont += 1
                else:
                    break
            cont = 0
        contador += 1
    print(resultado)
    resposta = input("Deseja analisar outra palavra? [s/n]: ").strip().lower()
    if resposta == 'n':
        break
    else:
        print()
print("\nFIM!!!")
