import pygame
import random

def mole(): # places mole at a random location
    x = random.randrange(0, 20) * 32
    y = random.randrange(0, 16) * 32
    return x, y

def grid(display): # displays the grid over the screen
    for i in range(20):
        for j in range(16):
            pygame.draw.line(display, ( 252, 255, 255), (i * 32, 0), (i * 32, 512))
            pygame.draw.line(display, ( 252, 255, 255), (0, j * 32), (640, j * 32))

def main(): # runs game
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        x, y = 0,0
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if x <= event.pos[0] < x + 32:
                        if y <= event.pos[1] < y + 32:
                            x, y = mole()
            screen.fill("light green")
            grid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
