
a = 3
b = 2

print("Soma =  ", a + b)
print("Subtração = ", a - b)
print("Multiplicação = ", a * b)
print("Divisão Padrão = ", a / b)
print("Divisão Inteira = ", a // b)
print("Modulo = ", a % b)
print("Exponenciação = ", a ** b)
print()

valor1 = 3
valor2 = 5


print(f"{valor1} == {valor2} ? = ", valor1 == valor2 )
print(f"{valor1} !=  {valor2} ? = ", valor1 != valor2 )
print(f"{valor1} > {valor2} ? = ", valor1 > valor2 )
print(f"{valor1} < {valor2} ? = ", valor1 < valor2 )
print(f"{valor1} >= {valor2} ? = ", valor1 >= valor2 )
print(f"{valor1} <= {valor2} ? = ", valor1 <= valor2 )


# Definindo algumas variáveis de teste
idade = 26
tem_carteira = True
tem_historico_ruim = False

print("--- TESTANDO O AND (E) ---")
# Precisa que AMBAS as condições sejam True para o resultado ser True
pode_dirigir = (idade >= 18) and tem_carteira
print(f"Idade >= 18 AND Tem carteira? = {pode_dirigir}")

print("\n--- TESTANDO O OR (OU) ---")
# Precisa que PELO MENOS UMA condição seja True
tem_desconto = (idade < 18) or (idade > 60)
print(f"Tem direito a desconto (menor de 18 OR maior de 60)? = {tem_desconto}")

print("\n--- TESTANDO O NOT (NEGAÇÃO) ---")
# Inverte o valor lógico de True para False (ou vice-versa)
print(f"Histórico ruim original: {tem_historico_ruim}")
print(f"Invertido com NOT (Não tem histórico ruim): {not tem_historico_ruim}")