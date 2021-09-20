import pygame
from random import randint
import itertools
pygame.init()
import math
#font=pygame.font.Font('arial.ttf',25)

Point={'Point','x,y'}
WHITE=(255,255,255)
RED=(200,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
BLACK=(0,0,0)
colors=[WHITE,RED,BLUE,GREEN,YELLOW,BLACK]
display_w=1280
display_h=960
BLOCKSIZE=20
maxx=(display_w//2)//BLOCKSIZE
maxy=(display_h//2)//BLOCKSIZE
maxx=200
maxy=200
v=maxx*maxy
d=35






SPEED=50


display=pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Gui für Aale')
clock=pygame.time.Clock()

i=0
#point=namedtuple('Point','x,y')
		

#class Block(maxx,maxy):
#		x=randint(0,maxx)
#		y=randint(0,maxy)
#		c=colors[randint(0,5)]
#		block=Block(x,y,c)
#		return block

def draw(p,c):
	x,y=p
	x=(x*BLOCKSIZE)+(display_w//2)
	y=(y*BLOCKSIZE)+(display_h//2)
	pygame.draw.rect(display,c,pygame.Rect((x,y),(BLOCKSIZE,BLOCKSIZE)))
	
def updateui(items):
	
#	blocks=[]
#	for i in range(2000):
#		blocks.append(generate_block(64,48))
	display.fill(BLACK)
	for item in items:
		#print(item)
		draw(item,GREEN)

#	for block in blocks:
#		pygame.draw.rect(display,block.c,pygame.Rect(block.x*BLOCKSIZE,block.y*BLOCKSIZE,BLOCKSIZE,BLOCKSIZE))
	pygame.display.flip()
	

def neighbors(point):
	x,y=point
	yield x +1, y
	yield x -1, y
	yield x, y+1
	yield x, y-1
	yield x +1, y+1
	yield x +1, y-1
	yield x -1, y+1
	yield x -1, y-1


def advance(state):
	newstate = set()
	newfocus = set()
	focusright=((display_w//BLOCKSIZE)//2)
	focusleft=focusright*-1
	focusbottom=(display_h//BLOCKSIZE)//2
	focustop=focusbottom*-1
	recalc = state | set(itertools.chain(*map(neighbors,state)))
	#recalc=state+set(itertools.chain(*map(neighbors,state)))
	for point in recalc:
		count = sum((neigh in state)
					for neigh in neighbors(point))
		if count == 3 or (count == 2 and point in state):
			newstate.add(point)
			x,y=point
			if (x>focusleft) and (x<focusright) and (y>focustop) and (y<focusbottom):
				newfocus.add(point)
	return newstate,newfocus
def main():
	glider = set([(0,0),(1,0),(2,0),(0,1),(1,2)])
	seed=[]
	
	for x in range(-maxx,maxx,1):
		for y in range(-maxy,maxy,1):
			#distance_to_center
			c2=(x*x+y*y)
			if c2 != 0 :
				dst=math.sqrt(c2)
				#print(x,' ',y,dst)
				print(x,y)

			if randint(0,100)<d:
				seed.append((x,y))
	state=set(seed)
	#print(newset)
		#state.add(newpoint)
		

	i=0	
	while True:
		print("cells : ",len(state),"iteration :",i)
		state,newfocus=advance(state)
		updateui(newfocus)
		clock.tick(SPEED)
		i=i+1
		#print("blub",i)
		#if i==20 : break
main()