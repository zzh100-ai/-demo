import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """管理飞船的类"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        self.image=pygame.image.load('D:\code\pythonxaingmu\python\游戏demo\images\ship.png')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
        self.moving_right=False
        self.moving_left=False
        
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """将飞船放到屏幕底部的中央"""
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)