import pygame
pygame.init()
w = (width, height) = (800, 800)
screeninfo = pygame.display.Info()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
pythonlogo = pygame.image.load("pythonlogo.png")
image_rect = pythonlogo.get_rect()
Speedy = pygame.math.Vector2(10, 20)


def main():
    while True:
        clock.tick(60)
        speedofpython()
        pale_green = (194, 255, 100)
        screen.fill(pale_green)
        screen.blit(pythonlogo, image_rect)
        pygame.display.flip()


def speedofpython():
    image_rect.move_ip(Speedy)
    width = screeninfo.current_w
    if image_rect.right > width:
        Speedy.x *= -1
    if image_rect.left < 0:
        Speedy.x *= -1
    if image_rect.top < 0:
        Speedy.y *= -1
    if image_rect.bottom > height:
        Speedy.y *= -1
if __name__ == "__main__":
    main()