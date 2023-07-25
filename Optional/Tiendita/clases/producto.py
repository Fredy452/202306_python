class Producto:
    """Creación de la clase producto"""

    def __init__(self, nombre: str, precio: float, categoria: str) -> None:
        """Definición del metodo constructor"""
        self.nombre = nombre 
        self.precio = precio
        self.categoria = categoria


    def actualizar_precio(self, cambio_porcentaje: float, is_elevado: bool):
        """Función para actualizar el precio"""
        if is_elevado:
            aumento = (self.precio * cambio_porcentaje)
            self.precio += aumento
            return self
        else:
            descuento = (self.precio * cambio_porcentaje)
            self.precio += descuento
            return self
    

    def print_info(self):
        """Metodo para imprimir datos del producto"""
        print("Datos del producto\n"
              f"Nombre: {self.nombre}\n"
              f"Categoria: {self.categoria}\n"
              f"Precio: ${self.precio}\n")
        return self


    def agregar_producto(self, nuevo_producto: str) -> None:
        pass


    def vender_producto(self, id) -> None:
        pass


    def inflacion(self, porcentaje_aumento):
        aumento = (self.precio * porcentaje_aumento)
        self.precio += aumento
        return self


    def __str__(self) -> str:
        return (f"{self.nombre}")

