from Identity import Identity

class Room ( Identity ) :
	def __init__ ( self, x, y, size_x, size_y) :
		Identity.__init__(self, "Room",'.', x, y, size_x, size_y)

	
