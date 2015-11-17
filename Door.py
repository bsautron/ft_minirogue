from Identity import Identity

class Door ( Identity ) :
	def __init__( self, x , y) :
		Identity.__init__(self, "Door", '+',x, y, 1, 1)


