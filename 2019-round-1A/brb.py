from time import sleep

seconds = 10*60
while True:
	seconds -= 1
	print('Live stream starting in {} seconds (BRB!)'.format(seconds))
	sleep(1)
