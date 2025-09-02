# Questão – Controle de Vendas

maior=0
menor=0
vtotal=0
valor=0
produtos=int(input("quantos produtos foram vendidos? "))
for n in range(1, produtos+1):
    valor=int(input(f"qual o valor do produto {n}: "))
    vtotal+=valor
    if valor>50:
        maior+=1
    elif valor<50:
        menor+=1
print(f"valor total de produtos vendidos: {vtotal}")
print(f"A quantidade de produtos vendidos com valor > 50 reais: {maior}")
print(f"A quantidade de produtos vendidos com valor < 50 reais: {menor}")