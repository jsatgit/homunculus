from Tkinter import *
import time
import random
from scipy import stats
import numpy

class Graphics:
	def __init__(self, 	
		winHeight = 800, 
		winWidth  = 800, 
		creatSize = 10, 
		speed 	  = 5, 
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
		self.speed = speed;
		self.tickTime = tickTime
		self.maxApart = maxApart
		self.xk = numpy.arange(8)
		#self.pk = (0.15, 0.1, 0.15, 0.1, 0.05, 0.1, 0.15, 0.2)
		self.pk =  (0.25,0.25,0.1,0.1,0.1,0.1,0.05,0.05)
		self.custMoves = stats.rv_discrete(values=(self.xk, self.pk))
		self.running = 1
		v = IntVar()
		self.currentCreature = 0
		Radiobutton(self.root, text="Rabbit", variable=v, value=1, command=self.__rabbitRadioButton).pack()
		Radiobutton(self.root, text="Wolf", variable=v, value=2, command=self.__wolfRadioButton).pack()
		
	def start(self):
		self.root.protocol("WM_DELETE_WINDOW", self.__onClose)
		self.canvas.bind("<Button-1>", self.__onClick)
		self.canvas.pack()
		self.__tick()
	
	def __onClose(self):
		self.running = 0
		self.root.destroy()
	
	def __onClick(self, event):
		if self.currentCreature == 0:
			color = "black"
		else:
			color = "green"
		x1 = event.x
		y1 = event.y
		x2 = x1 + self.sqW
		y2 = y1 + self.sqW
		c = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=0)
		#self.creatures.append(c)
		cr = Creature(self.currentCreature, c, color) 
		self.creatures.append(cr)

	def __uni(self):
		return random.randint(0, 7)

	def __des(self):
		return self.custMoves.rvs()

	def __randMove(self):
		r = self.__des()
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
		
	def __giveSpeed(self, m):
		return (self.speed*m[0], self.speed*m[1])

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
			rm = self.__randMove()
			spm = self.__giveSpeed(rm)
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
				self.canvas.itemconfig(self.creatures[i].graphicsObj, fill=self.creatures[i].color)	

	def __tick(self):
		while self.running:
			self.__move()
			self.__collisions()
			self.canvas.update()
			time.sleep(self.tickTime)
	def __rabbitRadioButton(self):
		self.currentCreature = 0
	def __wolfRadioButton(self):
		self.currentCreature = 1

class Creature:
	def __init__(self, creatureType, graphicsObj, color):
		self.creatureType = creatureType
		self.graphicsObj = graphicsObj
		self.color = color

def main():
	# Construct Graphics with custom parameters like:
    # 	Graphics(speed=10, maxapart=20)	

	g = Graphics(speed=2, tickTime = 0.01)
	g.start()

if __name__ == "__main__":
	main()
