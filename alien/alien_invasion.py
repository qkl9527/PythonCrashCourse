import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import functions as funcs
from pygame.sprite import Group

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()

	# 获取配置对象
	ai_settings = Settings();

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	print(screen)
	pygame.display.set_caption(ai_settings.title)


	# 创建飞船
	ship = Ship(ai_settings, screen)

	# 创建外星人
	# alien = Alien(ai_settings, screen)

	# 创建一个用于存储子弹的组
	bullets = Group()
	aliens = Group()

	# 创建外星人群
	funcs.create_alien_fleet(ai_settings, screen, aliens)


	#开始游戏主体
	while True:
		
		funcs.check_events(ai_settings, screen, ship, bullets)

		# 更新飞船绘制
		ship.update()

		funcs.update_bullets(bullets, aliens)

		funcs.update_aliens(ai_settings, aliens)

		# 绘制屏幕
		funcs.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()
