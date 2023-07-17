
class CuentaBancaria:
    """Definicion de la clase de cuenta bancaria"""

    def __init__(self,nombre: str, tasa_interes, balance = 0):
        """Definicion delconstructor"""
        self.nombre = nombre
        self.balance = self.establecer_balance(balance)
        self.tasa_interes = self.establecer_interes(tasa_interes)
    
    
    def mostrar_info_cuenta(self):
        guion = "-" * 45
        print(f" {guion} \n Usuario: {self.nombre} balance: ${self.balance} interes: {self.tasa_interes} \n {guion} \n")  # noqa: E501
        return self

    @staticmethod
    def establecer_balance(monto):
        if monto < 0:
            return 0
        else:
            return monto
        
    @staticmethod
    def establecer_interes(interes):
        """Metodo para establecer interes"""
        if interes > 0 and interes < 100:
            return interes * 0.01
        else:
            return 0.01

    def deposito(self, monto):
        """Funcion para añadir depositos"""
        self.balance += self.establecer_balance(monto)
        return self

    def retiro(self, monto):
        """Función para efectuar el retiro"""
        if monto > self.balance:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
            return self
        else:
            self.balance -= monto
        return self
    
    def generar_interes(self):
        """Función para generar interes siempre y cuando se tenga deposito"""
        if self.balance > 0:
            interes = self.balance
            interes *= self.tasa_interes
            self.balance += interes
            return self
        
# Creando dos usuarios
marcos = CuentaBancaria("Marcos", 5)
lucas = CuentaBancaria("Lucas", 7)

#Creando deposito y generando intereses
marcos.deposito(100).deposito(100).deposito(100).retiro(150).generar_interes().mostrar_info_cuenta()
lucas.deposito(200).deposito(200).retiro(25).retiro(25).retiro(25).retiro(25).generar_interes().mostrar_info_cuenta()
