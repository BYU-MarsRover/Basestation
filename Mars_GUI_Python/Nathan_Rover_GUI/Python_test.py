#######################
# Author: Nathan Warner
# created: 2 - 4 - 15
#######################

## convetions to be determined

import socket
import signal
import sys
import string

def main():

# A class is defined by using the class keyword followed by the class name and a colon
# usage: class <className>:
class Person:
	# class constructors are created/defined as follows
	#			<Note arguments>
	def __init__(name, age, gender):
		self.Name = name
		self.Age = age
		self.Gender = gender
		
	def ageAYear():
		self.Age += 1
	
	def setGender(newgender):
		self.Gender = newgender
	
	