import pygame
import os
import sys



# 设置工作路径
os.chdir(os.path.dirname(sys.argv[0]))

class Alien:
    '''管理外星人的模块'''
    def __init__(self,ai_game):
        # 初始化设置外星人
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # 加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()
        print(self.rect)
        # 外星人放在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image,self.rect)

