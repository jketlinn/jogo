import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

# Carregar imagens
dino_img = pygame.image.load("dino.png")
dino_img = pygame.transform.scale(dino_img, (70, 70))
obstacle_img = pygame.image.load("cactus.png")
obstacle_img = pygame.transform.scale(obstacle_img, (20, 50))

# Variáveis do dinossauro
dino_width = 70
dino_height = 70
dino_x = 50
dino_y = HEIGHT - dino_height
dino_vel_y = 0 
jumping = False

# Variáveis do obstáculo
obstacle_width = 10
obstacle_height = 40
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height

# Função para reiniciar o obstáculo
def reset_obstacle():
    global obstacle_x
    obstacle_x = WIDTH

# Loop principal do jogo
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                dino_vel_y = -10

    # Lógica do pulo do dinossauro
    if jumping:
        dino_y += dino_vel_y
        dino_vel_y += 1

        if dino_y >= HEIGHT - dino_height:
            dino_y = HEIGHT - dino_height
            jumping = False

    # Lógica do movimento do obstáculo
    obstacle_x -= 5
    if obstacle_x < 0:
        reset_obstacle()

    # Verificação de colisão
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if dino_rect.colliderect(obstacle_rect):
        running = False

    # Preenchimento da tela
    screen.fill((255, 255, 255))

    # Desenho do dinossauro
    screen.blit(dino_img, (dino_x, dino_y))

    # Desenho do obstáculo
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()