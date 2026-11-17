numero, maior, menor = 0 , 0 , 0 
for i in range(0,10):
    numero = int(input(f"Informe um valor {i+1} : "))
    if maior== 0 and menor == 0: 
        menor = numero 
        maior = numero
    if numero < menor: menor = numero
    elif numero > maior: maior = numero
print(f"O maior o e menor número da lista foram {maior} , {menor} respectivamente ")

