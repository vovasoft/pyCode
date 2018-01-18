from TurtleWorld import *
from math import pi 
world = TurtleWorld()
bob = Turtle()
bob2 = Turtle()
print(bob)

bob.delay=0.01
bob2.delay=0.01
def polygon(t,length,n):
	for i in range(n):
		fd(t,length)
		lt(t,360.0/n)

print(pi)
		
def circle(t,r):
	circumference = 2*r*pi
	n = int(circumference/3)+1 
	length = circumference / n
	polygon( t, length, n)

def arc1(t,r,angle):
	arc_length = 2*r*pi*angle/360
	n = int(arc_length/3)+1 
	stemp_length = arc_length / n
	stemp_angle = float(angle)/n
	for i in range(n):
		fd(t,stemp_length)
		lt(t,stemp_angle)
def arc2(t,r,angle):
	arc_length = 2*r*pi*angle/360
	n = int(arc_length/3)+1 
	stemp_length = arc_length / n
	stemp_angle = float(angle)/n
	for i in range(n):
		fd(t,stemp_length)
		rt(t,stemp_angle)
		
def oneflower(t,r,n):
	arc1(t,r,360/n)
	lt(t,180-360/n)
	arc1(t,r,360/n)
	arc2(t,r,360/n)
	lt(t,180+360/n)
	arc2(t,r,360/n)

def flowers(t,r,n):
	for i in range(int(n/2)):
		oneflower(t,r,n);
		t.lt(360/n)
#polygon(bob2,100,1)
#circle(bob,50)
#arc(bob,50,180)
flowers(bob,100,5)


wait_for_user()


