########################################################################
#						      Librerías							       #
########################################################################

import json
from os import system

########################################################################
#						      Funciones							       #
########################################################################

def clear(Espaciado):	#	Pequeña funcion que simula un clear, además recibe un entero para centrar
						#	el texto que lo sigue a continuación.
	system('clear')
	print("\n"*Espaciado)

def Pausa():

	input('\n		  "Pusa enter" para volver al menú...')

def ListarPeliculas(Catalogo):	#	Recibe el catálogo e imprime por pantalla el título, año y duración de esta
	for pelicula in Catalogo:
		print("		=========================================")
		print("		Título:		",pelicula["title"])
		print("		Año:		",pelicula["year"])
		print("		Duración:	",pelicula["duration"].replace("PT","").replace("M",""),"min")
	print("		=========================================")

def ListarPelActores(Catalogo):	#	Recibe el catalogo e imprime por pantalla el título y el numero de actores de las peliculas
	for pelicula in Catalogo:
		print("		=========================================")
		print("		Título:		",pelicula["title"])
		print("		Actores:	",len(pelicula["actors"]))

def BuscadorEnSinopsis(C1,C2,Catalogo):		#	Recibe 2 palabras por teclado. Comprueba si están en la sinopsis, y si están
	lista=[]								#	las añade a una lista.
	for pelicula in Catalogo:
		sinopsis=pelicula["storyline"].upper()
		if sinopsis.count(C1)!=0 and sinopsis.count(C2)!=0:
			lista.append(pelicula["title"])
	return lista

def BuscadorPorActor(Actor,Catalogo):
	

########################################################################
#						   Código Principal							   #
########################################################################

with open("movies.json","r") as fichero:

	Catalogo = json.load(fichero)

	while True:													############################
																#			Menú           #
		clear(0)												############################
		print('''\n\n	Elige una de las siguientes opciones:				

	 1. Listar el título, año y duración de todas las películas.
	 2. Mostrar los títulos de las películas y  el número de 
	    actores/actrices que tiene cada una.
	 3. Buscar peliculas por palabras en sinopsis
	 4. Mostrar las películas en las que ha trabajado un actor dado.
	 5. Buscar pelicula por fechas
	 0. Salir
			''')
		
		try:		#	Uso un try por si el usuario introduce un valor nulo o un caracter no entero. 

			opcion=int(input("\n		Opción:  "))

		except:		#	Error:

			print('\n		Debes introducir una opción válida')		
			Pausa()
		else:		#	Si introduce un entero ejecuta una de las siguientes opciones.

			if opcion==0:		#############
								#	Salir   #
				clear(0)		#############
				break

			if opcion==1:
				clear(0)
				ListarPeliculas(Catalogo)
				Pausa()

			if opcion==2:
				clear(0)
				ListarPelActores(Catalogo)
				Pausa()

			if opcion==3:
				clear(10)
				print("			Buscador por palabras (en inglés):")		
				C1=input("			Coincidencia 1 >>> ").upper()
				C2=input("			Coincidencia 2 >>> ").upper()
				lista=BuscadorEnSinopsis(C1,C2,Catalogo)
				print("\n			Se han econtrado las siguientes películas:\n")
				try:
					if len(lista)>0:
						print("\n			Se han econtrado las siguientes películas:\n")
						for pelicula in lista:
							print("			>",pelicula)
				except:
					print("\n			No se han econtrado películas\n")
				Pausa()

			if opcion==4:
				clear(10)
				print("			Buscador por actor:")		
				Actor=input("			Nombre >>> ").upper().replace(" ","").replace(".","")

				Pausa()

			if opcion==5:

				Pausa()