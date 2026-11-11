# ==========================================
# PRÁTICA 1: O Python como Calculadora
# ==========================================
print("--- Calculadora Básica ---")
print(2 + 3)
print(10 - 4)
print(5 * 5)
print(20 / 4)


# ==========================================
# PRÁTICA 2: O Comando print() e Strings
# ==========================================
print("\n--- Meus Primeiros Textos ---")
# Usando aspas duplas
print("Meu primeiro código em Python!")

# Usando aspas simples (o resultado é o mesmo)
print('Olá, mundo! Usando aspas simples.')


# ==========================================
# PRÁTICA 3: O Zen do Python (Curiosidade)
# ==========================================
print("\n--- Filosofia do Python (Zen) ---")
# Este comando exibe os princípios de design do Python escritos por Tim Peters
import this


# ==========================================
# PRÁTICA 4: Variáveis e Tipos de Dados
# ==========================================
print("\n--- Trabalhando com Variáveis ---")

# Números Inteiros (int)
idade = 26
print("Idade (Inteiro):", idade)

# Números Reais / Ponto Flutuante (float) - note o uso do ponto (.)
altura = 1.75
print("Altura (Float):", altura)

# Textos / Strings (str)
nome = "Luiz Antônio"
print("Nome (String):", nome)

# Booleanos (bool) - True ou False (Sempre com a inicial maiúscula)
programador_ativo = True
print("É programador ativo? (Booleano):", programador_ativo)


# ==========================================
# PRÁTICA 5: Atribuição Múltipla e Tipagem Forte
# ==========================================
print("\n--- Atribuição Múltipla ---")
# Declarando duas variáveis na mesma linha
a, b = 7, "João Moreno"
print("Valor de a:", a)
print("Valor de b:", b)

# ATENÇÃO À TIPAGEM FORTE DO PYTHON:
# O código abaixo geraria um erro se executado porque o Python não soma 
# um número inteiro (int) com uma string (str) automaticamente:
# resultado_erro = a + b 
# print(resultado_erro)