import os
import sys
import pygame
from pygame.sprite import Sprite

# 设置工作路径
os.chdir(os.path.dirname(sys.argv[0]))

class Ship(Sprite):
    '''管理飞船的模块'''
    def __init__(self,ai_game):
        #初始化飞船并设置初始置
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像并获取其外接矩形
        # image_path = 'C:\\NEWStudy\\PythonStudy\\project1_Alien\\alien_invasion\\images\\ship.bmp'
        # self.image = pygame.image.load(image_path)
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        # 每艘新飞船都放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 在飞船的属性 x 中存储一个浮点数
        self.x = float(self.rect.x)
        # 右移标志(一开始不移动)
        self.moving_right = False
        # 左移标志(一开始不移动)
        self.moving_left = False


    # 判断移动状态
    def update(self):
        '''根据移动标志调整飞船的位置'''
        # 更新飞船而不是 rect 对象的 x 值
        # 右移
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # 左移
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 根据 self.x 更新 rect 对象
        self.rect.x = self.x
    
    def center_ship(self):
        """将飞船放在屏幕底部的中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    


    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)




        