import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				# 飞船左移
				#ship.rect.centerx -= 1
				ship.moving_left = True
			elif event.key == pygame.K_RIGHT:
				# 飞船右移
				#ship.rect.centerx += 1
				ship.moving_right = True
			elif event.key == pygame.K_SPACE:
				# 创建一颗子弹， 并将其加入到编组bullets中
				new_bullet = Bullet(ai_settings, screen, ship)
				bullets.add(new_bullet)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				# 飞船左移
				#ship.rect.centerx -= 1
				ship.moving_left = False
			elif event.key == pygame.K_RIGHT:
				# 飞船右移
				#ship.rect.centerx += 1
				ship.moving_right = False

def update_screen(ai_settings, screen, ship, bullets, aliens):
	screen.fill(ai_settings.bg_color)

	# 绘制飞船
	ship.blitme()

	# 绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# 绘制外星人
	aliens.draw(screen)

	# 让最近绘制的屏幕可见
	pygame.display.flip()


def update_bullets(bullets, aliens):
	# 更新子弹绘制
	bullets.update()

	# 删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	# print(len(bullets))

	# 子弹射中外星人，两个都消失
	pygame.sprite.groupcollide(bullets, aliens, True, True)


def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	ai_settings.fleet_direction *= -1
	print(ai_settings.fleet_direction)

def update_aliens(ai_settings, aliens):
	# 更新外星人绘制
	check_fleet_edges(ai_settings, aliens)
	aliens.update()


def create_alien_fleet(ai_settings, screen, aliens):
	for alien_number in range(10):
		for alien_h_number in range(3):
			alien = Alien(ai_settings, screen)
			alien_width = alien.rect.width
			alien_height = alien.rect.height
			alien.x = alien_width + 2 * alien_width * alien_number
			alien.y = alien_height + 2 * alien_height * alien_h_number
			alien.rect.x = alien.x
			alien.rect.y = alien.y
			aliens.add(alien)