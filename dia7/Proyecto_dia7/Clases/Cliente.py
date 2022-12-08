from dia7.Proyecto_dia7.Clases.Persona import *


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__int__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Hola {self.nombre} {self.apellido}" \
               f" tu balance es de : {self.balance} euros"

    def depositar(self, cantidad):
        """
        Cuanto dinero quieres depositar en tu cuenta
        :return:
        """
        self.balance += cantidad
        print(f"Se ha depositado en su cuenta: {cantidad}\n"
              f"Saldo total: {self.balance}")

    def retirar(self, cantidad):
        """
        Cuanto dinero quieres retirar
        :return:
        """
        if cantidad > self.balance:
            print("lo sentimos no tienes tanto dinero")
        else:
            self.balance -= cantidad
            print(f"Se han retirado: {cantidad} euros de tu cuenta\n"
                  f"Saldo total: {self.balance}")



