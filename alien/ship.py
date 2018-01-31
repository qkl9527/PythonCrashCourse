import pygame

class Ship():
	"""游戏飞船 设置的类"""

	def __init__(self, ai_settings, screen):

		self.screen = screen
		self.ai_settings = ai_settings

		# 加载非常图片并获取其外接矩形
		self.image = pygame.image.load("images/ship.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 将飞船放在屏幕中央最底部
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 飞船的中心点
		self.center = self.rect.centerx;

		# 移动标志
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			# self.rect.centerx += 1
			self.center += self.ai_settings.ship_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			# self.rect.centerx -= 1
			self.center -= self.ai_settings.ship_speed


		self.rect.centerx = self.center


	def blitme(self):
		"""" 在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)