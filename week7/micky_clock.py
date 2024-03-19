import pygame
import sys
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

WHITE = (255, 255, 255)
clock_image = pygame.image.load("week7/clock.png")
right_arm_image = pygame.image.load("week7/left_arm.png")
left_arm_image = pygame.image.load("week7/right_arm.png")

clock_rect = clock_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
right_arm_rect = right_arm_image.get_rect(center=(340, 400))
left_arm_rect = left_arm_image.get_rect(center=(460, 400))

def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = (minute / 60) * 360
    second_angle = (second / 60) * 360

    rotated_right_arm = rotate_image(right_arm_image, -minute_angle)
    rotated_left_arm = rotate_image(left_arm_image, -second_angle)

    screen.fill(WHITE)

    screen.blit(clock_image, clock_rect)
    screen.blit(rotated_right_arm, rotated_right_arm.get_rect(center=right_arm_rect.center))
    screen.blit(rotated_left_arm, rotated_left_arm.get_rect(center=left_arm_rect.center))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
