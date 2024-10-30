import pygame
import random

# Inicialización
pygame.init()
screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Tao Pai Pai")
clock = pygame.time.Clock()

# Cargar las imágenes
cielo = pygame.image.load("cielo.png").convert()
montanas = pygame.image.load("montanas.png").convert_alpha()
viento = pygame.image.load("viento.png").convert_alpha()
tao = pygame.image.load("tao.png").convert_alpha()

# Obtener anchos de las imágenes
ancho_cielo = cielo.get_width()
ancho_montanas = montanas.get_width()
ancho_viento = viento.get_width()

# Posiciones iniciales
pos_x_cielo = pos_x_montanas = pos_x_viento = 0

# Velocidades del parallax
velocidad_cielo = 1
velocidad_montanas = 2
velocidad_viento = 5

# Posición inicial de Tao
pos_tao_x = 100
pos_tao_y = 300
velocidad_tao = 5
rango_movimiento = (100, 500)

amplitud_temblor = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and pos_tao_y > rango_movimiento[0]:
        pos_tao_y -= velocidad_tao
    if keys[pygame.K_DOWN] and pos_tao_y < rango_movimiento[1]:
        pos_tao_y += velocidad_tao


    temblor = random.randint(-amplitud_temblor, 
                             amplitud_temblor)

    pos_x_cielo -= velocidad_cielo
    pos_x_montanas -= velocidad_montanas
    pos_x_viento -= velocidad_viento

    if pos_x_cielo <= -ancho_cielo:
        pos_x_cielo = 0
    if pos_x_montanas <= -ancho_montanas:
        pos_x_montanas = 0
    if pos_x_viento <= -ancho_viento:
        pos_x_viento = 0

    screen.blit(cielo, (pos_x_cielo, 0))
    screen.blit(cielo, (pos_x_cielo + ancho_cielo, 0))
    screen.blit(montanas, (pos_x_montanas, 0))
    screen.blit(montanas, (pos_x_montanas + ancho_montanas, 0))
    screen.blit(viento, (pos_x_viento, 0))
    screen.blit(viento, (pos_x_viento + ancho_viento, 0))
    screen.blit(tao, (pos_tao_x, pos_tao_y + temblor))

    pygame.display.flip()
    clock.tick(60)
