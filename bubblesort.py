#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Implementação de código de ordenação bubble sort
# 

tamanho = int(input("Informe o tamanho do vetor: "))
print()
vetor = []
loop = 0

# Alimentando o vetor
for n in range(tamanho):
    i = n+1
    numero = int(input("Entre com o %dº número: " %i)) # %d é um marcador de número inteiro
    vetor.append(numero)

# Aqui acontece o Bubble Sort (ordenação)
for a in range(tamanho):
    for b in range(tamanho-1): # tamanho-1 para evitar out of range
        if (vetor[b] > vetor[b+1]):
            auxiliar = vetor[b]
            vetor[b] = vetor[b+1]
            vetor[b+1] = auxiliar

        loop = loop + 1

# Imprime o vetor ordenado
print()
print(vetor)
print()
print("O laço de ordenação executou %d vezes." %loop)
