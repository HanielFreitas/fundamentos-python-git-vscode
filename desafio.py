# Desafio 1 - Bônus de Salário

#constantes
constantes = 1000

#Variáveis de entrada de dados
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
bonus = float(input("Porcentagem do bônus recebido: "))
valor_bonus = constantes + salario * bonus

#Exibição do nome do usuário
print(f"Seu nome é {nome}, o valor do bônus foi de: {valor_bonus} reais")
