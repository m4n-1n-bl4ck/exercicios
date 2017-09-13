# -*- coding: UTF-8 -*-

def main():
	
	try:
		num = int(input("Insira um numero inteiro: "))
	except:
		print("\nErro, digite novamente")
		main()

	lista = [x for x in range(300)]

	try:
		posicao = lista.index(num)
		print("O número {} está na posição {}" .format(num, posicao))
	except:
		print("O número não consta na lista!")



if(__name__ == "__main__"):
	main()