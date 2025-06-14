import datetime

#Variavel para armazenar o ano atual
ano_atual = datetime.datetime.now().year

#Entrada de dados do usuário
nome = input("Digite seu nome: ") 
ano_nascimento = int(input("Digite a ano do seu nascimento: "))

#Exibição do nome do usuário
print ("Seu nome é " + nome) 

#Remoção de espaços em branco
nome = nome.replace(" ","") 

#Exibição do tamanho do nome do usuário
print("Seu nome tem o total de letras igual: "+ str(len(nome)))

#Cálculo da idade do usuário
idade = ano_atual - ano_nascimento

#Exibição da idade do usuário
print("Sua idade é: " + str(idade) + " anos")