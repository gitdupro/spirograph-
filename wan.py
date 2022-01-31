from turtle import up,down,setpos,mainloop,color
from math import sin,cos,radians,fabs
def clc(x,y,R):
	up()
	setpos(x+R,0)
	down()
	for t in range(1,361):
		t=radians(t)
		setpos(x+R*cos(t),y+R*sin(t))
def wanin(x,y,R,r):
	d=R-r
	for t in range(1,10000):
		t=radians(t)
		dx=d*cos(t)
		dy=d*sin(t)
		cx=r*cos(-R*t/r)
		cy=r*sin(-R*t/r)
		setpos(x+dx+cx,y+dy+cy)
		if fabs(dx+cx-R)<0.25 and fabs(dy+cy)<0.25:
			break
def wanout(x,y,R,r):
	d=R+r
	for t in range(1,10000):
		t=radians(t)
		dx=d*cos(t)
		dy=d*sin(t)
		cx=r*cos(3.1415926+R*t/r)
		cy=r*sin(3.1515926+R*t/r)
		setpos(x+dx+cx,y+dy+cy)
		if fabs(dx+cx-R)<0.25 and fabs(dy+cy)<0.25:
			break

color("red")		
R=500
r=85
x,y=0,0
clc(x,y,R)
wanin(x,y,R,r)

x+=100
R+=30
clc(x,y,R)
wanin(x,y,R,r)

clc(50,50,350)
wanout(50,50,350,50)
mainloop()