import sys
import pygame
from time import sleep
from alien import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

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
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        # 加载飞船
        self.ship = Ship(self)
        # 创建用于存储子弹的编组
        self.bullets = pygame.sprite.Group()
        # 加载外星人
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # 游戏一开始处于非活动状态
        self.game_active = False
        # 创建开始和结束标志
        # 创建 Play 按钮
        self.play_button = Button(self, "Play")
        # 创建分数实例
        # 创建存储游戏统计信息的实例，并创建记分牌
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

    
    def ___update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环多重绘屏幕
        # self.screen.fill(self.bg_color)
        self.screen.fill(self.settings.bg_color)
         # 在指定位置绘制飞船
        self.ship.blitme()
        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 在指定位置绘制外星人
        self.aliens.draw(self.screen)
        # 显示得分
        self.sb.show_score()
        # 如果游戏处于非活动状态，就绘制 Play 按钮
        if not self.game_active:
            self.play_button.draw_button()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

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

            if self.game_active:
                # 通过状态改变飞船的行为
                self.ship.update()
                # 更新子弹位置
                self._update_bullets()
                # 更新外星人位置
                self._update_aliens()
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
    为了进一步简化 run_game()，我们把更新屏幕的代码移到一个名为
    __update_screen() 的方法中
    '''

    
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            
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
    
    """更新子弹的位置并删除已消失的子弹"""
    def _update_bullets(self):
        # 更新子弹的位置
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # 检查外星人是否被击中，如果所有外星人都被击中，重新创建新的外星人舰队
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中了外星人
        # 如果是，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, False, True)
        if not self.aliens:
            # 删除现有的子弹并创建一个新的外星舰队
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            # 最高分
            self.sb.check_high_score()


    # 创建单个外星人
    def _create_alien(self, x_position,y_position):
        alien = Alien(self)
        # 改变坐标X、Y,先赋值x、y,再赋值alien的真正坐标x、y值
        alien.x = x_position
        alien.rect.x = x_position
        alien.y = y_position
        alien.rect.y = y_position
        self.aliens.add(alien)

    """创建一个外星舰队"""
    def _create_fleet(self):
        """创建一个外星舰队"""
        # 创建一个外星人，再不断添加，直到没有空间添加外星人为止
        #  外星人的间距为外星人的宽度和外星人的高度
        alien = Alien(self)
        # alien_width = alien.rect.width #alien的宽高
        # alien_height = alien.rect.height
        # 属性 rect.size 是一个元组，包含外星人的宽度和高度
        alien_width, alien_height = alien.rect.size
        current_x = alien_width
        current_y = alien_height
        while current_y < (self.settings.screen_height/2 - 3 * alien_height):
            while current_x < (self.settings.screen_width/2 - 2 * alien_width):
                # 创建对象
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width
                # new_alien = Alien(self)
                
                # new_alien.x = current_x
                # new_alien.rect.x = current_x
                # # 改变坐标Y,先赋值y,再赋值alien的真正坐标x值
                # new_alien.y = current_y
                # new_alien.rect.y = current_y
                # current_x += 2 * alien_width
                
            # 添加一行外星人后，重置 x 值并递增 y 值
            current_x = alien_width
            current_y += 2*alien_height
            # print(current_x,current_y)
    
    '''
    当有外星人到达屏幕（右/左）边缘时，需要让整个外星舰队向下移动，
    并改变它们的移动方向（向左/向右）。
    '''
    def _check_fleet_edges(self):
        """在有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                # 将整个外星舰队向下移动，并改变它们的方向
                self._change_fleet_direction()
                break
    
    """将整个外星舰队向下移动，并改变它们的方向"""
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕的下边缘"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # 像飞船被撞到一样进行处理
                self._ship_hit()
                break

    """更新外星人的位置并删除已消灭的外星人"""
    def _update_aliens(self):
        # 更新外星人的位置
        """检查是否有外星人位于屏幕边缘，并更新整个外星舰队的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否有外星人到达了屏幕的下边缘
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        """响应飞船和外星人的碰撞"""
        """响应飞船和外星人的碰撞"""
        if self.stats.ships_left > 1:
            # 将 ships_left 减 1
            self.stats.ships_left -= 1
            # 剩余飞船数量
            self.sb.prep_ships()
            # 清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()
            # 创建一个新的外星舰队，并将飞船放在屏幕底部的中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.5)
        else:
            self.game_active = False
            # 显示光标
            pygame.mouse.set_visible(True)
    
    def _check_play_button(self, mouse_pos):
        """在玩家单击 Play 按钮时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # 还原游戏设置
            self.settings.initialize_dynamic_settings()
            # 重置游戏的统计信息
            self.stats.reset_stats()
            self.game_active = True
            # 显示成绩
            self.sb.prep_score()
            # 显示等级
            self.sb.prep_level()
            # 显示剩余飞船数量
            self.sb.prep_ships()
            # 清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()
            # 创建一个新的外星舰队，并将飞船放在屏幕底部的中央
            self._create_fleet()
            self.ship.center_ship()
            # 隐藏光标
            pygame.mouse.set_visible(False)

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()