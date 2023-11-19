import pygame

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

def music_update(volume):
    music = {
        1: 'Music/She_studious_girl_by_tohomoko.mp3',
        2: 'Music/2Hardlight_Groove_by_iteachvader.mp3', 
        3: 'Music/Wanderer_-_A_cool_vs_dave_and_bambi_agony_series_fantrack.mp3',
        4: 'Music/Cirno_trumpet.mp3',
        5: 'Music/2Hardlight_Groove_by_iteachvader.mp3',
    }

    for i in music:
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(music[i])
        pygame.mixer.music.play()
        pygame.event.wait()

def main():
    scrollPosition = 0
    run = True
    music_update(volume=0.5)
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