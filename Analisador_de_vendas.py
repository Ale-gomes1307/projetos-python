# Projeto: Analisador de Vendas

"""
 O programa deverá:
1. Perguntar quantas vendas serão registradas.
2. Receber o valor de cada venda.
3. Armazenar os valores.
4. Calcular o faturamento total.
5. Calcular a média das vendas.
6. Identificar a maior venda.
7. Identificar a menor venda.
8. Mostrar um relatório final.
"""

# 1. Perguntar quantas vendas serão registradas
vendas_registradas = int(input("Quantas vendas serão registradas? "))

# 2. Criar uma lista para armazenar as vendas
vendas = []

# 3. Criar um loop para receber os valores
for i in range (vendas_registradas):
    valor_venda = float(input(f"Digite o valor da venda {i + 1}: "))
    vendas.append(valor_venda)

# 4. Calcular o faturamento total
faturamento_total = sum(vendas)

# 5. Calcular a média das vendas
media_das_vendas = faturamento_total / vendas_registradas

# 6. Identificar a maior venda
maior_venda = max(vendas)

# 7. Identificar a menor venda
menor_venda = min(vendas)

# 8. Exibir o relatório final
print("\n--- Relatório de Vendas ---")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Média das vendas: R$ {media_das_vendas:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")
