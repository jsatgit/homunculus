from Tkinter import *
import time
import random
from scipy import stats
import numpy
from creature import *

class CreatureSelection:
	def __init__(self, master):
		self.cur = IntVar()
		self.cur.set(0)

		l = Creatures.listing
		for i in xrange(len(l)):
			r = Radiobutton(master, 
							 text=l[i].name, 
							 variable=self.cur, 
							 value=i)
			r.pack()

class Graphics:
	def __init__(self, 	
		winHeight = 800, 
		winWidth  = 800, 
		creatSize = 10, 
		tickTime  = 0.1, 
		maxApart  = 50):	

		self.root = Tk()
		self.height = winHeight 
		self.width = winWidth
		self.sqW = creatSize
		self.creatures = []
		self.canvas = Canvas(self.root, 
			width=self.width,
			height=self.height, 
			highlightthickness=0)
		self.tickTime = tickTime
		self.maxApart = maxApart
		self.running = 1
		self.creatureSelection = CreatureSelection(self.root)

	top = Toplevel()
	top.mainloop()
		
	def start(self):
		self.root.protocol("WM_DELETE_WINDOW", self.__onClose)
		self.canvas.bind("<Button-1>", self.__onClick)
		self.canvas.pack()
		self.__tick()
	
	def __onClose(self):
		self.running = 0
		self.root.destroy()

	def __onClick(self, event):
		x1 = event.x
		y1 = event.y
		x2 = x1 + self.sqW
		y2 = y1 + self.sqW

		typ = self.creatureSelection.cur.get()
		cts = Creatures.listing 
		sq = self.canvas.create_rectangle(x1, y1, x2, y2, 
											fill=cts[typ].colour, 
											width=0)
		c = Creature(typ, 
					 sq, 
					 cts[typ].colour, 
					 cts[typ].speed, 
					 cts[typ].movement) 
		self.creatures.append(c)

	def __randMove(self, movement):
		r = movement.rvs()
		if r == 0:
			return (1,0)
		elif r == 1:
			return (1,1)
		elif r == 2:
			return (0,1)
		elif r == 3:
			return (-1,1)
		elif r == 4:
			return (-1,0)
		elif r == 5:
			return (-1,-1)
		elif r == 6:
			return (0,-1)
		elif r == 7:
			return (1,-1)
		
	def __giveSpeed(self, m, speed):
		return (speed*m[0], speed*m[1])

	def __adjust(self, c, m):
		coord = self.canvas.coords(c)
		x1 = coord[0] + m[0]
		y1 = coord[1] + m[1]
		if x1 < 0:
			dx = 1	
		elif x1 >= self.width:
			dx = -1
		else:
			dx = m[0]
		if y1 < 0:
			dy = 1
		elif y1 >= self.height:
			dy = -1
		else:
			dy = m[1]
		return (dx, dy)

	def __move(self):
		for c in self.creatures:
			co = c.graphicsObj
			rm = self.__randMove(c.movement)
			spm = self.__giveSpeed(rm, c.speed)
			adj = self.__adjust(co, spm)
			self.canvas.move(co, adj[0], adj[1])

	def __close(self, i,j):
		ci = self.canvas.coords(self.creatures[i].graphicsObj)
		cj = self.canvas.coords(self.creatures[j].graphicsObj)
		cix = ci[0]
		ciy = ci[1]
		cjx = cj[0]
		cjy = cj[1]
		xapart = abs(cix - cjx)
		yapart = abs(ciy - cjy)
		if xapart < self.maxApart and yapart < self.maxApart:
			return 1
		else:
			return 0

	def __collisions(self):
		n = len(self.creatures)
		neighbours = numpy.zeros(n)
		for i in xrange(0,n-1):
			for j in xrange(i+1,n):
				if self.__close(i,j):
					neighbours[i] = 1
					neighbours[j] = 1
		
		for i in xrange(0,n):
			if neighbours[i]:
				self.canvas.itemconfig(self.creatures[i].graphicsObj, fill="red")	
			else:
				self.canvas.itemconfig(self.creatures[i].graphicsObj, fill=self.creatures[i].colour)	

	def __tick(self):
		while self.running:
			self.__move()
			self.__collisions()
			self.canvas.update()
			time.sleep(self.tickTime)

def main():
	# Construct Graphics with custom parameters like:
    # 	Graphics(speed=10, maxapart=20)	

	g = Graphics(tickTime = 0.01)
	g.start()

if __name__ == "__main__":
	main()
