import pygame

class SnakeWing:
    def __init__(self, pos):
        self.pythonlogo = pygame.image.load("pythonlogo.png")
        self.pythonlogo = pygame.transform.scale(self.pythonlogo, (100, 100))
        self.image_rect = self.pythonlogo.get_rect()
        self.image_rect.center = pos
        self.Speedy = pygame.math.Vector2(100, 100)
        self.pythonlogo = pygame.image.load("pythonlogo.png")
        self.pythonlogo = pygame.transform.scale(self.pythonlogo, (100, 100))
        self.image_rect = self.pythonlogo.get_rect()
        self.image_rect.center = pos
        self.Speedy = pygame.math.Vector2(100, 100)

    def speedofpython(self):
        screeninfo = pygame.display.Info()
        self.image_rect.move_ip(self.Speedy)
        width = screeninfo.current_w
        height = screeninfo.current_h
        if self.image_rect.right > width:
            self.Speedy.x *= -1
        if self.image_rect.left < 0:
            self.Speedy.x *= -1
        if self.image_rect.top < 0:
            self.Speedy.y *= -1
        if self.image_rect.bottom > height:
            self.Speedy.y *= -1

    def draw(self, screen):
        screen.blit(self.pythonlogo, self.image_rect)


