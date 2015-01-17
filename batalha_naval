#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Exercício originário do site codeacademy.com

from random import randint

board = []

for x in range(5):
	board.append(["O"] * 5)

def print_board(board):
	for row in board:
		print(" ".join(row))

print("Vamos jogar Batalha Naval!")
print("Você tem 4 tentativas.")
print_board(board)

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# print(ship_row)
# print(ship_col)

for turn in range(4):
	guess_row = int(input("Adivinhe a Linha: "))
	guess_col = int(input("Adivinhe a Coluna: "))

	if guess_row == ship_row and guess_col == ship_col:
		print("Parabéns, você afundou meu couraçado!")
		print("Fim do jogo.")
		break
	else:
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			print("Oops, isso não é nem mesmo no oceano.")
		elif(board[guess_row][guess_col] == "X"):
			print("Você já tentou esse.")
		else:
			print("Você errou meu couraçado!")
			board[guess_row][guess_col] = "X"
	if turn == 3:
		print("Fim do jogo.")
    
	print("Tentativa ", turn + 1)
	print_board(board)
