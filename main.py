import pygame
from musicService import startMusic

WIDTH, HEIGHT = (510, 512.5)
clock = pygame.time.Clock()

pygame.init()

# Main Initialization

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the hands!")
background = pygame.image.load('Images/checkerboard.png')
icon = pygame.image.load('Images/err.webp') 
pygame.display.set_icon(icon)

def background_update(scrollPosition):
    window.blit(background, (0, scrollPosition))
    window.blit(background, (0, scrollPosition - HEIGHT))
    pygame.display.update()

def main():
    scrollPosition = 0
    run = True
    startMusic(volume=0.5)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        scrollPosition = (scrollPosition + 1) % (HEIGHT + 1)
        background_update(scrollPosition)
        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()