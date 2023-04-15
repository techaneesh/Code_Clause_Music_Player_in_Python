#basic music player by pygame 
import os
import pygame

pygame.init()

# For 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Music Player")


font = pygame.font.Font(None, 36)

## Keep all songs in the below folder with code

music_dir = "E:\Downloads\Python code clause project"
# OS module is used for fetch all songs in list view
music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
current_music_index = 0


pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music_index]))
pygame.mixer.music.play()

pygame.mixer.music.set_volume(0.5)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RIGHT:


                current_music_index = (current_music_index + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:


                current_music_index = (current_music_index - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music_index]))
                pygame.mixer.music.play()

    screen.fill(WHITE)

    # which song is playing will be display on top below code for that functionality
    current_music_title = music_files[current_music_index]
    text = font.render(current_music_title, True, BLACK)
    screen.blit(text, (50, 50))

    # playing song will show in red color remain will be black.
    for i, music_title in enumerate(music_files):
        if i == current_music_index:
            text_color = (255, 0, 0)
        else:
            text_color = BLACK
        text = font.render(music_title, True, text_color)
        screen.blit(text, (50, 100 + i * 50))

    pygame.display.flip()

    clock.tick(60)
pygame.quit()
