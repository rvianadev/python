#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Breno Rodrigues - brenofeliphe@gmail.com
# Mega Sena - number generator
# 11/01/2015
# adapted from:
#------------------------------------------------
# Gerador de números para a Quina
# Versão 1.0
# Rodrigo Viana de Oliveira - roviol@gmail.com
# 04/01/2015

from random import randint

print()
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print()
bilhetes = int(input('Quantos bilhetes deseja jogar? '))
dezenas = int(input('Deseja apostar com 6, 7 ou 8 dezenas? '))
print()
for n in range(1, bilhetes + 1):
	bilhete = []
	for z in range(dezenas):
		bilhete.append(randint(1,60))
	print('Bilhete %d: ' % n, bilhete)
print()
print ('               BOA SORTE!!!             ')
print()
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print()
