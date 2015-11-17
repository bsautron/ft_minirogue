class Identity :
	def __init__( self, type, character, x, y, size_x, size_y ) :
		print "Creation d'un " + type + " Pos " + str(x) + "/" + str(y), "Size " + str(size_x) + "/" + str(size_y)
		self.type = type
		self.x = x
		self.y = y
		self.size_x = size_x
		self.size_y = size_y
		self.c = character

	def renderMe(self, window):
		for i in range(self.y, self.y + self.size_y - 1):
			for j in range(self.x, self.x + self.size_x - 1):
				print "[" + str(j) + "/" + str(i) + "]"
				window.move(i, j)
				window.addch(self.c)

	def isIn(self, ident):
		for i in range(self.y, self.y + self.size_y):
			for j in range(self.x, self.x + self.size_x):
				if (i >= ident.y and i <= ident.y + ident.size_y and j >= ident.x and j <= ident.x + ident.size_x):
					return True
	
		return False


	
