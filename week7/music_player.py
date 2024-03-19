import pygame
import os

pygame.init()

screen = pygame.display.set_mode((600, 200))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)

font = pygame.font.Font(None, 36)

music_dir = "C:/Users/temir/Music"  # Example music directory
songs = os.listdir(music_dir)
current_song_index = 0

pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))

def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
    pygame.mixer.music.play()

def play_previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
    pygame.mixer.music.play()

running = True
paused = False
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_n:
                play_next_song()
            elif event.key == pygame.K_p:
                play_previous_song()

    text = font.render("Controls: Space(ST/PL), N(ext), P(revious)", True, (0, 0, 0))
    screen.blit(text, (60, 80))

    pygame.display.flip()

pygame.quit()