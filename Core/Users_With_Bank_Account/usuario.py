from cuenta_bacaria import CuentaBancaria
"""
Creando clase usuario
"""

class User:
    def __init__(self, nombre: str, correo: str) -> None:
        """Metodo constructor"""
        self.nombre = nombre
        self.correo = correo
        self.cuenta = CuentaBancaria(tasa_interes = 2, balance = 0)

    def hacer_deposito(self, monto: str):
        """Metodo para hacer deposito"""
        self.cuenta.deposito(monto)
        return self

    def hacer_retiro(self, monto: int):
        """Metodo hacer retiro"""
        self.cuenta.retiro(monto)
        return self
    
    def mostrar_balance_usuario(self):
        """Metodo para imprimir datos del usuario"""
        guion = "-" * 45
        print(f" {guion} \n Usuario: {self.nombre} balance: ${self.cuenta.balance} interes: {self.cuenta.tasa_interes} \n {guion} \n")  # noqa: E501
        return self
    
    def transfer_dinero(self, other_user, monto: int):
        """Metodo para hacer transferencia de dinero"""
        self.cuenta.retiro(monto)
        other_user.cuenta.deposito(monto)
        return self