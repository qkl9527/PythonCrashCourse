class Settings():
	"""存储 游戏的 设置的类"""

	def __init__(self):

		self.title = '外星人入侵'
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# 设置飞船的速度
		self.ship_speed = 1.5

		# 设置子弹参数
		self.bullet_speed = 1
		self.bullet_width = 6
		self.bullet_height = 8
		self.bullet_color = (255, 255, 255)

		# 外星人参数
		self.alien_speed = 0.5
		# 外星人战舰 移动方向 1右 -1左
		self.fleet_direction = 1