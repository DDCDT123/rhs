"""
This class covers forwards and defensemen.

The attributes are from NHL 13's stats system with some slight additions to make generating a weight easier.
"""

"""

DDCDT123 editing here:

I've got some ideas for this, and maybe it will do better in different files, but I wanted to leave a comment
here at the top to see what you thought, then let you handle it. I'm going to be starting a Comp Sci major this
year and have been starting basic coding, so I'll attempt to do a basic framework here, but I'm not familier with python
in the slightest, so this is all guessing on how it would work and I'm probably TOTALLY off-base. 
I'd assume that you would put this all in different filesbut I wanted to put it here so you could see
it all in one spot. I mostly just wanted to formulate some ideas and be able to share.

There are different kinds of players, just like in NHL 13. Playmakers, PFs, TWF, Snipers, OFD, DFD, TWD. I think
that we could have base modifiers for each type of player. Most modifiers would be between 10-20, I'd recommend 
15 in most cases, 20 seems like too much. Depending on how you want to scale skill, many of these values may be too much.

"""
"""
class ply:
	# Offensive
	mod_deking = 8
	mod_off_awareness = 15
	mod_hand_eye = 15
	mod_off_awareness = 15
	mod_puck_control = 10
	mod_slapshot_accuracy = -15
	mod_slapshot_power = -15
	mod_wristshot_accuracy = -10
	mod_wristshot_power = -10
	
	# Defensive
	mod_aggressiveness = -10
	
class pf:
	# Offensive
	mod_puck_control = -10
	mod_slapshot_accuracy = 5
	mod_slapshot_power = 5
	mod_wristshot_accuracy = 5
	mod_wristshot_power = 5

	# Defensive
	mod_aggressiveness = 15 or 20
	mod_body_checking = 15
	mod_fighting_skill = 5

	# Athleticism
	mod_durability = 15
	mod_endurance = 10
	mod_strength = 20
	
class twf:
	# Offensive
	mod_off_awareness = 10
	mod_puck_control = 10
	mod_slapshot_accuracy = 5
	mod_slapshot_power = 5
	mod_wristshot_accuracy = 5
	mod_wristshot_power = 5

	# Defensive
	mod_def_awareness = 10
	mod_discipline = 5
	mod_shot_blocking = 10
	mod_stick_checking = 10
	mod_blocking_accuracy = 10

	# Athleticism
	mod_balance = 5
	
class sniper:
	# Offensive
	mod_hand_eye = 15
	mod_off_awareness = 15
	mod_puck_control = 15
	mod_slapshot_accuracy = 15
	mod_slapshot_power = 10
	mod_wristshot_accuracy = 15
	mod_wristshot_power = 10

	# Defensive
	mod_aggressiveness = -15
	mod_body_checking = -10
	mod_def_awareness = -15
	mod_shot_blocking = -5
	mod_stick_checking = -5
	mod_blocking_accuracy = -5

class ofd:
	# Offensive
	mod_deking = 5
	mod_off_awareness = 15
	mod_puck_control = 10
	mod_slapshot_accuracy = 20
	mod_slapshot_power = 10
	mod_wristshot_accuracy = 10
	mod_wristshot_power = 5

	# Defensive
	# I'm not really sure how much lower this should be, but I figured that some 
	# detrimental effects should be in order
	mod_aggressiveness = -5
	mod_def_awareness = -5
	mod_faceoffs = -15 # Reduced b/c defenseman
	mod_shot_blocking = -5
	mod_stick_checking = -5
	mod_blocking_accuracy = -5

class dfd:
	# Offensive
	mod_deking = -5
	mod_off_awareness = -10
	mod_slapshot_accuracy = -5
	mod_slapshot_power = -5
	mod_wristshot_accuracy = -5
	mod_wristshot_power = -5

	# Defensive
	mod_aggressiveness = 5
	mod_def_awareness = 15
	mod_faceoffs = -15
	mod_shot_blocking = 10
	mod_stick_checking = 10
	mod_blocking_accuracy = 10

class twd:
	# Offensive
	mod_deking = 5
	mod_off_awareness = 5
	mod_slapshot_accuracy = 5
	mod_slapshot_power = 5
	mod_wristshot_accuracy = 5
	mod_wristshot_power = 5

	# Defensive
	mod_def_awareness = 5
	mod_faceoffs = -15
	mod_shot_blocking = 5
	mod_stick_checking = 5
	mod_blocking_accuracy = 5
"""

from bases.player import Player as PB

class Skater(PB):
	# Offensive
	deking = 50
	hand_eye = 50
	off_awareness = 50
	puck_control = 50
	slapshot_accuracy = 50
	slapshot_power = 50
	wristshot_accuracy = 50
	wristshot_power = 50

	# Defensive
	aggressiveness = 50
	body_checking = 50
	def_awareness = 50
	discipline = 50
	faceoffs = 50
	fighting_skill = 50
	shot_blocking = 50
	stick_checking = 50
	blocking_accuracy = 50

	# Athleticism
	acceleration = 50
	agility = 50
	balance = 50
	durability = 50
	endurance = 50
	strength = 50
