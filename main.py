#Proyecto del día 7: Cuenta bancaria
loop = True

#Clase persona
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


#Clase cliente
class Cliente(Persona):

    def __init__(self,nombre,apellido,numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = float(balance)

    def __str__(self):
        return f'''\nHola {self.nombre} {self.apellido}
Tus datos son los siguientes:
Número de cuenta: {self.numero_cuenta}
Balance de cuenta: ${self.balance}\n'''

    def despositar(self):
        dinero_depositado = float(input("¿Cuánto dinero desea depositar? "))
        self.balance += dinero_depositado
        print(f"Su balance actual es: {self.balance}")

    def retirar(self):
        dinero_retirado = float(input("¿Cuánto dinero desea retirar? "))
        if self.balance >= dinero_retirado:
            self.balance -= dinero_retirado
            print(f"Su balance actual es: {self.balance}")
        else:
            print("Fondos insuficientes")

#Ejecutar código
def crear_cliente():
    nombre = input("Escriba su nombre: ")
    apellido = input("Escriba su apellido: ")
    numero_cuenta = input("Escriba su número de cuenta: ")
    cuenta_cliente = Cliente(nombre,apellido,numero_cuenta)
    return cuenta_cliente


def inicio():
    cuenta_cliente = crear_cliente()
    print(cuenta_cliente)
    loop = True
    while loop:
        opcion = input("\n¿Desea depositar, retirar, o salir? ").lower()
        if opcion == 'depositar':
            cuenta_cliente.despositar()
        elif opcion == 'retirar':
            cuenta_cliente.retirar()
        elif opcion == 'salir':
            loop = False
        print(cuenta_cliente)
    print("Ha salido exitosamente")


inicio()

