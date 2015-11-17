from Identity import Identity
import random

class Corridor() :
	def	__init__(self, room, beg, end, map) :
		self.coordinates = []
		self.coordinates.append(Identity("coordinates",'X',beg.x,beg.y,1,1))

		tmp_x = tmp_y = -1
		
		while (not self.coordinates[len(self.coordinates) - 1].isIn(end)):
			last = self.coordinates[ len( self.coordinates ) - 1]

			r = random.randint(0, 1)
			r2 = random.uniform(0, 10)

			if  r == 0 :
				if r2 < 8 :
					tmp_x = last.x + 1 * self.sign(end.x-tmp_x)
				else :
					tmp_x = last.x - 1 * self.sign(end.x - tmp_x)
				
				tmp_y = last.y

			else :
				if r2 < 8 :
					tmp_y = last.y + 1 * self.sign(end.y - tmp_y)
				else :
					tmp_y = last.y - 1 * self.sign(end.y - tmp_y)
				tmp_x = last.x

			new = Identity ("coordinates", 'X', tmp_x, tmp_y, 1, 1)
			print new, beg, end
			if (new.isIn(end) or (not new.isInList(room) and new.isIn(map))):
				self.coordinates.append( Identity ( "coordinates", 'X', tmp_x, tmp_y, 1, 1))
				continue
				

	def sign(self, n) :
		if n >= 0 :
			return 1
		return -1
