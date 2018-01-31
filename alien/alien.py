import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" 外星人 类 """

	def __init__(self, ai_settings, screen):

		super().__init__();

		self.screen = screen
		self.ai_settings = ai_settings
		
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)


	def check_edges(self):
		""""如果外星人位于屏幕边缘，就返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right > screen_rect.right:
			return True
		elif self.rect.left <= screen_rect.left:
			return True


	def update(self):
		# self.x += self.ai_settings.alien_speed
		self.x += (self.ai_settings.alien_speed * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def blitme(self):
		self.screen.blit(self.image, self.rect)