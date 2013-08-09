"""
File containing various helper methods.  Nothing really special here but gives an idea on how the mechanics work.
"""
# A lot of our values will be decimal since they'll carry weights along with the actual value
from random import uniform

"""
gen_weight

Get a weight multiplier based on a characteristic's accuracy.

accuracy - The attribute's accuracy that we are geting a weight for.
attr - The attribute we are weighing for.

A random value is generated between between accuracy and 100.0 (since accuracy can only be 0.0 - 1.0), then divided by the attribute's value.
"""
def gen_weight(accuracy, attr):
	weight = uniform(accuracy, 1.0)

	return weight / attr

"""
do_pass

Returns a percentage value of likelihood that a pass will succeed.  This is then used to test if a defensemen will block it.

If the end result (after this call) is that the block value > do_pass value, pass is intercepted.  Otherwise, pass is made.
"""
def do_pass(player):
	speed = player.passing_speed / 100.0
	accuracy = player.passing_accuracy / 100.0

	# We are judging this against the accuracy
	return accuracy * uniform((speed * gen_weight(accuracy, speed)), 1.0)

def do_block(player):
	shot_blocking = player.shot_blocking / 100.0
	stick_checking = player.stick_checking / 100.0
	blocking_accuracy = player.blocking_accuracy / 100.0

	stick_check = uniform((stick_checking * gen_weight(stick_checking, blocking_accuracy)), 1.0)
	shot_block = uniform((shot_blocking * gen_weight(shot_blocking, blocking_accuracy)), 1.0)

	if stick_check > shot_block:
		return stick_check
	elif stick_check < shot_block:
		return shot_block

	return shot_block

"""
Below code demonstrates the above helpers.
"""
if __name__ == "__main__":
	class Player(object):
		passing_speed = 90
		passing_accuracy = 95
		shot_blocking = 78
		stick_checking = 87
		blocking_accuracy = 89

	p = Player()

	puck_pass = do_pass(p)
	block = do_block(p)

	print "> Pass:",puck_pass,"; Block:",block

	if puck_pass > block:
		print "> Pass made"
	else:
		print "> Block made"