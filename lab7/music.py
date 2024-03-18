import pygame
import sys
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((200,300))

clock = pygame.time.Clock()

songs = ['song1.mp3', 'song2.mp3', 'song3.mp3']     
num_songs = len(songs)
current_song_index = 0

pygame.mixer.music.load(songs[current_song_index])
pygame.mixer.music.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % num_songs
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % num_songs
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
                
                
    pygame.display.update()
    clock.tick(60)