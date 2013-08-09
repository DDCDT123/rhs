"""
This is a skeleton/base class that will encompass Forwards+Defensemen+Goalies, and the subclasses from there (if it goes that deep).

Basically everything that will be the focus of EVERY body on the ice will be stated here.  While this may or may not be a lot for a class,
this is the best way to do OOP, as far as I'm concerned, anyways.  Have a better suggestion?  Please for the love of JebusMonkeys let me know.
"""

class Player(object):
	# Is player injured?
	injured = False

	# Is player in penalty
	penalized = False

	# Time on ice (each index is per game, each game is in periods)
	"""
	This one is tricky as its basically structured like this:
	[0] = {1 : 3.24, 2 : 10, 3 : 5.1}

	So this means game 1 (index-0) the player was on the ice for 3.24% of the first period, 10% of the 2nd, etc...total of 18.34% of the game being on ice.
	"""
	ice_time = []

	# No idea why this is base-age, but eh
	age = 18

	# This is more so feet.inches (default height is 6' 1")
	height = 6.01

	# Weight is in lbs because I'm from America and I wasn't taught the SI system
	weight = 180.0

	# Position of player (relatively unimportant but could be used for statistical purposes)
	position = ""