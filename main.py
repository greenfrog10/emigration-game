import pygame
from map_loader import MapLoader 
from player import Player
from npc import check_dialogue, Textbox

pygame.init()

FPS = 60
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True

map = MapLoader(WIDTH,HEIGHT,"map.tmx",3)
player = Player("assets/pipo-nekonin001.png",map.spawn_x,map.spawn_y)
map.world.add(player,layer=1)

textbox = Textbox(WIDTH, HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        pygame.display.toggle_fullscreen()
    for collision, file, x, y in map.enter:
        if collision.colliderect(player.rect):
            map = MapLoader(WIDTH,HEIGHT,file,3)
            player = Player("assets/pipo-nekonin001.png",x,y)
            map.world.add(player,layer=1)
    for collision, file, x, y in map.exit:
        if collision.colliderect(player.rect):
            map = MapLoader(WIDTH,HEIGHT,file,3)
            player = Player("assets/pipo-nekonin001.png",x,y)
            map.world.add(player,layer=1)
    
    screen.fill((0, 0, 0)) 
    
    if not textbox.visible:
        player.move(map.collision_list)
    
    player.update()
    map.world.center(player.rect.center)
    map.world.draw(screen)
    
    check_dialogue(map.npc_list, player, screen, textbox)    
    
    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()