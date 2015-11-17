from Identity import Identity
import random
class Corridor() :
	def	__init__(self, room, x_beg, y_beg, x_end, y_end, szWindow_x, szWindow_y) :
		self.coordinates = []
		self.coordinates.append(Identity("coordinates",'X',x_beg,y_beg,1,1))
		
		while (not self.coordinates[len(self.coordinates) - 1].x == x_end and not self.coordinates[len(self.coordinates) - 1].y == y_end):
			tmp_x = tmp_y = -1
			tmp = self.coordinates[ len( self.coordinates ) - 1]
			while (not (tmp_x == x_end and tmp_y == y_end) and self.inRoom(room, tmp_x, tmp_y) or self.inOutWindow(tmp_x, tmp_y, szWindow_x, szWindow_y)) : 

				r = random.randint(0, 1)
				r2 = random.uniform(0, 10)

				if  r == 0 :
					if r2 < 8 :
						tmp_x = tmp.x + 1 * self.sign(x_end-tmp_x)
					else :
						tmp_x = tmp.x - 1 * self.sign(x_end - tmp_x)
					
					tmp_y = tmp.y

				else :
					if r2 < 8 :
						tmp_y = tmp.y + 1 * self.sign(y_end - tmp_y)
					else :
						tmp_y = tmp.y - 1 * self.sign(y_end - tmp_y)
					tmp_x = tmp.x
			print tmp_x, "/", tmp_y
			self.coordinates.append( Identity ( "coordinates", 'X', tmp_x, tmp_y, 1, 1))

	def inRoom(self, room, x, y) :
		for i in range(len(room)):
			tmp = room[i]
			if  x >= tmp.x and x <= tmp.x + tmp.size_x and tmp.y <= y and y <= tmp.y+tmp.size_y :
				return True

		return False

	def inOutWindow(self, x, y, szWindow_x, szWindow_y) :
		return x < 0 or x > szWindow_x - 1 or y < 0 or y > szWindow_y - 1
	
	def sign(self, n) :
		if n > 0 :
			return 1 
		if n < 0 :
		 	return -1
		if n == 0:
			return 0
