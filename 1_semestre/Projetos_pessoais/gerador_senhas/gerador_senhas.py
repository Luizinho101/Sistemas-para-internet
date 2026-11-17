
import random

alfabeto_maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alfabeto_minusculo = ['1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numero_aleatorio = random.randint(0,9)

senha = []

tamanho = int(input("Informe o tamanho da senha : "))

for i in range(0, tamanho):
    alfabeto = random.randint(0,33)
    senha.append(alfabeto_minusculo[alfabeto])
    
print(f"Sua senha é : {senha}")
