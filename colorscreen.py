#!/usr/bin/python

import pygame, sys, serial, time

from pygame.locals import *

pygame.init()
# Create a 400x300 pixel screen
colordisplay = pygame.display.set_mode((400,300)) 
# Change the top caption
pygame.display.set_caption('Color Screen')

# Set up serial connection with arduino
s = serial.Serial("/dev/ttyACM0")

def serial_in():
	l = s.readline() 
	x = l.rstrip().split(',')
	rgb = [int(val) for val in x]
	return rgb

while(True):
	
	try:
		rgb = serial_in()
		print rgb
		colordisplay.fill((rgb[0],rgb[1],rgb[2]))
		pygame.display.update()
	except TypeError as e:
		s.flush()
		print 'The error as ' + str(e)
        
	except IndexError as e:
		s.flush()
		print 'The error as ' + str(e)

        except ValueError as e:
                s.flush()
                print 'The error as ' + str(e)

	
	
	
	

