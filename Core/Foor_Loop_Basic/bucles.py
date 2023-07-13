"""Imprime todos los numeros del 0 al 150"""
for x in range(0, 151):
    #print(x)
    pass


"""Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000. """
for x in range(5, 10001, 5):
    #print(x)
    pass


"""
Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
Si es divisible por 5, imprime "Coding” en su lugar. 
Si es divisible por 10, imprime "Coding Dojo". 
"""
for n in range(1, 101):
    # if n % 5 == 0:
    #     print("Dojo")
    # if n % 10 == 0:
    #     print("Coding Dojo")
    # print(n)
    pass


"""Agrega los enteros impares del 0 al 500,000, e imprime la suma final."""
sum = 0
for n in range(0, 500_000):
    # if n % 2 != 0:
    #     sum += n
    pass

#print("La suma de todos los imapres es: ", sum)


""" 
Imprime números positivos comenzando desde el 2018 
en cuenta regresiva de 4 en 4. 
"""
for n in range(2018, 0, -4):
    #print(n)
    pass


"""
Establece tres variables: lowNum, highNum, mult. 
Comenzando en lowNum y pasando por highNum, 
imprime solo los enteros que sean múltiplos de mult. 
Por ejemplo, si lowNum=2, highNum=9 y mult=3. 
El bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
"""

luwNum = 2
highNum = 9
mult = 3

for n in range(luwNum, highNum +1):
    if n % mult == 0:
        print(n)