import pygame

class Mascota:
    def __init__(self):
        self.energia = 100
        self.hambre = 0
        self.higiene = 100
        self.estado = "Feliz"

    def alimentar(self):
        self.hambre = max(0, self.hambre - 10) # evita que el hambre menor que 0
        self.energia = max(100, self.energia - 10) # evita que la energia sea mayor que 100
        self.higiene = max(0, self.higiente - 10) # evita que la higiene sea menor que 0

    def banar(self):
        self.higiene = min(100, self.higiene + 40) # evita que la higiene sea mayor que 100
        self.energia = min(100, self.energia - 10) # evita que la energia sea mayor que 100
        self.hambre = min(100, self.hambre + 10) # evita que el hambre sea mayor que 100

    def dormir(self):
        self.energia = min(100, self.energia + 40) # evita que la energia sea mayor que 100
        self.hambre = min(100, self.hambre + 10) # evita que el hambre sea mayor que 100
        self.higiene = max(0, self.higiene - 10) # evita que la higiene sea menor que 0

    def actualizarEstado(self):
        if self.hambre > 60:
            self.estado = "Hambriento"
        elif self.higiene < 40:
            self.estado = "Sucio"
        elif self.energia < 30:
            self.estado = "Cansado"
        else:
            self.estado = "Feliz"

