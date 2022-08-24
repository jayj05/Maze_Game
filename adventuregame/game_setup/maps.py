import pygame
import csv
import os
from .colors import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, type):
        super().__init__()
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

class TileMap():
    def __init__(self, spritesheet, csv_filename):
        self.sheet = spritesheet
        self.tile_size = 32
        self.start_x = 0 
        self.start_y = 0

        self.tiles = self.load_tiles(csv_filename)

        self.map = pygame.Surface((896, 640))
        self.map.set_colorkey((WHITE))

        self.tile_group = pygame.sprite.Group()
        for tile in self.tiles:
            self.tile_group.add(tile)
        

    def draw_map(self, surface):
        self.tile_group.draw(surface)

    def load_tiles(self, filename):
        tiles = [] 
        tilemap = self.read_csv(filename)
        
        x, y = 0, 0
        for row in tilemap:
            x = 0
            for tile in row:
                if tile == '0':
                    tiles.append(Tile(self.walkable_tile(32, 32), x*self.tile_size, y*self.tile_size, 'walkable'))
                elif tile == '1':
                    tiles.append(Tile(self.border_tile(32, 32), x*self.tile_size, y*self.tile_size, 'border'))
                elif tile == '3':
                    tiles.append(Tile(self.exit_tile(32, 32), x*self.tile_size, y*self.tile_size, 'exit'))
                # Move to next tile in row
                x += 1
            # Move to next row
            y += 1

        return tiles
    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
            return map
                
    def border_tile(self, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (32, 0, width, height))
        return image
        
    def walkable_tile(self, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (0, 0, width, height))
        return image

    def exit_tile(self, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (64, 0, width, height))
        return image


        
