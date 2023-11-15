import pygame

WIDTH, HEIGHT = (510, 512.5)
clock = pygame.time.Clock()

pygame.init()

# Main Initialization

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the hands!")
background = pygame.image.load('checkerboard.png')
icon = pygame.image.load('err.webp') 
pygame.display.set_icon(icon)

def background_update(scrollPosition):
    window.blit(background, (0, scrollPosition))
    window.blit(background, (0, scrollPosition - HEIGHT))
    pygame.display.update()

def music_update():
    music = {
        1: 'She_studious_girl_by_tohomoko.mp3',
    }

    for i in range(len(music)):
        pygame.mixer.music.load(music[i])
        pygame.mixer.music.play()
        pygame.time.delay(1000) 

def main():
    scrollPosition = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        scrollPosition = (scrollPosition + 1) % (HEIGHT + 1)
        background_update(scrollPosition)
        music_update()
        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()