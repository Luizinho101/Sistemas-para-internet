
#exibindo valores na tela

for i in range(1 ,9):
    print(f"valor na tela : {i}")


#Usar for para exibir uma lista de frutas

frutas = ["maçã", "banana","caju","manga","abacaxí"]

contador = 0

for x in frutas:
    print(f"Fruta : {frutas[contador]}")
    contador += 1


#Media de 5 valore

media = 0
testador = 1

for teste  in range(0, 5):
    media += float(input(f"Informe o valor {testador} : "))
    testador += 1

print(f"Media : {media/(testador-1)}")