"""
# Questão 02

Débora se inscreveu em uma rede social para se manter em contato com seus amigos.
A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte.
O site considera uma senha forte quando ela satisfaz os seguintes critérios:

	- Possui no mínimo 6 caracteres.
	- Contém no mínimo 1 digito.
	- Contém no mínimo 1 letra em minúsculo.
	- Contém no mínimo 1 letra em maiúsculo.
	- Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+

Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte.
Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser
adicionados para uma string qualquer ser considerada segura.

"""

print("Verificador de senhas fortes!\n"
	  "Para criar uma senha forte siga as intruções:\n"
	  	"- Possui no mínimo 6 caracteres.\n"
		"- Contém no mínimo 1 digito.\n"
		"- Contém no mínimo 1 letra em minúsculo.\n"
		"- Contém no mínimo 1 letra em maiúsculo.\n"
		"- Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+")
while True:
	while True:
		senha = input("Digite uma nova senha:")
		numeros = strUpper = strLower = especiais = 0

		if len(senha) < 6:
			print("Senha deve ter no minímo 6 caracteres!")
		else:
			for contador in senha:
				if contador.isnumeric():
					numeros += 1
				elif contador.isupper():
					strUpper += 1
				elif contador.islower():
					strLower += 1
				elif contador in "!@#$%^&*()-+":
					especiais += 1
			break
	if numeros == 0 or strUpper == 0 or strLower == 0 or especiais == 0:
		print("Senha fraca!")
	else:
		print("Senha forte!")
	resposta = input("Deseja testar outra senha? [s/n]:").strip()[0].lower()
	if resposta == "n":
		break
