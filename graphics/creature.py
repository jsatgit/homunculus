from scipy import stats
import numpy

class Creature:
	def __init__(self, 
				 typ, 
				 graphicsObj, 
				 colour,
				 speed,
				 movement):
		self.typ = typ
		self.graphicsObj = graphicsObj
		self.colour = colour
		self.speed = speed
		self.movement = movement

class Prop:
	def __init__(self, name, colour, speed, movement):
		self.name = name
		self.colour = colour
		self.speed = speed
		self.movement = movement

class Movements:
	vals = numpy.arange(8)
	probs1 =  (0.25,0.25,0.1,0.1,0.1,0.1,0.05,0.05)
	moves1 = stats.rv_discrete(values=(vals, probs1))

class Creatures:
	listing = [
		Prop("Carrot", "orange", 0, Movements.moves1),
		Prop("Rabbit", "blue", 1, Movements.moves1),
		Prop("Wolf", "grey", 3, Movements.moves1)
	]
