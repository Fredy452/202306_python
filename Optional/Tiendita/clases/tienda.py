from .producto import Producto

Producto

class Tienda:
    """Definición de la clase tienda"""

    def __init__(self, nombre: str) -> None:
        """Metodo constructor de la clase"""
        self.nombre = nombre
        self.productos = []


    def agregar_producto(self, producto: list):
        """Agrega un producto a la lista de productos de la tienda"""
        self.productos.append(producto)


    def mostrar_producto(self):
        """Metodo para listar los productos de la tienda"""
        print("Datos de la tienda")
        print(f"Nombre: {self.nombre}")
        print("Lista de productos")
        for i, producto in enumerate(self.productos):
            print(f"{i} - {producto}")
        print("\n")


    def vender_producto(self, id):
        """Metodo ára eliminar un producto vendido"""
        print(f"Se ha vendido e roducto: {self.productos[id]}")
        self.productos.remove(self.productos[id])
        