# tuplas
tupla1 = () #tupla vacia
print(tupla1)
tupla2 = ('Esto es un texto',) #una tupla con un elemento que es una cadena
print(tupla2)
tupla3 = ('Una cadena', 123) #una tupla con dos elementos
print(tupla3)
tupla4 = ('apple', 2018, 'Samsung', 4.9, 't', True) #una tupla de seis elementos
print(tupla4)

tupla5 = (2, 4.7, 'Nota', 5, 3, 2.9)
print(tupla5[1])
print(tupla5[2])
print(tupla5[3])

tupla6 = (0, 1, 2, 3)
tupla7 = ('A', 'B', 'C')
tupla8 = (tupla6, tupla7)
print(tupla6)
print(tupla7)
print(tupla7[0]) #Muestra solo la tupla 1
print(tupla7[1]) #Muestra solo la tupla 2
print(tupla7[1][0]) #Muestra de la tupla 2 el elemento en el índice 0

#concatenar
tupla9 = ('A', 'B', 'C', 'E')
tupla10 = (1, 2, 3, 4, 5)
tupla11 =tupla9 + tupla10
print(tupla10)

#Repetir
#Crear una tupla con multiples copias de una tupla
tupla12 = (1, 2, 3, 4, 5)
tupla13 = tupla12 * 3
print(tupla13)

#Comparar
#Se usan los operadores convencionales (<, <=, >, >=, ==, !=)
tupla14 = ('Rojas',)
tupla15 = (123,)
tupla16 = ('Rosas',)
tupla17 = ('rosas',)
print((tupla14, tupla15) < (tupla16, tupla17))
print((tupla16, tupla15) == (tupla17, tupla15))

#definicion de una lista
lista = [] #lista vacia
lista1 = ['Este es un texto'] #Una lista con un elemento
lista2 = ['Una cadena', 123] #Una lista de dos elementos
lista3 = [1, 2, 3, 4.5, 'hola', 'a'] #Una lista de seis elementos
print(lista)
print(lista1)
print(lista2)
print(lista3)

lista5 = [0, 1, 2, 3]
lista6 = ["A","B","C"]
lista7 = [lista5, lista6]
print(lista7)
print(lista7[0])#Muestra solo la lista 5
print(lista7[1])#Muestra solo lista 6
print(lista7[1][0])#Muestra la lista 6 el elemento en el indice 0

#concatenar
lista8 = ('A', 'B', 'C', 'E')
lista9 = (1, 2, 3, 4, 5)
lista10 =lista8 + lista9
print(lista10)
print(lista10[2])

#El metodo extend agrega una lista al final de otra lista, la operacion afecta a la lista invocante
nombres1 =["Antonio","Maria","Mabel"]
nombres2 =["Barry","John","Guttag"]
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)

#Repetir
lista11 = (1, 2, 3, 4, 5)
lista12 = lista11 * 3
print(lista12)

#Comparar
#Se usan los operadores convencionales (<, <=, >, >=, ==, !=)
print(["Rojas", 123] < ["Rosas", 123])
print(["Rosas", 123] < ["rosas", 123])
print(["Rosas", 123] < ["Rosas", 23])

#Es posible determinar si un elemento se encuentra en una lista
lista13 = ["Cien","Años","De","Seriedad"]
if "Seriedad" in lista13:
    print("Si esta en la lista")
else:
    print("No esta en la lista")

#Iterando un alista
lista15 = ["Hola","Amigos","Mios"]
for palabra in lista15:#Para cada palabra de la lista
    print(palabra, end=",")#Parametro end evita el salto de linea

#DICCIONARIOS
#Ejmeplo
diccionario = {}#Diccionario vacio
#Diccionario con 4 items o registros
puertos = {
    22:"SSH",
    23:"Telnet",
    80: "HTTP",
    3306: "MySQL"
}
print(puertos)

#EL metodo update agrega items de un diciionario a otro
puertos1 = {
    22:"SSH",
    80:"HTTP"
}
puertos2 = {
    53:"DNS",
    443:"HTTPS"
}
print(puertos1)
puertos1.update(puertos2)
print(puertos1)

#Comparar
#Se mira si los diccionarios tienen los mismos items
a ={123:"Rojas",87:"Rosas"} == {87:"Rosas", 123:"Rojas", 78:"Otro"}
print(a)

#Accediendo a un item con la clave dada
puertos3 = {
    22:"SSH",
    23:"Telnet",
    80:"HTTP",
    3306:"MySQL"
}
protocolo = puertos3[22]
print(protocolo)

#Eliminar item con la clave dada
calificaciones = {
    "Alumno1":5,
    "Alumno2":3,
    "Alumno3":4,
    "Alumno4":3
}
print(calificaciones)
del calificaciones["Alumno3"]
print(calificaciones)

#Iterar un diccionario
#Usar el ciclo for y el metodo items para obtener los items de un diccionario
dicPuertos = {
    22:"SSH",
    23:"Telnet",
    80:"HTTP"
}
for x,y in dicPuertos.items():
    print(x, "-> ", y)