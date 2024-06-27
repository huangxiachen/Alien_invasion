import pygame
class Settings:
    """存储游戏《外星人入侵》中所有有关游戏配置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        # 默认屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        # 限制飞船被撞次数
        self.ship_limit = 3 

        # 子弹的设置（这些设置创建了宽 3 像素、高 15 像素的深灰色子弹。子弹的速度比飞船稍快。）
        self.bullet_width = 700
        self.bullet_height = 35
        self.bullet_color = (220,20,60)
        # 限制子弹数量
        self.bullets_allowed = 3

        # 外星人的设置
        self.fleet_drop_speed = 100  #左移

        # 以什么速度加快游戏的节奏
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5
        # 调用初始化速度方法
        self.initialize_dynamic_settings()

        
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 飞船移动速度
        self.ship_speed = 1.5
        # 子弹移动速度
        self.bullet_speed = 2.0
         # 外星人速度
        self.alien_speed = 20.0 #右移
        # 外星人移动方向
        # fleet_direction 为 1 表示向右移动，为-1 表示向左移动
        self.fleet_direction = 1
        # 记分设置
        self.alien_points = 50
    
    # 提高速度
    def increase_speed(self):
        """提高速度设置的值"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # 提高分数
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
