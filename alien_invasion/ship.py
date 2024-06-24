import os
import sys
import pygame

# 设置工作路径
os.chdir(os.path.dirname(sys.argv[0]))

class Ship:
    '''管理飞船的模块'''

    def __init__(self,ai_game):
        #初始化飞船并设置初始置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        # image_path = 'C:\\NEWStudy\\PythonStudy\\project1_Alien\\alien_invasion\\images\\ship.bmp'
        # self.image = pygame.image.load(image_path)
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()

        # 每艘新飞船都放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    
    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)




        