import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

x = 320
y = 240
vx = 0
vy = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x - 25 > 0: 
                    vx = -20
                else:
                    vx = 0

            elif event.key == pygame.K_RIGHT:
                if x + 25 < 640: 
                    vx = 20
                else:
                    vx = 0

            elif event.key == pygame.K_UP:
                if y - 25 > 0: 
                    vy = -20
                else:
                    vy = 0

            elif event.key == pygame.K_DOWN:
                if y + 25 < 480: 
                    vy = 20
                else:
                    vy = 0

        elif event.type == pygame.KEYUP:
            vx = 0
            vy = 0

    x += vx
    y += vy

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (200, 0, 0), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()