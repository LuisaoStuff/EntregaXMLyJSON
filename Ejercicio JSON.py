########################################################################
#			      Librerías				       #
########################################################################

import json
from os import system
from datetime import datetime	#	Importo esta librería para validar la fecha en el ultimo ejercicio
import webbrowser

########################################################################
#			      Funciones				       #
########################################################################

def fehInstalado():							#######################################################
	system('whereis feh > salida.txt')				#   Comprueba  si  tienes instalado  el paquete feh   #
	clear(7)							#   para luego poder ejecutar el  comando. Si no lo   #
	with open("salida.txt","r") as Salida:				#   tienes instalado, te da la opcion de instalarlo   #
		if Salida.readlines()[0]=='feh:\n':			#######################################################
			print('''		Parece que no tienes instalado el paquete "feh"
		Si desea que durante la ejecución de este python
		se puedan mostrar las imágenes de los personajes
		debería instalarlo.
				''')
			Afirmacion=['YES','Y','SI','S']
			Eleccion=input('		¿Desea instalar el paquete "feh"?	').upper()
			if Eleccion in Afirmacion:
				system('sudo apt-get install -y feh')
				Miniaturas=True
			else:
				Miniaturas=False
		else:
			Miniaturas=True
	Salida.close()
	system('rm salida.txt')
	return Miniaturas

def Desinstalar_feh():
	system('whereis feh > salida.txt')					#############################################
	clear(10)								#   Al final del programa te da la opcion   #
	with open("salida.txt","r") as Salida:					#   de desinstalar el paquete feh	    #
		if Salida.readlines()[0]!='feh:\n':				#############################################
			Afirmacion=['YES','Y','SI','S']
			Eleccion=input('	   Antes de salir, ¿desea desinstalar el paquete "feh"?	').upper()
			if Eleccion in Afirmacion:
				system('sudo apt-get remove -y feh')
	Salida.close()
	system('rm salida.txt')

def clear(Espaciado):		#	Pequeña funcion que simula un clear, además recibe un entero para centrar
	system('clear')		#	el texto que lo sigue a continuación.
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
	lista=[]				#	las añade a una lista.
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

def ValidarFecha(Fecha):		#	Recibe una fecha y valida que tenga el formato YYYY-MM-DD
	try:
		Fecha = datetime.strptime(Fecha, '%Y-%m-%d')
		return True
	except:
		print("\n			Introduce una fecha correcta")
		return False

def FiltrarPorFechas(F1,F2,Catalogo):	#	Recibe dos fechas. Si hay una pelicula cuya fecha de estreno está
	lista=[]							#	entre esas dos, la añade a una lista.
	F1=int(F1.replace("-",""))					#	\
	F2=int(F2.replace("-",""))					#	|	Convierto las fechas en enteros para
	for pelicula in Catalogo:					#	|	poder compararlas en el "if"
		Fecha=int(pelicula["releaseDate"].replace("-",""))	#	/
		if F1<Fecha and F2>Fecha:
			lista.append(pelicula["title"])
	return lista

def MediaMasAlta(Lista,Catalogo):	#	Recibe una lista de peliculas y el catalogo completo. Devuelve las 3 mejores con url y media
	ListaFinal=[]
	for pelicula in Catalogo:
		if pelicula["title"] in Lista:
			film=[]								#	Inicializo una lista con el título la media de notas
			film.append(pelicula["title"])					#	y la url del poster
			film.append(sum(pelicula["ratings"])/len(pelicula["ratings"]))
			film.append(pelicula["posterurl"])
			ListaFinal.append(film)						#	Añado la lista film a la lista final de peliculas
	ListaFinal=sorted(ListaFinal, key=lambda nota: nota[1],reverse=True)		#	Ordeno la lista por calificaciones de mayor a menor
	return ListaFinal[0:3]								#	y devuelvo solo las 3 primeras.


########################################################################
#			   Código Principal			       #
########################################################################

with open("movies.json","r") as fichero:

	Catalogo = json.load(fichero)

	Posters=fehInstalado()

	while True:										############################
												#	    Menú           #
		clear(0)									############################
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
						#   Salir   #
				clear(0)	#############
				Desinstalar_feh()
				clear(0)
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
				clear(6)
				print("			El formato es YYYY-MM-DD\n\n")
				print("			Primera fecha:")		#	\
				F1=input("			Fecha >>> ")		#	|
				while ValidarFecha(F1)==False:				#	|
					F1=input("			Fecha >>> ")	#	|	Valido el formato de las fechas
				print("			Segunda fecha:")		#	|
				F2=input("			Fecha >>> ")		#	|
				while ValidarFecha(F2)==False	:			#	|
					F2=input("			Fecha >>> ")	#	/
				try:
					clear(0)
					ListaPeliculas=FiltrarPorFechas(F1,F2,Catalogo)			#	Filtro primero las peliculas entre las dos fechas
					for pelicula in MediaMasAlta(ListaPeliculas,Catalogo):		#	Despues uso esa lista para encontrar las 3 con
						print("	>",pelicula[0],"-",round(pelicula[1],2))	#	puntuacion mas alta e imprimo los datos.
						if Posters:			#	Si se ha instalado "feh" se utiliza
							system('feh -Zqa 125 --title "{}" {} &2> /dev/null'.format(pelicula[0],pelicula[2]))
						else:				#	Si no, utiliza la librería webbrowser
							webbrowser.open(pelicula[2])
					Pausa()
				except:
					print("			No se han encontrado peliculas")		#	Si no, significa que no ha encontrado ninguna pelicula
					Pausa()
