import random
from Point import *
from Reward import *
from Robo import *

r1 = Reward(random.randint(0,10),random.randint(0,10),'moeda')
r2 = Reward(random.randint(0,10),random.randint(0,10),'gasolina')
r3 = Reward (random.randint(0,10),random.randint(0,10),'arma')
robot = Robo(random.randint(0,10),random.randint(0,10))

rewards = [r1,r2,r3]

def check_reward(robot, rewards):
	ok = False
	for reward in rewards:
		if reward.x == robot.x and reward.y == robot.y:
			print("o robo achou a recompensa: %s" % reward.name)
			ok = True
	return ok


for i in range(10):
	movement = input('digite, up, down, left ou right para o movimento: ')
	if movement == 'up':
		robot.move_up()
	elif movement == 'right':
		robot.move_right()
	elif movement == 'down':
		robot.move_down()
	elif movement == 'left':
		robot.move_left()
	else:
		print('movimento invalido')
		continue
	print(robot)
	check_reward(robot, reward)






