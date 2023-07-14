"""
1. Actualizar valores en diccionarios y listas
    - Cambia el valor 10 en x a 15. Una vez que hayas terminado,
    x ahora debería ser [ [5,2,3], [15,8,9] ].
    - Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
    - En el directorio_deportes, cambia "Messi" por "Andrés".
    - Cambia el valor 20 en z a 30.
"""
x = [ [5,2,3], [10,8,9] ] 
#Cambiando el valor a x
x[1][0] = 15
print(x)


estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#Cambiando apellido del primer alumno
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)


directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
#Cambiando Messi por Andres
directorio_deportes['fútbol'][0] = 'Andres'
print(directorio_deportes)


z = [ {'x': 10, 'y': 20} ]
#Cambiando el valor y:20 a 30
z[0]['y'] = 30
print(z)


"""
2. Iterar a través de una lista de diccionarios
Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios,
la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociad
"""
def iterateDictionary(estudiantes: list) -> print:
    for estudiante in estudiantes:
        for key, value in estudiante.items():
            print(f"{key} - {value}")

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(estudiantes) 


"""
3. Obtener valores de una lista de diccionarios
Crea una función iterateDictionary2(key_name, 
some_list)que, dada una lista de diccionarios y un nombre de clave,
la función imprima el valor almacenado en esa clave para cada diccionario. 
Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
"""

def iterateDictionary2(key_name, some_list):
    for diccionario in some_list:
        if key_name in diccionario:
            print(diccionario[key_name])
        else:
            print(f"La clave {key_name} no existe en el diccionario")

iterateDictionary2('last_name', estudiantes)

"""
4. Iterar a través de un diccionarios con valores de lista
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos 
listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima
los valores asociados dentro de la lista de cada clave.
"""
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key}" )
        for n in range(len(value)):
            print(f"{value[n]}")

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],  # noqa: E501
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']  # noqa: E501
}
printInfo(dojo)