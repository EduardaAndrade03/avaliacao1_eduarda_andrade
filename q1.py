# Questão 1 (Fácil) – Verificação de Número Par ou Ímpar

num = int(input("digite um numero "))
if num%2==0:
    print(f"{num} é par")
else:
    print(f"{num} é impar")
if num>0:
    print(f"{num} é positivo")
elif num<0:
    print(f"{num} é negativo")
elif num==0:
    print(f"{num} é igual a zero")

    