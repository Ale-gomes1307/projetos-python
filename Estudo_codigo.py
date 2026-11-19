# Exercício 1 — Apresentação
"""
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
print("Olá,", nome,"!", "você tem", idade, "anos.")

"""
# Exercício 2 — Calculadora de soma
"""
nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota_final = float(nota1) + float(nota2)
print("A soma das notas é:", nota_final)

"""
# Exercício 3 — Calculando a média

"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("A média das notas é:", media)
"""

#Exercício 4 — Maior de idade
"""
idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade")
"""
# Exercício 5 — Aprovado ou reprovado

"""
nota = float(input("Digite a sua nota: "))
if nota >= 7:
    print("Parabéns! Você foi aprovado.")
elif nota >= 5:
    print("Voce esta de recuperação")
else:
    print("Infelizmente você foi reprovado.")

"""
# Exercício 7 — Contagem
"""
for i in range(1, 11):
    print(i)
"""
# Exercício 8 — Tabuada
"""
numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
"""

#Exercício 9 — Somando números

"""
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
numero4 = int(input("Digite o quarto número: "))
numero5 = int(input("Digite o quinto número: "))
soma = numero1 + numero2 + numero3 + numero4 + numero5
print("A soma dos números é:", soma)
"""
# Exercício 10 — Caixa eletrônico
"""
saldo_inicial = 1000
saque = float(input("Digite o valor que deseja sacar: "))
if saque <= saldo_inicial:
    saldo_final = saldo_inicial-saque
    print("Saque realizado com sucesso! Seu saldo final é:", saldo_final)
else:
    print("Saldo insuficiente para realizar o saque.")

"""
"""
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

print(f"Olá, {nome}! daqui a 5 anos você terá {idade +5} anos.")
"""
"""
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
daqui_a_cinco_anos = idade +5 

print(f"Olá, {nome}! daqui a 5 anos você terá {daqui_a_cinco_anos} anos.")

"""
"""
idade = int(input("Digite a sua idade: "))
cnh = input("Você possui CNH? (sim/não): ")
verificador = idade >=18 and cnh == "sim"

if verificador == True:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

    """
"""
usuario = input("Digite o seu nome de usuario: ")
senha = input("Digite a sua senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso!")
else:
    print("Usuario ou senha incorretos.")
"""

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
frutas.append("manga")
print(frutas)
contagem = len(frutas)
print("O número de frutas na lista é:", contagem)