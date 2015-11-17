from Identity import Identity

class Alive ( Identity ) :
	def __init__( self, type, character, x, y, nbLife) :
		Identity.__init__(self, type, character, x, y, 1, 1)
		self.nbLife = nbLife
	
# pas de verification si le deplacement est posible ou non.
	def move(self, x, y) :
		print self.name, "move to", x, y
		self.x = x
		self.y = y
	
