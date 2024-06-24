import sys
import pygame
from ship import Ship

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
        # 设置初始化窗口大小
        self.screen = pygame.display.set_mode((1200, 800))
        # 设置窗口标题
        pygame.display.set_caption("Alien Invasion")
        # 设置背景颜色
        self.bg_color = (230,230,230)
        # 初始化飞船
        self.ship = Ship(self)

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
            self.__check_events()

            # # 每次循环多重绘屏幕
            # self.screen.fill(self.bg_color)
            # # 在指定位置绘制飞船
            # self.ship.blitme()
            # # 让最近绘制的屏幕可见
            # pygame.display.flip()
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

    '''
    为了进一步简化 run_game()，我们把更新屏幕的代码移到一个名为
    __update_screen() 的方法中
    '''
    def ___update_screen(self):
        # 每次循环多重绘屏幕
        self.screen.fill(self.bg_color)
        # 在指定位置绘制飞船
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()