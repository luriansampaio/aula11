# # Bibliotecas
import random

# #random.randint = números inteiros
# n = random.randint(1,10)
# m = random.randint(1,10)
# print (n,m)

#------------------------------------------------
# Gerar números decimais 
n_decimal = random.uniform(1,10)
numero_decimal = round(n_decimal,3) # arredonda
print(f'{n_decimal:.2f}') #formata para duas casas 
print(numero_decimal)