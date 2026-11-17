
import random

vetor_caracteres = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','@','!',',','.','&','*']


senha = []
input_opcoes = 0
caractere = 0


tamanho = int(input("Informe o tamanho da senha : "))

print(" Digite 1 para adicionar numeros a senha : ")

print(" Digite 2 para adicionar letras  e numeros a senha : ")

print(" Digite 3 para adicionar , letras e numeros especiais a senha : ")

input_opcoes = int(input(" Escolha uma das 3 opções : "))


for i in range(0, tamanho):

    if input_opcoes == 1:
        caractere = random.randint(0,9)
    elif input_opcoes == 2:
        caractere = random.randint(0,34)
    elif input_opcoes == 3:
        caractere = random.randint(0,40)


    senha.append(vetor_caracteres[caractere])

senha2 = ''.join(senha)
    
print(f"Sua senha é : {senha2}")
