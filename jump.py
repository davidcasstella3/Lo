import pygame
import sys


pygame.init()

screen_width, screen_height = 564, 1002
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Salto")

tanjiro = pygame.image.load("tanjiro.png")
map_game = pygame.image.load("map.png")

tanjiro_width, tanjiro_height = tanjiro.get_size()
tanjiro = pygame.transform.scale(tanjiro, (100, 200))


x = screen_width // 2
y = screen_height - tanjiro_height
vel = 5 


is_jumping = False
jump_count = 10

clock = pygame.time.Clock()
while True:
    clock.tick(30)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - tanjiro_width:
        x += vel

    # Control de salto
    if not is_jumping:
        if keys[pygame.K_SPACE]: 
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1  # Comienza a bajar
            y -= (jump_count ** 2) * 0.5 * neg  # Actualiza la posición vertical
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10  # Reinicia el salto

    screen.blit(map_game, (0, 0))
    screen.blit(tanjiro, (x, y))

    pygame.display.update() 
