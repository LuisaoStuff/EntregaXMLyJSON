########################################################################
#						      Librerías							       #
########################################################################

import json
from os import system
from datetime import datetime	#	Importo esta librería para validar la fecha en el ultimo ejercicio

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

def ValidarActor(Actor,Catalogo):		#	Recibe un actor y devuelve verdadero si lo encuentra
	indicador=False
	for pelicula in Catalogo:
		if Actor in pelicula["actors"]:
			indicador=True
	return indicador


def Filmografia(Actor,Catalogo):		#	Recibe un actor y añade a una lista las peliculas en las que aparece.
	lista=[]
	for pelicula in Catalogo:
		if Actor in pelicula["actors"]:
			lista.append(pelicula["title"])
	return lista

def ValidarFecha(Fecha):
	try:
		Fecha = datetime.strptime(Fecha, '%Y-%m-%d')
		return True
	except:
		print("\n			Introduce una fecha correcta")
		return False

def FiltrarPorFechas(F1,F2,Catalogo):
	lista=[]
	F1=int(F1.replace("-",""))
	F2=int(F2.replace("-",""))
	for pelicula in Catalogo:
		Fecha=int(pelicula["releaseDate"].replace("-",""))
		if F1<Fecha and F2>Fecha:
			lista.append(pelicula["title"])
	return lista



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
				if len(lista)>0:
					print("\n			Se han econtrado las siguientes películas:\n")
					for pelicula in lista:
						print("			>",pelicula)
				else:
					print("\n			No se han econtrado películas\n")
				Pausa()

			if opcion==4:
				clear(10)
				print("			Buscador por actor:")		
				Actor=input("			Nombre >>> ").title()
				if ValidarActor(Actor,Catalogo):
					print("			",Actor,"aparece en:")
					for pelicula in Filmografia(Actor,Catalogo):
						print("			>",pelicula)
				else:
					print("			",Actor,"no aparece en la lista.")
				Pausa()

			if opcion==5:
				clear(10)
				print("			El formato es YYYY-MM-DD\n\n")
				
				print("			Primera fecha:")		#	\
				F1=input("			Fecha >>> ")		#	|
				while ValidarFecha(F1)==False:			#	|
					F1=input("			Fecha >>> ")	#	|	Valido el formato de las fechas
				print("			Segunda fecha:")		#	|
				F2=input("			Fecha >>> ")		#	|
				while ValidarFecha(F2)==False:			#	|
					F2=input("			Fecha >>> ")	#	/
				try:
					print("			Se han encontrado",len(FiltrarPorFechas(F1,F2,Catalogo)),"películas:")	#	Si la lista devuelta por la funcion
					for pelicula in FiltrarPorFechas(F1,F2,Catalogo):										#	tiene longitud, la imprime
						print("			> ",pelicula)
				except:
					print("			No se han encontrado peliculas")			#	Si no, significa que no ha encontrado ninguna pelicula

				Pausa()