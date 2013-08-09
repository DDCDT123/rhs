from bases.player import Player as PB

class Goalie(PB):
	# Glove variables
	glove_high = 50
	glove_low = 50

	# Stick/pad side variables
	stick_high = 50
	stick_low = 50

	# How good is the goalie at keeping his legs shut
	five_hole = 50

	# Through a screen how likely is it the goalie will see the puck?
	vision = 50