2d space
	- positioning
	- integer

organisms
	communication
		- direct communications
	represented as points (for now)
		- coordinates of organism are the same, they are in the interact state
		- how to detect collision
			* position field, two parameters x and y
			* land also knows where the organisms are
				- need to keep a list of currently occupied land
				- keep a list of pointers to the land block containing animals
					* at every tick, for each occupied land block, look for duplicates
				- algorithm for duplicate
				- Algorithm -> find all pairs of integer that differ by at most 1? in linear time
	some form  of movement speed
		- counted by pixel / tick?
		
	evolution
		- organisms are given traits based of their species, slight variations will exist.
		- in certain times where species are dying, if the outlier survives, then the species itself will now shift to these outliers.
		- organism can also affect environment
		- partial environment can also be organisms (plants, tree, immobile organism)
		- environment allows certain immobile organisms to flourish 
		-> mobile organism feed on these immobile organisms 
		-> higher level organisms feed on these organism
		
	initiation state
		- certain level of interest?
	
	ignore state
		- characterized by disinterest
	
	random death parameter
	
predator prey model
	- dependent on initiation / ignore parameters?
	
PARAMETER LIST
	- hunger
	- warmth
	- interests in other organisms
	- random death parameter
	- happiness factor / angry
	- speed
	- status within known member of species
	- number of family member
	- relations with various organisms
	- problem solving abilities
	- vision
	- smell? measured by intensities. [perhaps for mating as well, but perhaps can also attract predators]
	- strength
	- mass
	- calories / energy
	- waste 
	- age

**BEGINNING STAGE**
- simple organisms
- non macro social organisms (can form packs, but not like tribes)
- goal is survive and reproduce
- carrot, bunny, wolf to start with *************
- carrots just grows
- bunnies will have random movement unless wanting to eat
	- random movement = vision based -> non uniform movement check around the squares
		*higher probability to squares within current vision view
- wolf eats bunnies, bunnies will attempt to escape

