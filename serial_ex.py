#!/usr/bin/python

import serial

s = serial.Serial("/dev/ttyACM0")

while(True):
	l = s.readline() 
	x = l.rstrip().split(',')
	rgb = [int(val) for val in x]
	print rgb
	

