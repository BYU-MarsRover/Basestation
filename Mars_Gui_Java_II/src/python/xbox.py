#!/usr/bin/python
# Simple program taking input from an xbox controller using pygame library
# and sending this data over a linux pipe to a java aplication.
import sys, os, pygame, serial
from contextlib import contextmanager
xbox = 0
a = [ 0, 'a', 0 ]
b = [ 1, 'b', 0 ]
y = [ 3, 'y', 0 ]
x = [ 2, 'x', 0 ]
lb = [ 4, 'lb', 0 ]
rb = [ 5, 'rb', 0 ]
back = [ 6, 'back', 0 ]
start = [ 7, 'start', 0 ]
bxb = [ 8, 'bxb', 0 ]
ljp = [ 9, 'ljp', 0 ]
rjp = [ 10, 'rjp', 0 ]
hl = [ 11, 'hl', 0 ]
hr = [ 12, 'hr', 0 ]
hu = [ 13, 'hu', 0 ]
hd = [ 14, 'hd', 0 ]
lt = [ 15, 'lt', 0 ]
rt = [ 16, 'rt', 0 ]
lx = [ 17, 'lx', 0 ]
ly = [ 18, 'ly', 0 ]
rx = [ 19, 'rx', 0 ]
ry = [ 20, 'ry', 0 ]
buttons = [ a, b, x, y, lb, rb, back, start, bxb, ljp, rjp, hl, hr, hu, hd, 
            lt, rt, lx, ly, rx, ry ]

def main():
    controller_init()
    control()

def controller_init():
    # Pygame initialziation
    pygame.init()
    pygame.joystick.init()
    global xbox
    xbox = pygame.joystick.Joystick(0)
    xbox.init()
    if not xbox.get_name() == "Microsoft X-Box 360 pad":
        sys.exit("Error, wrong gamepad: " + xbox.get_name())
    else:
        print "Initialization complete!"

