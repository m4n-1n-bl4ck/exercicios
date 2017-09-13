# -*- coding:UTF-8 -*-

def eh_primo(x):
	fator = 2

	if(x == 2):
		return True

	while((x % fator != 0) and (fator <= x / 2)):
		fator = fator + 1

	if(x % fator == 0):
		return False 

	else:
		print("O número {} é primo!" .format(x))
		return True

def main():

	try:
		num = int(input("Insira um numero inteiro: "))
	except:
		print("\nErro, digite novamente")
		main()

	for x in range(2, num + 1):
		eh_primo(x)

if(__name__ == "__main__"):
	main()