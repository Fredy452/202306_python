num1 = 42 # declaración de variable tipo int    
num2 = 2.3 # declaración tipo float
boolean = True # declaracion tipo voolean 
string = 'Hello World' # declaracion de variable tipo str
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#obeto
fruit = ('blueberry', 'strawberry', 'banana') # tupla
print(type(fruit))#Imprimiendo el tipo de dato de fruit
print(pizza_toppings[1])# Imprime el elemento en la posisción 1 de la lista
pizza_toppings.append('Mushrooms')#agrega un elemento a la lista
print(person['name']) # Imprime el nombre del ogjeto en este caso John
person['name'] = 'George' #cambiamos el valor de john a George
person['eye_color'] = 'blue' #agregamos un nuevo atributo al objeto
print(fruit[2])# imprime frutilla

if num1 > 45: #condicional if que evalua si un numero esmayor que 45
    print("It's greater")
else: # si no se cumple a condición evaluada se ejecuta la siguiente acción 
    print("It's lower")

if len(string) < 5:# Evaua si la laongitud de string es menor a 5
    print("It's a short word!")
elif len(string) > 15:# caso contrario
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):#condicional for 
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)