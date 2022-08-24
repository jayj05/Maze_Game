import pygame

from game_setup.maps import Tile 
from .mainwindow import MainWindow
from .mainwindow import GameMechanics
from .colors import *


class Player(pygame.sprite.Sprite):
    def __init__(self, sheet, width, height):
        super().__init__()
        self.sheet = sheet
        self.x, self.y = 0, 0
        self.sprite_sheet_column_amt = 4

        self.rect_x = 0 
        self.rect_y = 0

        self.width = width 
        self.height = height

        self.is_moving_backwards = False 
        self.is_moving_forwards = False 
        self.is_moving_left = False 
        self.is_moving_right = False

        self.backward_frames = [] 
        for i in range(self.sprite_sheet_column_amt):
            self.backward_frames.append(self.backward_animation(i, self.x, self.y, 0.75))

        self.forward_frames = []
        for i in range(self.sprite_sheet_column_amt):
            self.forward_frames.append(self.forward_animation(i, self.x, self.y, 0.75))

        self.left_frames = [] 
        for i in range(self.sprite_sheet_column_amt):
            self.left_frames.append(self.left_animation(i, self.x, self.y, 0.75))

        self.right_frames = [] 
        for i in range(self.sprite_sheet_column_amt):
            self.right_frames.append(self.right_animation(i, self.x, self.y, 0.75))

        self.current_frame = 0 
        self.image = self.backward_animation(0, self.x, self.y, 0.75)

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def update(self):

        # Moving backwards
        if self.is_moving_backwards:
            self.rect.y += GameMechanics.RECT_VELOCITY
            
            self.current_frame += 0.2  # This will prolong the amount of time spent on each frame of the sprite
            if self.current_frame >= len(self.backward_frames):
                self.current_frame = 0

            self.image = self.backward_frames[int(self.current_frame)] # Int will keep the float value of self.current_frame rounded down until it reaches the next whole number
        
        # Moving forward
        if self.is_moving_forwards:
            self.rect.y -= GameMechanics.RECT_VELOCITY
            
            self.current_frame += 0.2
            if self.current_frame >= len(self.forward_frames):
                self.current_frame = 0 
            
            self.image = self.forward_frames[int(self.current_frame)]
        
        # Moving left
        if self.is_moving_left:
            self.rect.x -= GameMechanics.RECT_VELOCITY

            self.current_frame += 0.2 
            if self.current_frame >= len(self.left_frames):
                self.current_frame = 0
            
            self.image = self.left_frames[int(self.current_frame)]
        
        if self.is_moving_right:
            self.rect.x += GameMechanics.RECT_VELOCITY  

            self.current_frame += 0.2 
            if self.current_frame >= len(self.right_frames):
                self.current_frame = 0
            
            self.image = self.right_frames[int(self.current_frame)]

    def move_backward(self):
        self.is_moving_backwards = True 
    
    def move_backward_done(self):
        self.image = self.backward_frames[0]
        self.is_moving_backwards = False
    
    def move_forward(self):
        self.is_moving_forwards = True 

    def move_forward_done(self):
        self.image = self.forward_frames[0]
        self.is_moving_forwards = False

    def move_left(self):
        self.is_moving_left = True 
    
    def move_left_done(self):
        self.image = self.left_frames[0]
        self.is_moving_left = False

    def move_right(self):
        self.is_moving_right = True 
    
    def move_right_done(self):
        self.image = self.right_frames[0]
        self.is_moving_right = False

    def backward_animation(self, frame, pos_x, pos_y, scale=1):
        # SRCALPHA will remove the black background without having to set the colorkey
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  
        image.blit(self.sheet, (pos_x, pos_y), (frame*self.width, 0, self.width, self.height))
        image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
        return image

    def forward_animation(self, frame, pos_x, pos_y, scale=1):
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        image.blit(self.sheet ,(pos_x, pos_y), (frame*self.width, self.height*3, self.width, self.height))
        image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
        return image

    def left_animation(self, frame, pos_x, pos_y, scale=1):
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        image.blit(self.sheet, (pos_x, pos_y), (frame*self.width, self.height, self.width, self.height))
        image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
        return image 

    def right_animation(self, frame, pos_x, pos_y, scale=1):
        image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        image.blit(self.sheet, (pos_x, pos_y), (frame*self.width, self.height*2, self.width, self.height))
        image = pygame.transform.scale(image, (self.width*scale, self.height*scale))
        return image 