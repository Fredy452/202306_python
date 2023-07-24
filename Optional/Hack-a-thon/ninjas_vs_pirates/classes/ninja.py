class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        separator = "-"*40
        print("Datos del ninja\n"
              f"Name: {self.name}\n"
              f"Strength: {self.strength}\n"
              f"Speed: {self.speed}\n"
              f"Health: {self.health}\n{separator}")

    def attack( self, pirate):
        """Metod to attack the pirate"""
        pirate.health -= self.strength
        print("Atacando al pirata")
        return self