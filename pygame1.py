import pygame
from pythonlogo import*
pygame.init()
w = (width, height) = (800, 800)
screeninfo = pygame.display.Info()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
var = SnakeWing((300, 300))


def main():
    while True:
        clock.tick(60)
        var.speedofpython()
        pale_green = (194, 255, 100)
        screen.fill(pale_green)
        var.draw(screen)
        pygame.display.flip()




if __name__ == "__main__":
    main()