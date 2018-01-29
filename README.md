# lab1
Author: Austin Schober
Course: ES432
Instructor: Prof. Donnal

Intent: The goal of this lab is to gather PWM (analog) inputs with an Arduino Uno connected to a knob potentiometer and a potentiometer joystick.

Components: 
  1x Knob Potentiometer
  1x Joystick
  1x Arduino Uno
  1x RGB LED
  12x Wires
  1x Linux machine (virtual used in lab)
  1x 5V Source
  
Wiring:
  Joystick:
    +5V to power line (5V)
    GND to ground line
    Vrx to Arduino Uno A3
    Vry to Arduino Uno A2
  Knob Potentiometer:
    GND to ground line
    Vin to power line (5V)
    Out to Arduino Uno A1
  RGB LED:
    R to Arduino Uno ~P3
    G to Arduino Uno ~P5
    B to Arduino Uno ~P6
  Arduino Uno:
    GND to ground line
   
Arudino Uno Code (rgb_controller):
  1.) initialize a serial output with a 9600 baud rate
  2.) analogRead() from A3-A5 and save in variable
  3.) map() these analog values (between 0-1023) to a scale of 0 to 255 to accomplish 1-bit output
  4.) analogWrite() to ~P3, ~P5, ~P6 (or other pins with PWM ~ capabilities)
        Note: in order to match biologic light output, use gamma correction in output 
        Background: https://learn.adafruit.com/led-tricks-gamma-correction/the-issue
        Quick fix: https://learn.adafruit.com/led-tricks-gamma-correction/the-quick-fix
  5.) Serial.print() to get format r,g,b\n over serial output
  
Pygame code (colorscreen.py)
  1.) import pygame, serial, and sys
  2.) create screen object for color output
  3.) set up serial read to "/dev/ttyACM0" - this is the arduino uno
  4.) create function to read serial input and parse into list of integers
  5.) loop through serial read, display.fill(), update display
