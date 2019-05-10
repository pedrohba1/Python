from Point import *

class Robo(Point): 
	def print_x(self):
		print(self.x)

	def print_y(self):
		print(self.y)

	def move_up(self):
		if self.y < 10:
			self.y = self.y +1
		else:
			print('movimento proibido:')

	def move_down(self):
		if self.y > 0:
			self.y = self.y -1
		else:
			print('movimento proibido:')

	def move_left(self):
		if self.x > 0:
			self.x = self.x + 1
		else:
			print('movimento proibido:')

	def move_right(self):
		if self.x < 10:
			self.x = self.x -1 
		else:
			print('movimento proibido:')
