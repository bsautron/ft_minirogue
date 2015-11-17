# coding: utf8

from Identity import Identity
from Door import Door
import random

class Room ( Identity ) :
	def __init__ ( self, x, y, size_x, size_y) :
		Identity.__init__(self, "Room",'.', x, y, size_x, size_y)
		self.nbDoor = random.randint(1, 3)
		self.door = []
		self.generateDoors()

	def generateDoors(self):
		for i in range(self.nbDoor):
			pos = random.randint(1, 4)
			if (pos == 1):
				x = self.x
				y = random.randint(self.y, self.y + self.size_y - 1)
			elif (pos == 2):
				x = self.x + self.size_x - 1
				y = random.randint(self.y, self.y + self.size_y - 1)
			elif (pos == 3):
				x = random.randint(self.x, self.x + self.size_x - 1)
				y = self.y
			elif (pos == 4):
				x = random.randint(self.x, self.x + self.size_x - 1)
				y = self.y + self.size_y - 1
			self.door.append(Door(x, y))

	def renderRoom(self, window):
		self.renderMe(window)
		for i in range(self.y, self.y + self.size_y):
			for j in range(self.x, self.x + self.size_x):
				if (i == self.y or i == self.y + self.size_y - 1):
					window.move(i, j)
					window.addch('-')
				if (j == self.x or j == self.x + self.size_x - 1):
					window.addch(i, j, '|')

		for i in range(len(self.door)):
			window.move(self.door[i].y, self.door[i].x)
			window.addch(self.door[i].c)
