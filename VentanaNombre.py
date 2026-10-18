import pygame
import sys
import os
class PantallaNombre:
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    GRIS = (200, 200, 200)

    ANCHO = 500
    ALTO = 900

    def __init__(self, puntaje):
        pygame.init()
        self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Ingresar Nombre")
        self.fuente_titulo = pygame.font.Font(None, 30)
        self.fuente_subtitulo = pygame.font.Font(None, 36)
        self.fuente_input = pygame.font.Font(None, 36)
        self.texto_input = ""
        self.input_active = False
        self.fondo = self.cargar_imagen("menu_fondo.png")
        self.puntaje = puntaje
        titulo_texto = "¡Nuevo récord!"
        titulo_render = self.fuente_titulo.render(titulo_texto, True, self.BLANCO)
        titulo_rect = titulo_render.get_rect(center=(self.ANCHO // 2, 50))

        subtitulo_texto = "Ingresa tu nombre:"
        subtitulo_render = self.fuente_subtitulo.render(subtitulo_texto, True, self.BLANCO)
        subtitulo_rect = subtitulo_render.get_rect(center=(self.ANCHO // 2, 110))

        input_box = pygame.Rect(50, 220, self.ANCHO - 100, 50)
        boton_aceptar = pygame.Rect(self.ANCHO // 2 - 100, 310, 200, 50)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        self.input_active = not self.input_active
                    else:
                        self.input_active = False
                if event.type == pygame.KEYDOWN:
                    if self.input_active:
                        if event.key == pygame.K_RETURN:
                            if self.texto_input.strip():
                                self.escribir_en_archivo(
                                    "puntajes.txt",
                                    f"{self.texto_input.strip().replace(',', ' ')},{self.puntaje}",
                                )
                                return
                        elif event.key == pygame.K_BACKSPACE:
                            self.texto_input = self.texto_input[:-1]
                        else:
                            self.texto_input += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_aceptar.collidepoint(event.pos) and self.texto_input.strip():
                        self.escribir_en_archivo(
                            "puntajes.txt",
                            f"{self.texto_input.strip().replace(',', ' ')},{self.puntaje}",
                        )
                        return

            self.ventana.blit(self.fondo, (0, 0))

            pygame.draw.rect(self.ventana, self.NEGRO, titulo_rect)
            self.ventana.blit(titulo_render, titulo_rect)

            pygame.draw.rect(self.ventana, self.NEGRO, subtitulo_rect)
            self.ventana.blit(subtitulo_render, subtitulo_rect)

            color_input = self.GRIS if not self.input_active else self.BLANCO
            pygame.draw.rect(self.ventana, color_input, input_box, 2)
            texto_superficie = self.fuente_input.render(self.texto_input, True, self.BLANCO)
            self.ventana.blit(texto_superficie, (input_box.x + 5, input_box.y + 5))
            if not self.texto_input.strip():
                ayuda = self.fuente_input.render("Escribe tu nombre", True, self.GRIS)
                self.ventana.blit(ayuda, (input_box.x + 5, input_box.y + 5))

            boton_color = self.GRIS if self.texto_input.strip() else (100, 100, 100)
            pygame.draw.rect(self.ventana, boton_color, boton_aceptar)
            texto_boton = self.fuente_input.render("Guardar", True, self.NEGRO)
            texto_boton_rect = texto_boton.get_rect(center=boton_aceptar.center)
            self.ventana.blit(texto_boton, texto_boton_rect)

            pygame.display.flip()

    def cargar_imagen(self, nombre_archivo):
            ruta = "img/" + nombre_archivo
            return pygame.transform.scale(pygame.image.load(ruta).convert(), (self.ANCHO, self.ALTO))
    
    def escribir_en_archivo(self, nombre_archivo, contenido):
        ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
        with open(ruta, 'a', encoding='utf-8') as archivo:
            archivo.write(contenido + '\n')

def finish():
    print("terminado")