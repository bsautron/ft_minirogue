class Identity :
	def __init__( self, type, character, x, y, size_x, size_y ) :
		print "Creation d'un " + type + " Pos " + str(x) + "/" + str(y), "Size " + str(size_x) + "/" + str(size_y)
		self.type = type
		self.x = x
		self.y = y
		self.size_x = size_x
		self.size_y = size_y
		self.c = character

	
