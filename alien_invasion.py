import pygame
import sys
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
    def run_game(self):
            while True:
                self._check_events()
                self.ship.update()
                self._update_bullets()
                self._update_screen()
                self._update_aliens()
                self.clock.tick(60)
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        print(f"按键: {event.key}, 字符: {chr(event.key) if 32 <= event.key <= 126 else 'N/A'}")
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            print("检测到Q键，退出游戏")
            sys.exit()
        elif event.key == pygame.K_ESCAPE:  # 添加ESC键退出
            print("检测到ESC键，退出游戏")
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
    def _fire_bullet(self):
        """创建一颗子弹并且将其加入编组bullets"""
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                 self.bullets.remove(bullet)
        # 检查是否有子弹击中了外星人
        # 如果是，就删除相应的子弹和外星人
        collistions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
    def _update_screen(self):

        """更新屏幕上面的图像，并切换到新的屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
    def _create_fleet(self):
        """创建一个舰队"""
        # 创建一个外星人，再不断添加，直到空间没有外星人为止
        # 外星人的间距为外星人的宽度和外星人的高度
        
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        while current_y<(self.settings.screen_height-3*alien_height):
            while current_x<(self.settings.screen_width-2*alien_width):
                self._create_alien(current_x,current_y)
                current_x+=2*alien_width
            current_x=alien_width
            current_y+=2*alien_height
          
    def _create_alien(self,x_position,y_position):
        """创建一个外星人并将其放到外星舰队"""
        new_alien=Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)
    def _update_aliens(self):
        """检查是否有外星人位于屏幕的边缘，并更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
    def _check_fleet_edges(self):
        """当有外星人到达边缘的时候应该采取措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """将整个外星舰队向下移动，并改变他们的方向 """
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()

