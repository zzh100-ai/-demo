
class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(230,230,230)
        # 飞船设置
        self.ship_speed=6
        self.ship_limit=3
        # 子弹设置
        self.bullet_speed=10
        self.bullet_width=4
        self.bullet_height=30
        self.bullet_color=(60,60,60)
        self.bullets_allowed=10
        # 外星人设置
        self.alien_speed=1.0
        self.fleet_drop_speed=50
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction=1
