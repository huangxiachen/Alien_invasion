import pygame
import os
import sys
from pygame.sprite import Sprite


# 设置工作路径
os.chdir(os.path.dirname(sys.argv[0]))

class Alien(Sprite):
    '''管理外星人的模块'''
    def __init__(self,ai_game):
        # 在左上角创建一个外星人
        super().__init__()
        # 初始化设置外星人
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()
        # 外星人放在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储用浮点数表示的外星人的位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
     
        


    '''外星人的位置'''
    def update(self):
        # 更新表示外星人的 rect 的位置
        """向左或向右移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    # 判断外星人位置是否移出屏幕外
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回 True"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image,self.rect)

