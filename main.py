from Player import Player
from Door import Door
from Room import Room
from Corridor import Corridor

r1 = Room ( 5,5,3,3 )
r2 = Room (10,5,3,3)
r3 = Room (6,7,1,1)
r = []
r.append(r1)
r.append(r2)
r.append(r3)
print type(r)
print len(r)
l = Corridor(r,3,7,15,5,20,20)
print "fini"
