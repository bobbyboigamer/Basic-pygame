import pygame

WIDTH, HEIGHT = (510, 512.5)

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the hands!")

background = pygame.image.load('checkerboard.png')
clock = pygame.time.Clock()

def background_update(scrollPosition):
    window.blit(background, (0, scrollPosition))
    window.blit(background, (0, scrollPosition - HEIGHT))
    pygame.display.update()
"""
def music_update():
    music = {
        1: 'She_studious_girl_by_tohomoko.mp3',
        2: 'Another_song.mp3',
        3: 'Yet_another_song.mp3',
        4: 'One_more_song.mp3',
        5: 'Final_song.mp3',
    }

    for i in range(1, 5):
        pygame.mixer.music.load(music[i])
        pygame.mixer.music.play()
        pygame.time.delay(1000) 
"""
def main():
    scrollPosition = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        scrollPosition += 1
        scrollPosition %= HEIGHT + 1

        background_update(scrollPosition)
#        music_update()
        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()