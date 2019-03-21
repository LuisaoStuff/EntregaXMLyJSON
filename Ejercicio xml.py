########################################################################
#						      Librerías							       #
########################################################################

from lxml import etree
from os import system	#	Esta librería la importo para usar el comando clear
#							y mantener de este modo una salida por pantalla limpia

########################################################################
#						      Funciones							       #
########################################################################

def clear(Espaciado):	#	Pequeña funcion que simula un clear, además recibe un entero para centrar
						#	el texto que lo sigue a continuación.
	system('clear')
	print("\n"*Espaciado)

def Pausa():

	input('\n		  "Pusa enter" para volver al menú...')

def ListarProvincias(Fichero):

	provincias=Fichero.xpath('//RADAR/../../NOMBRE/text()')

	return provincias

def ListarCarreteras(Fichero,Provincia):

	carreteras=Fichero.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/DENOMINACION/text()'%Provincia)
	return carreteras

def ContarRadares(Fichero,Provincia):

	TotalRadares=Fichero.xpath('count(//PROVINCIA[NOMBRE="%s"]/CARRETERA/RADAR)'%Provincia)
	return int(TotalRadares)

def ValidarProvincia(Fichero,Provincia):

	Aparece=int(Fichero.xpath('count(//PROVINCIA[NOMBRE="%s"])'%Provincia))
	if Aparece!=0:
		return True
	else:
		return False

def ValidarCarretera(Fichero,Carretera):

	Aparece=int(Fichero.xpath('count(//CARRETERA[DENOMINACION="%s"])'%Carretera))
	if Aparece!=0:
		return True
	else:
		return False

def ProvinciasPorCarretera(Fichero,Carretera):

	provincias=Fichero.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%Carretera)
	return provincias

########################################################################
#						   Código Principal							   #
########################################################################

fichero = etree.parse('Radares.xml')

while True:													############################
															#			Menú           #
	clear(0)												############################
	print('''\n\n		Elige una de las siguientes opciones:				

		1. Mostrar el nombre de las provincias de las 
		   que tenemos información sobre radares.
		2. Mostrar la cantidad  de radares de los que 
		   tenemos información.
		3. Mostrar el nombre de las carreteras de una
		   provincia y la cantidad de radares.
		4. Muestra las provincias por la que pasa una
		   carretera y sus respectivos radares.
		5. Cuenta los radares que tiene una carretera 
		   y muestra la localizacion de estos.
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
			for provincia in ListarProvincias(fichero):

				print("		-",provincia)

			Pausa()

		if opcion==2:
			Total=fichero.xpath('count(//RADAR)')
			clear(10)
			print("			El total de radares es:",int(Total))
			print("\n"*10)
			input("					     Pulsa enter para volver al menú...")

		if opcion==3:
			clear(10)
			print("			Introduce una provincia")		
			provincia=input("			>>> ").title()	# 	AÑADIR VALIDACIÓN DE LA PROVINCIA Y SI NO APARECE MOSTRAR UN ERROR
			
			if ValidarProvincia(fichero,provincia):
				clear(0)
				print("			Carreteras de",provincia,":")
				for carretera in ListarCarreteras(fichero,provincia):
					print("		  >>>",carretera)
				print("			Y tiene un total de",ContarRadares(fichero,provincia),"radares")
				Pausa()
			else:
				clear(10)
				print("			Esa provincia no existe")
				Pausa()

		if opcion==4:
			clear(10)
			print("			Introduce una carretera")		
			carretera=input("			>>> ").title()	# 	AÑADIR VALIDACIÓN DE LA PROVINCIA Y SI NO APARECE MOSTRAR UN ERROR
			if ValidarCarretera(fichero,carretera):

				Pausa()
			else:
				
				Pausa()

		if opcion==5:
			Pausa()