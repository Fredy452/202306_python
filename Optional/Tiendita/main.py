from clases.producto import Producto
from clases.tienda import Tienda




"""Creando instancia de producto"""
producto1 = Producto("pan", 2500, "panificados").print_info()
producto2 = Producto("arroz", 3500, "granos").print_info()
producto3 = Producto("cerveza", 10000, "bebidas").print_info()

"""Creando tienda"""
stock = Tienda("Super Stock")

"""Agregando producto a la tienda"""
stock.agregar_producto(producto1)
stock.agregar_producto(producto2)
stock.agregar_producto(producto3)

"""Mostrando objeto tienda"""
print(stock.mostrar_producto())
print(stock.vender_producto(1))
print(stock.mostrar_producto())
