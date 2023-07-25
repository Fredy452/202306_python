class MathDojo:
    """Creación de la clase mathdojo"""

    def __init__(self) -> None:
        """Constructor de la clase"""
        self.result = 0
    

    def suma(self, num, *nums) -> int:
        """Metodo que recibe uno o varios numeros como argumento"""
        self.result += num #suma con un solo argumento

        for numero in nums:
            """Recorreomos el argumento recibido"""
            self.result += numero
        return self
    

    def resta(self, num, *nums):
        """Metodo que recibe uno o varios argento para realizar la resta"""
        self.result -= num #suma con un solo argumento

        for numero in nums:
            """Recorreomos el argumento recibido"""
            self.result -= numero
        return self
    

    def __str__(self) -> str:
        return (f"Resultado: {self.result}")
    
mat = MathDojo() #creamos instancia del objeto

#mat.suma(2,3,4).suma(4,4).suma(3)#return 20
#mat.resta(2,3,4).resta(4,4).resta(3)#retur -20

mat.suma(2,450,4,70).resta(200,50,79,50)
print(mat)