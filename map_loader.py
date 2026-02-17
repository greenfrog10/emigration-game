import pygame
import pytmx
import pyscroll

class MapLoader:
    def __init__(self,WIDTH,HEIGHT,file,zoom):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.file = file
        self.zoom = zoom
        self.tmx_data = pytmx.load_pygame(file)
        self.map_data = pyscroll.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data,(WIDTH,HEIGHT))
        self.map_layer.zoom = zoom
        self.world = pyscroll.PyscrollGroup(self.map_layer)
        self.collision_list = []
        self.npc_list = []
        self.enter = []
        self.exit = []
        self.spawn_x = 0
        self.spawn_y = 0
        for obj in self.tmx_data.objects:
            if obj.type == "collision":
                self.collision_list.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            if obj.type == "player_spawn":
                self.spawn_x = obj.x
                self.spawn_y = obj.y
            if obj.type == "npcs":
                self.npc_list.append([pygame.Rect(obj.x, obj.y, obj.width, obj.height),obj.text])
            if obj.type == "enter":
                self.enter.append([pygame.Rect(obj.x,obj.y,obj.width,obj.height), obj.file, obj.x, obj.y - 60])
            if obj.type == "manual_enter":
                self.enter.append([pygame.Rect(obj.x,obj.y,obj.width,obj.height), obj.file, obj.dest_x,obj.dest_y])
            if obj.type == "exit":
                self.exit.append([pygame.Rect(obj.x,obj.y,obj.width,obj.height),obj.file,obj.x,obj.y + 60])

