"""
# Questão 01

Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
A base e altura da escada devem ser iguais ao valor de n.
A última linha não deve conter nenhum espaço.

"""

escada = [" ", " ", " ", " ", " ", " "]

for contador in range(1, 7):
	escada[len(escada) - contador] = "*"
	print("".join(escada))
	