import os 
import random

def numeros_aleatorios():
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    return num1, num2


def calcular_numeros(x, y):
    soma = x + y
    subtracao = x - y
    multiplicacao = x * y
    
    if y != 0:
        divisao = x / y
    else:
        divisao = "Não é possível dividir por 0."

    return soma, subtracao, multiplicacao, divisao

num1, num2 = numeros_aleatorios()
soma, sub, mult, div = calcular_numeros(num1, num2)

print(f"Números gerados: {num1} e {num2}")
print(f'Soma: {soma}')
print(f'Subtração: {sub}')
print(f'Multiplicação: {mult}')
print(f'Divisão: {div}')


