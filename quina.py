#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Gerador de números para a Quina
# Verso 1.1
# Corrigido o bug de dezenas repetidas no mesmo bilhete
# Os bilhetes são apresentados com as dezenas ordenadas
# O valor total da aposta é mostrado no final do programa
# Rodrigo Viana de Oliveira - roviol@gmail.com
# 23/07/2017

# Gerador de números para a Quina
# Versão 1.0
# Rodrigo Viana de Oliveira - roviol@gmail.com
# 04/01/2015

from random import randint

print()
print('$' * 48)
print()
bilhetes = int(input('Quantos bilhetes deseja jogar? '))
dezenas = int(input('Deseja apostar com 5, 6 ou 7 dezenas? '))
if dezenas == 5:
	total = bilhetes * 1.5
if dezenas == 6:
	total = bilhetes * 9
if dezenas == 7:
	total = bilhetes * 31.5
print()
for n in range(1, bilhetes + 1):
	bilhete = []
	for z in range(dezenas):
		duplicado = 1
		contador = 0
		while duplicado == 1:
			numero = randint(1,80)
			while contador < len(bilhete):
				for x in range(len(bilhete)):
					if numero == bilhete[x]:
						numero = randint(1,80)
						contador = 0
						break
					else:
						contador += 1
			bilhete.append(numero)
			duplicado = 0

	bilhete.sort()
	print('Bilhete %d: ' % n, bilhete)
print()
print("-" * 48)
print("Valor total da aposta é R$ %.2f" % total)
print("-" * 48)
print()
print ("               BOA SORTE!!!             ")
print()
print("$" * 48)
print()
