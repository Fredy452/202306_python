class CuentaBancaria:
    """Definicion de la clase de cuenta bancaria"""

    def __init__(self, tasa_interes, balance = 0):
        """Definicion delconstructor"""
        self.balance = self.establecer_balance(balance)
        self.tasa_interes = self.establecer_interes(tasa_interes)
    
    
    def mostrar_info_cuenta(self):
        guion = "-" * 45
        print(f" {guion} \n balance: ${self.balance} interes: {self.tasa_interes} \n {guion} \n")  # noqa: E501
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