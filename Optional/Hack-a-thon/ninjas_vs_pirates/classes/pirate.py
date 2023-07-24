class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        separator = "-"*40
        print(f"{separator}\nDatos del pirata\n"
              f"Name: {self.name}\n"
              f"Strength: {self.strength}\n"
              f"Speed: {self.speed}\n"
              f"Health: {self.health}\n{separator}")

    def attack ( self, ninja):
        """Metodo para atacar al ninja"""
        ninja.health -= self.strength
        print("Atacando al ninja")
        return self

