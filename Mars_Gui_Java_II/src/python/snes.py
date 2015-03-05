#!/usr/bin/python
#Simple program taking input from snes controller using pygame library
#and sending this data serially over a uart using python.serial.
import sys, os, pygame, serial
from contextlib import contextmanager
snes = 0
x = [ 0, 'x', 'A']
a = [ 1, 'a', 'B']
b = [ 2, 'b', 'C']
y = [ 3, 'y', 'D']
l = [ 4, 'l', 'E']
r = [ 5, 'r', 'F']
select = [ 8, 'select', 'G']
start = [ 9, 'start', 'H']
up = [ ':', 'up', 'I', 'false']
down = [ ';', 'down', 'J', 'false']
left = [ '<', 'left', 'K', 'false']
right = [ '=', 'right', 'L', 'false']
buttons = [ x, a, b, y, l, r, select, start ]
uart = serial.Serial('/dev/ttyACM0', 9600)

def main():
    controller_init()
    control()

def controller_init():
    #pygame initialziation
    pygame.init()
    pygame.joystick.init()
    global snes
    snes = pygame.joystick.Joystick(0)
    snes.init()
    #uart.open()
    if not snes.get_name() == "2Axes 11Keys Game  Pad":
        sys.exit("Error, wrong gamepad: " + snes.get_name())
    else:
        print "Initialization complete!"

def control():
    #Main control loop.
    global snes
    done=False
    while done==False:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                uart.write(str(event.button))
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    print 'x'
                    #print "Released " + str(event.button)
                    uart.write(x[2])
                if event.button == 1:
                    print 'a'
                    #print "Released " + str(event.button)
                    uart.write(a[2])
                if event.button == 2:
                    print 'b'
                    #print "Released " + str(event.button)
                    uart.write(b[2])
                if event.button == 3:
                    print 'y'
                    #print "Released " + str(event.button)
                    uart.write(y[2])
                if event.button == 4:
                    print 'left'
                    #print "Released " + str(event.button)
                    uart.write(l[2])
                if event.button == 5:
                    print 'right'
                    #print "Released " + str(event.button)
                    uart.write(r[2])
                if event.button == 8:
                    print 'select'
                    #print "Released " + str(event.button)
                    uart.write(select[2])
                if event.button == 9:
                    print 'start'
                    #print "Released " + str(event.button)
                    uart.write(start[2])
            if event.type == pygame.JOYAXISMOTION:
                x_axis = 0
                y_axis = 0
                if event.axis == 0:
                    x_axis = event.value
                if event.axis == 1:
                    y_axis = event.value
                if x_axis < 0:
                    print "left"
                    left[3] = 'true'
                    if right[3] == 'true':
                        right[3] = 'false'
                        uart.write(right[2])
                    uart.write(left[0])
                if x_axis > 0:
                    print "right"
                    right[3] = 'true'
                    if left[3] == 'true':
                        left[3] = 'false'
                        uart.write(left[2])
                    uart.write(right[0])
                if x_axis == 0:
                    if left[3] == 'true':
                        left[3] = 'false'
                        uart.write(left[2])
                    if right[3] == 'true':
                        right[3] = 'false'
                        uart.write(right[2])
                if y_axis > 0:
                    print "down"
                    down[3] = 'true'
                    if up[3] == 'true':
                        up[3] = 'false'
                        uart.write(up[2])
                    uart.write(down[0])
                if y_axis < 0:
                    print "up"
                    up[3] = 'true'
                    if down[3] == 'true':
                        down[3] = 'false'
                        uart.write(down[2])
                    uart.write(up[0])
                if y_axis == 0:
                    if up[3] == 'true':
                        up[3] = 'false'
                        uart.write(up[2])
                    if down[3] == 'true':
                        down[3] = 'false'
                        uart.write(down[2])

if __name__ == "__main__":
    main()
