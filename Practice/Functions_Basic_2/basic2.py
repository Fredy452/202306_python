"""
Cuenta regresiva
Crea una función que acepte un número como entrada. 
Devuelve una lista nueva que cuente de uno en uno, 
desde el número (como elemento 0) hasta 0 (como último elemento). 
Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
"""

def countdown(n: int) -> list:
    count = []
    for n in range(n, -1, -1):
        count.append(n)
    return count

print(countdown(10))


"""
Imprimir y devolver 
Crea una función que reciba una lista con dos números. 
Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2
"""
def print_and_return(a: list) -> int:
    print(a[0])
    return a[1]

print("Se retorna ", print_and_return([1, 2]))

"""
Primero más longitud 
Crea una función que acepte una lista 
Devuelva la suma del primer valor de la lista, más la longitud de la lista.
"""
def first_sum_long(ar: list) -> int:
    sum = ar[0] + len(ar)
    return sum

print("La suma del primer valor más la longitud es: ", first_sum_long([1,2,3,4,5]))


"""
Valores mayores que el segundo
Escribe una función que acepte una lista
Cree una nueva que contenga solo los valores de la lista original 
que sean mayores que su segundo valor. 
Imprime cuántos valores son y luego devuelve la lista nueva. 
Si la lista tiene menos de 2 elementos, has que la función devuelva False
"""

def mayores_segundos(arr: list) ->list:
    new_arr = []
    if len(arr) < 2:
        return False

    for num in arr:
        if arr[1] < num:
            new_arr.append(num)
    return new_arr

print("Mayores al segundo elemeno: ", mayores_segundos([5, 10, 11, 8, 15, 20, 2]))
#print("Mayores al segundo elemeno: ", mayores_segundos([5]))

"""Esta longitud, ese valor 
Escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, 
y cuyos valores sean todos el valor dado
"""

def longitud_and_value(a: int, b: int) -> list:
    new_arr = []
    for num in range(0, a):
        new_arr.append(b)
    return new_arr

print("Retorna", longitud_and_value(6,2))