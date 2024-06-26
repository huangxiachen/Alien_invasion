import pygame
class Settings:
    """存储游戏《外星人入侵》中所有有关游戏配置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 默认屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        # 移动速度
        self.ship_speed = 1.5
        # 限制飞船被撞次数
        self.ship_limit = 3 

        # 子弹的设置（这些设置创建了宽 3 像素、高 15 像素的深灰色子弹。子弹的速度比飞船稍快。）
        self.bullet_speed = 2.0
        self.bullet_width = 700
        self.bullet_height = 35
        self.bullet_color = (220,20,60)
        # 限制子弹数量
        self.bullets_allowed = 3
        # 外星人的设置
        # 外星人速度
        self.alien_speed = 20.0 #右移
        self.fleet_drop_speed = 100  #左移
        # 外星人的数量
        self.alien_count = 0
        # fleet_direction 为 1 表示向右移动，为-1 表示向左移动
        self.fleet_direction = 1
        
