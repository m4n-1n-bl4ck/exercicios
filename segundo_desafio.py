# -*- coding: UTF-8 -*-

from random import *

def main():
	
	lista = [randint(0, 5000000) for x in range(500)]
	lista2 = [randint(0, 5000000) for x in range(50000)]

	lista_final = [x for x in lista if x not in lista2]

	print(lista_final)

if(__name__ == "__main__"):
	main()