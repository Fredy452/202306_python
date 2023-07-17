#Importando modulos
from usuario import User

pedro = User("Pedro", "correo@correo.com").hacer_deposito(300).mostrar_balance_usuario()

jose = User("Jose", "correo@correo.com").mostrar_balance_usuario()

pedro.transfer_dinero(jose, 100).mostrar_balance_usuario()

jose.mostrar_balance_usuario()