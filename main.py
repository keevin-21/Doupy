import pygame
from mascota import Mascota
from boton import Boton

class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mascota Virtual")
        self.reloj = pygame.time.Clock()
        self.mascota = Mascota()
        self.corriendo = True
        self.botones = [
            Boton(50, 500, 150, 50, "Alimentar", self.mascota.alimentar),
            Boton(225, 500, 150, 50, "Dormir", self.mascota.dormir),
            Boton(400, 500, 150, 50, "Bañarse", self.mascota.banar)
        ]

    def ejecutar(self):
        while self.corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.corriendo = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self.manejarEventoMouse(evento)
            
            self.mascota.actualizar()
            self.dibujar()

            self.reloj.tick(60)
        pygame.quit()

    def manejarEventoMouse(self, evento):
        for boton in self.botones:
            if boton.isClick(evento.pos):
                boton.accion()

    def dibujar(self):
        self.pantalla.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        textoEstado = font.render(f"Estado: {self.mascota.estado}", True, (0, 0, 0))
        self.pantalla.blit(textoEstado, (50, 50))
        for boton in self.botones:
            boton.dibujar(self.pantalla)
        pygame.display.flip()

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