def control():
    #Main control loop.
    global xbox, a, b, x, y, lb, rb, back, start, bxb, ljp 
    global rjp, hl, hr, hu, hd, lt, rt, lx, ly, rx, ry 
    done=False
    while done==False:
        for event in pygame.event.get():
            # Button press handling.
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    a[2] = 1
                    print "a pressed"
                elif event.button == 1:
                    b[2] = 1
                    print "b pressed"
                elif event.button == 2:
                    x[2] = 1
                    print "x pressed"
                elif event.button == 3:
                    y[2] = 1
                    print "y pressed"
                elif event.button == 4:
                    lb[2] = 1
                    print "left bumper pressed"
                elif event.button == 5:
                    rb[2] = 1
                    print "right bumper pressed"
                elif event.button == 6:
                    back[2] = 1
                    print "back pressed"
                elif event.button == 7:
                    start[2] = 1
                    print "start pressed"
                elif event.button == 8:
                    bxb[2] = 1
                    print "big X button pressed"
                elif event.button == 9:
                    ljp[2] = 1
                    print "left joystick push button pressed"
                elif event.button == 10:
                    rjp[2] = 1
                    print "right joystick push button pressed"
            # Button release handling.
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    a[2] = 0
                elif event.button == 1:
                    b[2] = 0
                elif event.button == 2:
                    x[2] = 0
                elif event.button == 3:
                    y[2] = 0
                elif event.button == 4:
                    lb[2] = 0
                elif event.button == 5:
                    rb[2] = 0
                elif event.button == 6:
                    back[2] = 0
                elif event.button == 7:
                    start[2] = 0
                elif event.button == 8:
                    bxb[2] = 0
                elif event.button == 9:
                    ljp[2] = 0
                elif event.button == 10:
                    rjp[2] = 0
            # Hat event handling.
            if event.type == pygame.JOYHATMOTION:
                if event.value[0] == -1:
                    hl[2] = 1
                    print "hat left pressed"
                elif event.value[0] == 0:
                    hl[2] = 0
                    hr[2] = 0
                elif event.value[0] == 1:
                    hr[2] = 1
                    print "hat right pressed"
                if event.value[1] == 1:
                    hu[2] = 1
                    print "hat up pressed"
                elif event.value[1] == 0:
                    hu[2] = 0
                    hd[2] = 0
                elif event.value[1] == -1:
                    hd[2] = 1
                    print "hat down pressed"
            # Joystick event handling.
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value < -0.85:
                        lx[2] = -1
                    elif event.value > -0.84 and event.value < -0.65:
                        lx[2] = -0.75
                    elif event.value > -0.64 and event.value < -0.35:
                        lx[2] = -0.5
                    elif event.value > -0.34 and event.value < -0.1:
                        lx[2] = -0.25
                    elif event.value > -0.1 and event.value < 0.1:
                        lx[2] = 0
                    elif event.value > 0.11 and event.value < 0.35:
                        lx[2] = 0.25
                    elif event.value > 0.36 and event.value < 0.65:
                        lx[2] = 0.50
                    elif event.value > 0.66 and event.value < 0.85:
                        lx[2] = 0.75
                    elif event.value > 0.86:
                        lx[2] = 1
                    if lx[2] != 0:
                        print "left joystick x axis value: " + str(lx[2])
                if event.axis == 1:
                    if event.value < -0.85:
                        ly[2] = -1
                    elif event.value > -0.84 and event.value < -0.65:
                        ly[2] = -0.75
                    elif event.value > -0.64 and event.value < -0.35:
                        ly[2] = -0.5
                    elif event.value > -0.34 and event.value < -0.1:
                        ly[2] = -0.25
                    elif event.value > -0.1 and event.value < 0.1:
                        ly[2] = 0
                    elif event.value > 0.11 and event.value < 0.35:
                        ly[2] = 0.25
                    elif event.value > 0.36 and event.value < 0.65:
                        ly[2] = 0.50
                    elif event.value > 0.66 and event.value < 0.85:
                        ly[2] = 0.75
                    elif event.value > 0.86:
                        ly[2] = 1
                    if ly[2] != 0:
                        print "left joystick y axis value: " + str(ly[2])
                if event.axis == 2:
                    if event.value > 0:
                        if lt[2] != 1:
                            lt[2] = 1
                            print "left trigger pressed"
                    elif event.value <= 0:
                        if lt[2] != 0:
                            lt[2] = 0
                if event.axis == 3:
                    if event.value < -0.85:
                        rx[2] = -1
                    elif event.value > -0.84 and event.value < -0.65:
                        rx[2] = -0.75
                    elif event.value > -0.64 and event.value < -0.35:
                        rx[2] = -0.5
                    elif event.value > -0.34 and event.value < -0.1:
                        rx[2] = -0.25
                    elif event.value > -0.1 and event.value < 0.1:
                        rx[2] = 0
                    elif event.value > 0.11 and event.value < 0.35:
                        rx[2] = 0.25
                    elif event.value > 0.36 and event.value < 0.65:
                        rx[2] = 0.50
                    elif event.value > 0.66 and event.value < 0.85:
                        rx[2] = 0.75
                    elif event.value > 0.86:
                        rx[2] = 1
                    if rx[2] != 0:
                        print "right joystick x axis value: " + str(rx[2])
                if event.axis == 4:
                    if event.value < -0.85:
                        ry[2] = -1
                    elif event.value > -0.84 and event.value < -0.65:
                        ry[2] = -0.75
                    elif event.value > -0.64 and event.value < -0.35:
                        ry[2] = -0.5
                    elif event.value > -0.34 and event.value < -0.1:
                        ry[2] = -0.25
                    elif event.value > -0.1 and event.value < 0.1:
                        ry[2] = 0
                    elif event.value > 0.11 and event.value < 0.35:
                        ry[2] = 0.25
                    elif event.value > 0.36 and event.value < 0.65:
                        ry[2] = 0.50
                    elif event.value > 0.66 and event.value < 0.85:
                        ry[2] = 0.75
                    elif event.value > 0.86:
                        ry[2] = 1
                    if ry[2] != 0:
                        print "right joystick y axis value: " + str(ry[2])
                if event.axis == 5:
                    if event.value > 0:
                        if rt[2] != 1:
                            rt[2] = 1
                            print "right trigger pressed"
                    elif event.value <= 0:
                        if rt[2] != 0:
                            rt[2] = 0

if __name__ == "__main__":
    main()
