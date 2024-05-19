import logging
import random
import time

while True:

	number	= random.randint(0, 4)

	if number == 0:
		logging.info("Hi guys, this is a debug message")
	elif number == 1:
		logging.warning("Guys, this is an warning message")
	elif number == 2:
		logging.error("Guys, this is an error message. PROD FELL")
	elif number == 3:
		logging.exception(Exception('this is an exception message'))
	
	time.sleep(1)
