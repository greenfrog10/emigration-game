import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert_alpha()
        self.images = {
            "down": (0, 0),
            "left": (0,32),
            "right": (0,64),
            "up": (0,96)
        }
        self.direction = "right"
        self.image = self.sprite_sheet.subsurface((self.images[self.direction]),(32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.hitbox = self.rect.inflate(-16, -20)
        
    def move(self, collision_list):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.hitbox.x -= self.speed
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.hitbox.x += self.speed
            self.direction = "right"
        elif keys[pygame.K_UP]:
            self.hitbox.y -= self.speed
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            self.hitbox.y += self.speed
            self.direction = "down"
        
        if self.hitbox.collidelist(collision_list) != -1:
            if keys[pygame.K_LEFT]:
                self.hitbox.x += self.speed
            elif keys[pygame.K_RIGHT]:
                self.hitbox.x -= self.speed
            elif keys[pygame.K_UP]:
                self.hitbox.y += self.speed
            elif keys[pygame.K_DOWN]:
                self.hitbox.y -= self.speed
        
        self.rect.center = self.hitbox.center
        
    def update(self):
        self.image = self.sprite_sheet.subsurface((self.images[self.direction]),(32, 32))