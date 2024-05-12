import os
import pygame

# Constants
SCREEN_SIZE = (200, 100)
CAPTION = "Mini Music Player"
FONT_SIZE = 24
FONT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

# Initialize pygame
pygame.mixer.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(CAPTION)

# Function to play a song
def play_song(song):
    if os.path.isfile(song):
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
    else:
        print("File not found!")

# Function to handle input
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                song = input("Song filename (with .mp3): ")
                play_song(song)
            elif event.key == pygame.K_p:
                pygame.mixer.music.pause() if pygame.mixer.music.get_busy() else pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
    return True

# Main loop
def main():
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.Font(None, FONT_SIZE)
        text = font.render(CAPTION, True, FONT_COLOR)
        screen.blit(text, (10, 10))
        running = handle_input()
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()