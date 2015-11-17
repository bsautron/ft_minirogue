from Player import Player
from Door import Door
from Room import Room

q = Player("Quentin", 3, 5, 100)
p = Door(3,8)
print str(p.x)+"/"+str(p.y)
print "character :", p.c
q.move(10, 2)

r = Room(10, 8, 4, 2)
print "creation d'une :", r.type, " x = ",r.x, "y=",r.y,"sizex",r.size_x,"sizey",r.size_y

