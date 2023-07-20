"""
Modulo de ninja que contara con los siguientes atributos
* Atributos
- nombre
- apellido
- mascotas
- premio
- comida_mascota 
* Metodos
- caminar()
- alimentar()
- bañar()
"""

class Ninja:
    """Creación de la clase ninja"""
    def __init__(self,
                 nombre: str,
                 apellido: str,
                 mascota,
                 premio: str,
                 comida_mascota: str
                 ) -> None:
        self.nombre = nombre
        self.apeelido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota

    
    def caminar(self):
        """Definición del metodo caminar de la clase ninja"""
        self.macosta.jugar()


    def alimentar(self, comida_mascota):
        """Definición del metodo alimentar de la clase ninja"""
        self.comida_mascota = comida_mascota
        self.mascota.comer()


    def bañar(self):
        """Definición del metodo bañar de la clase ninja"""
        pass


    def __str__(self) -> str:
        """Sobreescribimos el metodo str"""
        separador = "-" *40
        return ("Datos sobre el ninja \n"
                f"Nombre: {self.nombre}\n"
                f"Mascota: {self.mascota}\n"
                f"Premio: {self.premio}\n"
                f"Comida: {self.comida_mascota}\n{separador}")