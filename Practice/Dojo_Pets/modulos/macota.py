"""
Creación de la clase mascota 
Atributos
    name
    tipo
    golosinas
    salud
    energía 
Métodos
    dormir()
    comer()
    jugar()
    sonido() 
"""

class Mascota:
    """Definición de la clase mascota"""

    def __init__(self,
                 nombre: str,
                 tipo: str,
                 golosina: str,
                 salud: int,
                 energia: int) -> None:
        """Constructor de la clase mascota"""
        self.nombre = nombre
        self.tipo = tipo
        self.golosina = golosina
        self.salud = salud
        self.energia = energia


    def dormir(self):
        """Definicón del metodo dormir de la clase mascota"""
        self.energia += 25


    def comer(self):
        """Definición del metodo comer de la clase mascota"""
        self.energia += 5
        self.salud += 10


    def jugar(self):
        """Definición del metodo jugar de la clase mascota"""
        self.salud += 5


    def sonido():
        """Definición del metodo sonido de la clase mascota"""
        print("Esto es un ruido")

    
    def __str__(self) -> str:
        """Sobreescribiendo str"""
        return f"{self.nombre}"

    
    def mostrar_macota(self) ->None:
        print(f"Datos sobe la mascota {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Golosina: {self.golosina}")
        print(f"Salud: {self.salud}")
        print(f"Energia: {self.energia}")