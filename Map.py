from Identity import Identity
from Corridor import Corridor
from Room import Room
import random

class Map(Identity):
	""" My map """

	def __init__(self, sz_x, sz_y):
		Identity.__init__(self, "Map", ' ', 0, 0, sz_x, sz_y)
		self.room = []
		self.corridor = []

	def generateRandom(self):
		for i in range(5):
			size_x = random.randint(10, 20)
			size_y = random.randint(5, 10)
			x = random.randint(2, self.size_x - size_x - 2)
			y = random.randint(2, self.size_y - size_y - 2)
			room = Room(x, y, size_x, size_y)
			if not room.isInList(self.room):
				self.room.append(room)

	def connectRoom(self, room1, room2):
		self.corridor.append(Corridor(self.room, room1.door[0], room2.door[0], self))

	def renderMap(self, window):
		for i in range(len(self.room)):
			self.room[i].renderRoom(window)

