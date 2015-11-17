from Alive import Alive

class Player ( Alive ) :
	def __init__ ( self, name, x, y, nbLife ) :
		Alive.__init__(self, "Player", 'P', x, y, nbLife)
		self.name = name
	
