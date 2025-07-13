
class Settings:
    def __init__(self):
        # 屏幕设置
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
        self.alien_speed=2.0
        self.fleet_drop_speed=10
        # 以什么速度加快游戏的节奏
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction=1
    def initialize_dynamic_settings(self):
        """初始化随游戏变化而设置"""
        self.ship_speed=6
        self.bullet_speed=10
        self.alien_speed=2
        # fleet_direction为表示向右
        self.fleet_direction=1
    def increase_speed(self):
        """提高速度的设置"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale