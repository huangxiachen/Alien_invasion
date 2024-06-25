import sys
import pygame
from alien import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        '''
        我们将创建一个时钟(clock)，并确保它在主循环每次通过后都进
        行计时(tick)。当这个循环的通过速度超过我们定义的帧率时，Pygame 会计算需要
        暂停多长时间，以便游戏的运行速度保持一致。
        '''
        self.clock = pygame.time.Clock()
        # # 设置初始化窗口大小
        # self.screen = pygame.display.set_mode((1200, 800))
        # # 设置背景颜色
        # self.bg_color = (230,230,230)
        # 初始化设置
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width, 
        #                                        self.settings.screen_height))
        # 全屏模式
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # 设置窗口标题
        pygame.display.set_caption("Alien Invasion")
        # 加载飞船
        self.ship = Ship(self)
        # 创建用于存储子弹的编组
        self.bullets = pygame.sprite.Group()
        # 加载外星人
        self.alien = Alien(self)
    '''
    这将呈现一个游戏窗口，需要将其置于无限事件循环中。
    所有由用户交互产生的事件对象，如鼠标移动和点击等，
    都存储在一个事件队列中。 当 pygame.QUIT 被拦截时，
    我们将终止事件循环。 当用户单击标题栏上的 CLOSE 按钮时，将生成此事件。
    '''
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和鼠标事件(封装成了方法)
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            # 通过监听键盘和鼠标来改变飞船状态
            self.__check_events()
            # 通过状态改变飞船的行为
            self.ship.update()
            # 更新子弹位置
            self._update_bullets()
            # # 每次循环多重绘屏幕
            # self.screen.fill(self.bg_color)
            # # 在指定位置绘制飞船
            # self.ship.blitme()
            # # 让最近绘制的屏幕可见
            # pygame.display.flip()
            # 每次循环多重绘屏幕
            self.___update_screen()
            '''
            初始化 pygame 后，创建 pygame.time 模块中的 Clock 类的一个实例，然后在
            run_game() 的 while 循环末尾让这个时钟进行计时
            (游戏的帧率)
            '''
            self.clock.tick(60)
    
    '''
    我们将把管理事件的代码移到一个名为 _check_events() 的方法中，以简化
    run_game() 并隔离事件循环。通过隔离事件循环，可将事件管理与游戏的其他方面
    （如更新屏幕）分离。
    '''
    def __check_events(self):
        # 响应按键鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 处理具体按键所对应的事件
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_RIGHT:
                #     # 向右移动飞船
                #     self.ship.moving_right = True
                # elif event.key == pygame.K_LEFT:
                #     # 向左移动飞船
                #     self.ship.moving_left = True
                self._check_keydown_events(event)        
            elif event.type == pygame.KEYUP:
                # # 释放键盘右键
                # if event.key == pygame.K_RIGHT:
                #     self.ship.moving_right = False
                # # 释放键盘左键
                # elif event.key == pygame.K_LEFT:
                #     self.ship.moving_left = False
                self._check_keyup_events(event)

            
    # 处理按下按键的方法
    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
             # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
                # 结束游戏的键盘快捷键——Q 键
                sys.exit()   
        elif event.key == pygame.K_SPACE:
                # 按下空格发射子弹
                self._fire_bullet()
        

    # 处理释放按键的方法
    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            # 释放键盘右键
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # 释放键盘左键
            self.ship.moving_left = False

    # 子弹开火
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组 bullets """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    '''
    为了进一步简化 run_game()，我们把更新屏幕的代码移到一个名为
    __update_screen() 的方法中
    '''
    def ___update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环多重绘屏幕
        # self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 在指定位置绘制飞船
        self.ship.blitme()
        # 在指定位置绘制外星人
        self.alien.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()