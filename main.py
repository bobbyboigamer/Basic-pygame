import pygame

WIDTH, HEIGHT = (640, 480)

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the hands!")

# Functions
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()