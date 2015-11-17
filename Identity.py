class Identity :
	def __init__( self, type, character, x, y, size_x, size_y ) :
		self.type = type
		self.x = x
		self.y = y
		self.size_x = size_x
		self.size_y = size_y
		self.c = character

	def renderMe(self, window):
		for i in range(self.y, self.y + self.size_y):
			for j in range(self.x, self.x + self.size_x):
				window.move(i, j)
				window.addch(self.c)

	def isIn(self, ident, margin=0):
		for i in range(self.y, self.y + self.size_y):
			for j in range(self.x, self.x + self.size_x):
				if (i >= ident.y - margin and i <= ident.y + ident.size_y  + margin and j >= ident.x - margin and j <= ident.x + ident.size_x + margin):
					return True
		return False

	def isInList(self, listIdent, margin=0):
		for i in range(len(listIdent)):
			if self.isIn(listIdent[i], margin):
				return True
		return False

	def __str__(self):
		return self.type + ": " + str(self.x) + "/" + str(self.y) + " (" + str(self.size_x) + "/" + str(self.size_y) + ")"

