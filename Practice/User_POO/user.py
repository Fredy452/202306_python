"""
Creando clase usuario
"""
class User:
    def __init__(self, nombre: str, correo: str) -> None:
        """Metodo constructor"""
        self.nombre = nombre
        self.correo = correo
        self.balance_cuenta = 0

    def hacer_deposito(self, monto: str):
        """Metodo para hacer deposito"""
        self.balance_cuenta += monto

    def hacer_retiro(self, monto: int):
        """Metodo hacer retiro"""
        self.balance_cuenta -= monto
    
    def mostrar_balance_usuario(self):
        """Metodo para imprimir datos del usuario"""
        print(f"{self.nombre} {self.correo} {self.balance_cuenta} \n")
    
    def transfer_dinero(self, other_user, monto: int):
        """Metodo para hacer transferencia de dinero"""
        self.balance_cuenta -= monto
        other_user.balance_cuenta += monto
        

user2 = User("Jose", "correo@correo.com")
user2.hacer_deposito(100)
user2.mostrar_balance_usuario()


#Usuario 3
user3 = User("Carlos", "correo@gmail.com")
user3.hacer_deposito(100)
user3.mostrar_balance_usuario()


#Transfiriendo dinero
user2.transfer_dinero(user3, 50)

#mostrando balnce
user2.mostrar_balance_usuario()
user3.mostrar_balance_usuario()
