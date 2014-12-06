from Tkinter import *
import time
import random
from numpy import linspace
from scipy import *
from scipy.interpolate import UnivariateSpline 

# window dimensions
winHeight = 500 
winWidth  = 500

# tk and canvas object
root = Tk()
canvas = Canvas(root, width=winWidth, height=winHeight, highlightthickness=0)

# number of seconds per refresh
tick = 0.01

# square/circle width/diameter (h - half)
sqw = 6
sqhw = sqw/2

# number of points generated  between
# first and last sample point in an iteration
grain = 1000

# number of random points sampled per iteration
nsamples = 10

# starting coordinate
initX = 30
initY = 30

# smoothing factor
sfact = 1

def rect(x,y):	
	nx = x - sqhw
	ny = y - sqhw
	return canvas.create_rectangle(nx, ny, 
			nx+sqw, ny+sqw, fill="red", width=0)	

def circ(x,y):
	nx = x - sqhw
	ny = y - sqhw
	return canvas.create_oval(nx, ny, 
			nx+sqw, ny+sqw, fill="red", width=0)	


def sample(n, x, y):
	xs = [x]
	ys = [y]
	for i in xrange(n): 
		x = random.randint(winWidth)
		y = random.randint(winHeight)
		xs.append(x)
		ys.append(y)
	return (xs, ys)

def norm(x0, y0, x1, y1):
	return sqrt(pow((y1 - y0), 2) + pow((x1 - x0), 2))

def makeT(xs, ys):
	ts = [0]
	n = len(xs)
	for i in xrange(n-1):
		nm = norm(xs[i], ys[i], xs[i+1], ys[i+1])
		ts.append(ts[i] + nm)
	return ts

def plotpoints(xs, ys):
	n = len(xs)
	for i in xrange(n):
		circ(xs[i], ys[i])

def firstLast(t):
	first = t[0]
	n = len(t)
	last = t[n-1]
	return (first, last)

def getPath(x, y):
	(xs, ys) = sample(nsamples, x, y)
	ts = makeT(xs, ys)
	splinexs = UnivariateSpline(ts, xs, s=sfact) 
	splineys = UnivariateSpline(ts, ys, s=sfact)
	(first, last) = firstLast(ts)
	nts = linspace(first, last, grain)
	nxs = splinexs(nts)
	nys = splineys(nts)
	return (nxs, nys)

def main():
	root.wm_title("Interpolation test")
	canvas.pack()
	fx = initX
	fy = initY
	point = circ(fx, fy)
	while 1:
		(xs, ys) = getPath(fx, fy)
		n = len(xs)
		for i in xrange(1,n):
			# uncomment the line below to see path
			# circ(xs[i], ys[i])
			canvas.move(point, xs[i]-xs[i-1], ys[i]-ys[i-1])
			canvas.update()
			time.sleep(tick)
		fx = xs[n-1]
		fy = ys[n-1]
	root.mainloop()

if __name__ == "__main__":
	main()
