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

def ListarProvincias(Fichero):	#	Devuelve una lista de todas las provinias del xml

	provincias=Fichero.xpath('//RADAR/../../NOMBRE/text()')

	return provincias

def ListarCarreteras(Fichero,Provincia):	#	Recibe una provincia y devuelve una lista de las carreteras que tiene

	carreteras=Fichero.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/DENOMINACION/text()'%Provincia)
	return carreteras

def ContarRadares(Fichero,Provincia):	#	Recibe una provincia y devuelve un entero del total de radares que hay en ella

	TotalRadares=Fichero.xpath('count(//PROVINCIA[NOMBRE="%s"]/CARRETERA/RADAR)'%Provincia)
	return int(TotalRadares)

def ValidarProvincia(Fichero,Provincia):	# Recibe una provincia y devuelve verdadero si existe
	Aparece=int(Fichero.xpath('count(//PROVINCIA[NOMBRE="%s"])'%Provincia))
	if Aparece!=0:
		return True
	else:
		return False

def ValidarCarretera(Fichero,Carretera):	# Recibe una carretera y devuelve verdadero si existe
	Aparece=int(Fichero.xpath('count(//CARRETERA[DENOMINACION="%s"])'%Carretera))
	if Aparece!=0:
		return True
	else:
		return False

def ProvinciasPorCarretera(Fichero,Carretera):	#	<<< Recibe una carretera y devuelve una lista con las provincias por las que pasa
	provincias=Fichero.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()'%Carretera)
	return provincias

def ContarRCarretera(Fichero,Carretera):	#	<<< Recibe una carretera y devuelve un entero del total de radares
	TotalR=Fichero.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)'%Carretera)
	return int(TotalR)

def DiccionarioRadares(fichero,carretera):		#	<<< Esta funcion crea un diccionario de los radares a partir de una carretera
	lista=[]

	for i in range(0,ContarRCarretera(fichero,carretera)):
		PuntoInicial=[]
		PuntoInicial.append(fichero.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/PK/text()'%carretera)[i])
		PuntoInicial.append(fichero.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()'%carretera)[i])
		PuntoInicial.append(fichero.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'%carretera)[i])
		PuntoFinal=[]
		PuntoFinal.append(fichero.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_FINAL/PK/text()'%carretera)[i])
		PuntoFinal.append(fichero.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_FINAL/LATITUD/text()'%carretera)[i])
		PuntoFinal.append(fichero.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_FINAL/LONGITUD/text()'%carretera)[i])
		Sentido=fichero.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/SENTIDO/text()'%carretera)[i]
		Radar={"PuntoInicial":PuntoInicial,"PuntoFinal":PuntoFinal,"Sentido":Sentido}
		lista.append(Radar)

	return lista

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
			provincia=input("			>>> ").title()	
			
			if ValidarProvincia(fichero,provincia):	#	Valido la provincia con una funcion que devuelve true o false
				clear(0)
				print("			Carreteras de",provincia,":")		#	Si existe, listo todo
				for carretera in ListarCarreteras(fichero,provincia):
					print("		  >>>",carretera)
				print("			Y tiene un total de",ContarRadares(fichero,provincia),"radares")
				Pausa()
			else:
				clear(10)
				print("			Esa provincia no existe")	#	Si no existe muestra un error
				Pausa()

		if opcion==4:
			clear(10)
			print("			Introduce una carretera")		
			carretera=input("			>>> ").title()
			if ValidarCarretera(fichero,carretera):	#	Valido la carretera con una funcion que devuelve true o false
				clear(0)
				print("			La carretera",carretera,"pasa por:")	#	Si existe, listo todo
				for provincia in ProvinciasPorCarretera(fichero,carretera):
					print("			-",provincia)
				print("			Y tiene",ContarRCarretera(fichero,carretera),"radares.")
				Pausa()
			else:
				clear(10)
				print("			Esa carretera no existe")	#	Si no existe muestra un error
				Pausa()

		if opcion==5:
			clear(10)
			print("			Introduce una carretera")		
			carretera=input("			>>> ").title()
			if ValidarCarretera(fichero,carretera):	#	Valido la carretera con una funcion que devuelve true o false
				clear(0)							#	Si existe, listo todo
				print("			La carretera tiene",ContarRCarretera(fichero,carretera),"radares.")
				print("			La localización de estos es:")
				for radar in DiccionarioRadares(fichero,carretera):

					LatitudInicial=radar["PuntoInicial"][1]
					LongitudInicial=radar["PuntoInicial"][2]
					LatitudFinal=radar["PuntoFinal"][1]
					LongitudFinal=radar["PuntoFinal"][2]
					print("		========================================")
					print("		Radar:	")
					print("		 -Punto km inicial >>>",radar["PuntoInicial"][0])
					print("		   -Latitud >>>",LatitudInicial)
					print("		   -Longitud >>>",LongitudInicial)
					print("		 -Punto km inicial >>>",radar["PuntoFinal"][0])
					print("		   -Latitud >>>",LatitudFinal)
					print("		   -Longitud >>>",LongitudFinal)
					url='https://www.openstreetmap.org/directions?engine=graphhopper_car&route='+LatitudInicial+'%2C'+LongitudInicial+'%3B'+LatitudFinal+'%2C'+LongitudFinal+'#map=12/'+LatitudInicial+'/'+LongitudInicial+'&layers=N'
					print("		 ",url)
				print("		========================================")
				Pausa()
			else:
				clear(10)
				print("			Esa carretera no existe")	#	Si no existe muestra un error
				Pausa()