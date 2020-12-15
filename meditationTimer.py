# -*- coding: utf-8 -*-
"""
Leyla Tarhan
12/2020

run a simple, looping timer to remind you to take a break every so often.
timer sounds like a gong.

"""
# %% import libraries

import time
from datetime import datetime
from datetime import timedelta
from playsound import playsound


# %%

# main timer function
def meditationTimer(step, params = None):
	if nextStep == 'start' or nextStep == ' ':
		# get user input
		print('\n\n\nFill in the blanks below:')
		timerLengthString = input('take a break every ____ hours ')
		breakLengthString = input('breaks should last ____ minutes ')
		print('Do you want to set a one-time timer or a continuous loop?')
		timerType = input('1 = one-time, 2 = continuous loop: ')
		
		
		# store in params dict
		params = {};
		params['timerLengthString'] = timerLengthString;
		params['breakLengthString'] = breakLengthString;
		params['timerType'] = timerType;
		
		
	elif nextStep == '': # use existing params
		timerLengthString = params['timerLength'];
		breakLengthString = params['breakLength'];
		timerType = params['timerType'];
		
	# format as floats
	timerLength = float(timerLengthString)*60;
	breakLength = float(breakLengthString);		

    
    # timer loop
	if timerType == '2':
		print('timer will sound every ' + timerLengthString + ' hours for a ' + breakLengthString + '-minute break.')
	else:
		print('timer will sound in ' + timerLengthString + ' hours for a ' + breakLengthString + '-minute break.')
	print('starting now!')
    
	done = 0;
	while not done: # in timer mode
        
        # set a timer and let it run:
		breakStartTime = datetime.now() + timedelta(minutes = timerLength)
		breakStartTimeStr = breakStartTime.strftime('%I:%M %p')   
		print('\n\nnext break is at ' + breakStartTimeStr)
		time.sleep(60*timerLength) # pauses the code until the timer is up
        
		# when the timer's up, ring a gong:
		playsound('gong1.wav')
        
        # start a timer for the break
		print('time for a ' + breakLengthString + '-minute break...')
		time.sleep(60*breakLength)
        
        # play another gong to signal that the break is over
		playsound('gong2.wav')
		print('...break is over - back to work!')
		
		if timerType == '1': # one-time timer, so break out of the loop
			done = 1;
			return params, done;
			break;
        
    
# %% run the timer

print("Welcome to the meditation timer!")
looping = 1;
nextStep = 'start';
done = 0;
while looping:
	# run the timer in the relevant mode:
	if nextStep == 'start' or nextStep == ' ': # gather user input about the timer first
		(timerParams, done) = meditationTimer(nextStep); # will only return a value for 'done' if set a 1-time timer
	elif nextStep == '': # don't gather user input, just default to the pre-existing params
		(timerParams, done) = meditationTimer(nextStep, timerParams);
		
	if done == 1: # user set a 1-time timer that rang -- now give them the option to start a new one
		nextStep = input('ENTER to run this same timer again, SPACE to start a new timer, q to quit: ')
		if nextStep == 'q': # quit -- break out of the loop
			print('have a good day!');
			looping = 0;
			break
		
  
    
    