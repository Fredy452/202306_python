from classes.ninja import Ninja
from classes.pirate import Pirate

def gameInfo():
    decorator = "*" *40
    print(f"{decorator}\n"
          "Bienvenido al juego de pirata vs ninja\n"
          f"{decorator}")

"""
Creando los objetos de clases ninja y pirata
"""
michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

"""
Llamando a la función gameInfo()
"""
gameInfo()


"""
Creando la función attact Ninja
"""
def attack_Ninja():
    """metodo para llamar a la funcion ninja_attack()"""
    print("Que desea hacer?\n"
          "1- Realizar ataque\n"
          "2- Ver mi información\n")
    opcion = [1,2]
    opcionSelected = int(input("Elegir opción: \n"))
    if opcionSelected == opcion[0]:
        jack_sparrow.attack(michelangelo)
        michelangelo.show_stats()
    elif opcionSelected == opcion[1]:
        jack_sparrow.show_stats()


"""
Eligindo opcines
"""
print("Para continuar elija el rol")
rol = [1,2]
print("1- Pirata \n"
      "2- Ninja\n")
rolSelected = int(input("Ingrese Rol: "))
if rolSelected == rol[0]:
    print("Haz elegido el rol de Pirata\n")
    jack_sparrow.show_stats()
    attack_Ninja()
elif rolSelected == rol[1]:
    print("Haz elegido el rol de Ninja\n")
    michelangelo.show_stats()
else:
    print("Ingrese una opción valida")

    

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
# michelangelo.show_stats()