
ciudadescount = {} # se creea un diccionario 
import csv # para poder leer el archivo csv
with open('../Odalis_ExamenParcial1/Dalziel2016_data.csv', 'r') as T: 
    mi_data = csv.DictReader(T)
    for line in mi_data:  # ciudad que debe ser actualizada  y se utiliza 'for'  par ejecutar el codigo 
#                           en todos los argurmentos  de line
        myciudad = line['loc']
        ciudadescount[myciudad] = ciudadescount.get(myciudad, 0) #'get' permite actualizar el valor si la clave ya está presente
        #                                                           o añadir una nueva clave si la clave no está presente.
        ciudadescount[myciudad] = ciudadescount[myciudad] + 1  # Si la clave no está ya presente, se añadirá la clave y su valor
#                                                                será inicialmente 1
for city in ['CHICAGO', 'LOS ANGELES', 'NEW YORK']: 
    print(city, ciudadescount[city]) # imprime las ciudades y el mumero de registro 

# Funcion 5    
ciudadcases = {} # dicsionario que contiene la suma de la poblacion y nuemro de registros 
import csv 
with open('1dalziel.csv', 'r') as T:  
def avgyear(city, my_csv):
    citypop = ()
    for line in my_csv:
        mycity = line ['loc']
        pop= float (line['pop'])
        if line['cases'] != "NA":
            cases = float (line['cases'])
            citypop[mycity]= citypop.get(mycity,[0,0,0])
            citypop[mycity][0]= citypop[0]+ pop
            citypop[mycity][1]= citypop[1]+ case
            citypop[mycity][2]= citypop[2]+ 1
    for key in citypop:
        if key == city:
            avg_case = 100000*citypop[key][1]/citypop[key][0]
            return print(key, avg_case
    mi_data = csv.DictReader(T)
    for line in mi_data:   
        myciudad = line['loc']  
        pop = float(line['pop'])
        cases = float(line['cases'])# se trasforman los datos a float; es decir no enteros 
        ciudadcases[myciudad] = ciudadcases.get(myciudad, [0,0]) # se obtine el primer valor de la lista 
        ciudadcases[myciudad][0] = ciudadcases[myciudad][0] + pop # se obtine el segundo valor de la
# Primera Funcion                                                                lista (numero de registo actualizado) 
        ciudadcases[myciudad][1] = ciudadcases[myciudad][1] + cases 
def avgcity(city): 
    for city in ciudadcases.keys():  # Keys Crea una lista que contiene las claves del diccionario
        ciudadcases[city][0] = (ciudadcases[city][0] / ciudadcases[city][1])  # se divide la suma de la poblacion por 
    if city in city:                                                              
        for city in ['BALTIMORE','BOSTON','BRIDGEPORT', 'BUFFALO','CHICAGO']:   # en estas ciudades
            print(city,":", round(ciudadcases[city][0],2)) # imprime la ciudad y su promedio
avgcity(city= ciudadcases)
# Fucion de años 
import pandas as pd 

def avgyear(city, my_csv):
    citypop = ()
    for line in my_csv:
        mycity = line ['loc']
        pop= float (line['pop'])
        if line['cases'] != "NA":
            cases = float (line['cases'])
            citypop[mycity]= citypop.get(mycity,[0,0,0])
            citypop[mycity][0]= citypop[0]+ pop
            citypop[mycity][1]= citypop[1]+ case
            citypop[mycity][2]= citypop[2]+ 1
    for key in citypop:
        if key == city:
            avg_case = 100000*citypop[key][1]/citypop[key][0]
            return print(key, avg_case)
# tercera funcion 
def avgyear(city, my_csv):
    citypop = ()
    for line in my_csv:
        mycity = line ['loc']
        pop= float (line['pop'])
        if line['cases'] != "NA":
            cases = float (line['cases'])
            citypop[mycity]= citypop.get(mycity,[0,0,0])
            citypop[mycity][0]= citypop[0]+ pop
            citypop[mycity][1]= citypop[1]+ case
            citypop[mycity][2]= citypop[2]+ 1
    for key in citypop:
        if key == city:
            avg_case = 100000*citypop[key][1]/citypop[key][0]

            return print(key, avg_case)
# Funcion 4 
def avgyear(city, my_csv):
    citypop = ()
    for line in my_csv:
        mycity = line ['loc']
        pop= float (line['pop'])
        if line['cases'] != "NA":
            cases = float (line['cases'])
            citypop[mycity]= citypop.get(mycity,[0,0,0])
            citypop[mycity][0]= citypop[0]+ pop
            citypop[mycity][1]= citypop[1]+ case
            citypop[mycity][2]= citypop[2]+ 1
    for key in citypop:
        if key == city:
            avg_case = 100000*citypop[key][1]/citypop[key][0]
            return print(key, avg_case)
