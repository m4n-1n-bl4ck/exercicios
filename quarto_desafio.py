# -*- coding:UTF-8 *-*

import string

def cria_alfabeto():

	alfabeto = {}
	num = 1

	for i in range(ord('a'), ord('z') + 1):
		alfabeto.update({chr(i) : num})
		num += 1

	for i in range(ord('A'), ord('Z') + 1):
		alfabeto.update({chr(i) : num})
		num += 1

	return alfabeto

def soma_palavra(alfabeto, palavra):
	num = 0

	for ch in palavra:
		num += alfabeto.get(ch)

	return num

def eh_primo(x):
	fator = 2

	if(x == 2):
		return True

	while((x % fator != 0) and (fator <= x / 2)):
		fator = fator + 1

	if(x % fator == 0):
		print("O número {} não é primo!" .format(x))
		return False 

	else:
		print("O número {} é primo!" .format(x))
		return True

def main():

	palavra = input("Insira uma palavra: ")

	alfabeto = cria_alfabeto()
	num = soma_palavra(alfabeto, palavra)
	eh_primo(num)

main()