#!/usr/bin/python
# Simple program taking input from an xbox controller using pygame library
# and sending this data over a linux pipe to a java aplication.
import sys, os, pygame, serial, time
from contextlib import contextmanager
xbox = 0
send_file_path = '/tmp/xbox_to_java'
send_file = 0
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
arm_packet_skeleton = int('0x02CA00000000000000000000', 16)
turret_left_4 = int('0x0000FC180000000000000000', 16)
turret_left_3 = int('0x0000FD120000000000000000', 16)
turret_left_2 = int('0x0000FE0C0000000000000000', 16)
turret_left_1 = int('0x0000FF060000000000000000', 16)
turret_right_1 = int('0x000000FA0000000000000000', 16)
turret_right_2 = int('0x000001F40000000000000000', 16)
turret_right_3 = int('0x000002EE0000000000000000', 16)
turret_right_4 = int('0x000003E80000000000000000', 16)
shoulder_down_4 = int('0x00000000FC18000000000000', 16)
shoulder_down_3 = int('0x00000000FD12000000000000', 16)
shoulder_down_2 = int('0x00000000FE0C000000000000', 16)
shoulder_down_1 = int('0x00000000FF06000000000000', 16)
shoulder_up_1 = int('0x0000000000FA000000000000', 16)
shoulder_up_2 = int('0x0000000001F4000000000000', 16)
shoulder_up_3 = int('0x0000000002EE000000000000', 16)
shoulder_up_4 = int('0x0000000003E8000000000000', 16)
elbow_down_4 = int('0x000000000000FC1800000000', 16)
elbow_down_3 = int('0x000000000000FD1200000000', 16)
elbow_down_2 = int('0x000000000000FE0C00000000', 16)
elbow_down_1 = int('0x000000000000FF0600000000', 16)
elbow_up_1 = int('0x00000000000000FA00000000', 16)
elbow_up_2 = int('0x00000000000001F400000000', 16)
elbow_up_3 = int('0x00000000000002EE00000000', 16)
elbow_up_4 = int('0x00000000000003E800000000', 16)
wrist_down_4 = int('0x0000000000000000FC180000', 16)
wrist_down_3 = int('0x0000000000000000FD120000', 16)
wrist_down_2 = int('0x0000000000000000FE0C0000', 16)
wrist_down_1 = int('0x0000000000000000FF060000', 16)
wrist_up_1 = int('0x000000000000000000FA0000', 16)
wrist_up_2 = int('0x000000000000000001F40000', 16)
wrist_up_3 = int('0x000000000000000002EE0000', 16)
wrist_up_4 = int('0x000000000000000003E80000', 16)
wrist_left_4 = int('0x00000000000000000000FC18', 16)
wrist_left_3 = int('0x00000000000000000000FD12', 16)
wrist_left_2 = int('0x00000000000000000000FE0C', 16)
wrist_left_1 = int('0x00000000000000000000FF06', 16)
wrist_right_1 = int('0x0000000000000000000000FA', 16)
wrist_right_2 = int('0x0000000000000000000001F4', 16)
wrist_right_3 = int('0x0000000000000000000002EE', 16)
wrist_right_4 = int('0x0000000000000000000003E8', 16)
main_packet_skeleton = int('0x01C800000000', 16)
move_forward_4 = int('0x000000FA0000', 16)
move_forward_3 = int('0x000001F40000', 16)
move_forward_2 = int('0x000002EE0000', 16)
move_forward_1 = int('0x000003E80000', 16)
move_backward_1 = int('0x0000FF060000', 16)
move_backward_2 = int('0x0000FE0C0000', 16)
move_backward_3 = int('0x0000FD120000', 16)
move_backward_4 = int('0x0000FC180000', 16)
move_left_4 = int('0x00000000FC18', 16)
move_left_3 = int('0x00000000FD12', 16)
move_left_2 = int('0x00000000FE0C', 16)
move_left_1 = int('0x00000000FF06', 16)
move_right_1 = int('0x0000000000FA', 16)
move_right_2 = int('0x0000000001F4', 16)
move_right_3 = int('0x0000000002EE', 16)
move_right_4 = int('0x0000000003E8', 16)
arm_prev_packet = 0
main_prev_packet = 0
arm_toggle = 0
wrist_toggle = 0
drive_toggle = 1

def main():
    controller_init()
    send_file_init()
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
        print "Controller initialization complete!"

def send_file_init():
    # Initialize a pipe object.
    global send_file_path, send_file
    #os.remove(send_file_path)
    if not os.path.exists(send_file_path):
        os.mkfifo(send_file_path)
    print "Pipe initialization complete!"

def send(data):
    global send_file
    send_file = open(send_file_path, 'w')
    send_file.write(str(data) + '\n')
    send_file.close()

def control():
    #Main control loop.
    global xbox, send_file_path, send_file, a, b, x, y, lb, rb, back, start
    global bxb, ljp, rjp, hl, hr, hu, hd, lt, rt, lx, ly, rx, ry
    global arm_packet_skeleton, turret_left_4, turret_left_3, turret_left_2
    global turret_left_1, turret_right_1, turret_right_2, turret_right_3
    global turret_right_4, shoulder_down_4, shoulder_down_3, shoulder_down_2
    global shoulder_down_1, shoulder_up_1, shoulder_up_2, shoulder_up_3
    global shoulder_up_4, elbow_down_4, elbow_down_3, elbow_down_2, elbow_down_1
    global elbow_up_1, elbow_up_2, elbow_up_3, elbow_up_4
    global wrist_down_4, wrist_down_3, wrist_down_2, wrist_down_1
    global wrist_up_1, wrist_up_2, wrist_up_3, wrist_up_4
    global wrist_left_4, wrist_left_3, wrist_left_2, wrist_left_1
    global wrist_right_1, wrist_right_2, wrist_right_3, wrist_right_4
    global arm_prev_packet, arm_toggle, wrist_toggle, drive_toggle
    done=False
    while done==False:
        for event in pygame.event.get():
            # Button press handling.
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    a[2] = 1
                    #print "a pressed"
                elif event.button == 1:
                    b[2] = 1
                    #print "b pressed"
                elif event.button == 2:
                    x[2] = 1
                    #print "x pressed"
                elif event.button == 3:
                    y[2] = 1
                    #print "y pressed"
                elif event.button == 4:
                    lb[2] = 1
                    #print "left bumper pressed"
                elif event.button == 5:
                    rb[2] = 1
                    #print "right bumper pressed"
                elif event.button == 6:
                    back[2] = 1
                    #print "back pressed"
                    wrist_toggle = 0
                    if (arm_toggle == 0):
                        arm_toggle = 1
                        drive_toggle = 0
                    elif (arm_toggle == 1):
                        arm_toggle = 0
                        drive_toggle = 1
                elif event.button == 7:
                    start[2] = 1
                    #print "start pressed"
                    arm_toggle = 0
                    if (wrist_toggle == 0):
                        wrist_toggle = 1
                        drive_toggle = 0
                    elif (wrist_toggle == 1):
                        wrist_toggle = 0
                        drive_toggle = 1
                elif event.button == 8:
                    bxb[2] = 1
                    #print "big x button pressed"
                elif event.button == 9:
                    ljp[2] = 1
                    #print "left joystick push button pressed"
                elif event.button == 10:
                    rjp[2] = 1
                    #print "right joystick push button pressed"
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
                    #print "hat left pressed"
                elif event.value[0] == 0:
                    hl[2] = 0
                    hr[2] = 0
                elif event.value[0] == 1:
                    hr[2] = 1
                    #print "hat right pressed"
                if event.value[1] == 1:
                    hu[2] = 1
                    #print "hat up pressed"
                elif event.value[1] == 0:
                    hu[2] = 0
                    hd[2] = 0
                elif event.value[1] == -1:
                    hd[2] = 1
                    #print "hat down pressed"
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
                        #print "left joystick x axis value: " + str(lx[2])
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
                        #print "left joystick y axis value: " + str(ly[2])
                if event.axis == 2:
                    if event.value > 0:
                        if lt[2] != 1:
                            lt[2] = 1
                            arm_toggle = 1;
                            #print "left trigger pressed"
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
                        #print "right joystick x axis value: " + str(rx[2])
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
                        #print "right joystick y axis value: " + str(ry[2])
                if event.axis == 5:
                    if event.value > 0:
                        if rt[2] != 1:
                            rt[2] = 1
                            #print "right trigger pressed"
                    elif event.value <= 0:
                        if rt[2] != 0:
                            rt[2] = 0

        arm_cur_packet = arm_packet_skeleton
        # Turret Motion
        if (((lt[2] == 1) or (arm_toggle == 1)) and (lx[2] == -1)):
            arm_cur_packet = arm_cur_packet + turret_left_4
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (lx[2] == -.75)):
            arm_cur_packet = arm_cur_packet + turret_left_3
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (lx[2] == -.5)):
            arm_cur_packet = arm_cur_packet + turret_left_2
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (lx[2] == -.25)):
            arm_cur_packet = arm_cur_packet + turret_left_1
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (lx[2] == .25)):
            arm_cur_packet = arm_cur_packet + turret_right_1
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (lx[2] == .5)):
            arm_cur_packet = arm_cur_packet + turret_right_2
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (lx[2] == .75)):
            arm_cur_packet = arm_cur_packet + turret_right_3
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (lx[2] == 1)):
            arm_cur_packet = arm_cur_packet + turret_right_4
        
        # Shoulder Motion
        if (((lt[2] == 1) or (arm_toggle == 1)) and (ly[2] == -1)):
            arm_cur_packet = arm_cur_packet + shoulder_up_4
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ly[2] == -.75)):
            arm_cur_packet = arm_cur_packet + shoulder_up_3
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ly[2] == -.5)):
            arm_cur_packet = arm_cur_packet + shoulder_up_2
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ly[2] == -.25)):
            arm_cur_packet = arm_cur_packet + shoulder_up_1
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ly[2] == .25)):
            arm_cur_packet = arm_cur_packet + shoulder_down_1
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ly[2] == .5)):
            arm_cur_packet = arm_cur_packet + shoulder_down_2
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ly[2] == .75)):
            arm_cur_packet = arm_cur_packet + shoulder_down_3
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ly[2] == 1)):
            arm_cur_packet = arm_cur_packet + shoulder_down_4
       
        # Elbow Motion
        if (((lt[2] == 1) or (arm_toggle == 1)) and (ry[2] == -1)):
            arm_cur_packet = arm_cur_packet + elbow_up_4
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ry[2] == -.75)):
            arm_cur_packet = arm_cur_packet + elbow_up_3
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ry[2] == -.5)):
            arm_cur_packet = arm_cur_packet + elbow_up_2
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ry[2] == -.25)):
            arm_cur_packet = arm_cur_packet + elbow_up_1
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ry[2] == .25)):
            arm_cur_packet = arm_cur_packet + elbow_down_1
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ry[2] == .5)):
            arm_cur_packet = arm_cur_packet + elbow_down_2
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ry[2] == .75)):
            arm_cur_packet = arm_cur_packet + elbow_down_3
        elif (((lt[2] == 1) or (arm_toggle == 1)) and (ry[2] == 1)):
            arm_cur_packet = arm_cur_packet + elbow_down_4

        # Wrist Tilt Motion
        if (((rt[2] == 1) or (wrist_toggle == 1)) and (ry[2] == -1)):
            arm_cur_packet = arm_cur_packet + wrist_up_4
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (ry[2] == -.75)):
            arm_cur_packet = arm_cur_packet + wrist_up_3
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (ry[2] == -.5)):
            arm_cur_packet = arm_cur_packet + wrist_up_2
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (ry[2] == -.25)):
            arm_cur_packet = arm_cur_packet + wrist_up_1
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (ry[2] == .25)):
            arm_cur_packet = arm_cur_packet + wrist_down_1
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (ry[2] == .5)):
            arm_cur_packet = arm_cur_packet + wrist_down_2
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (ry[2] == .75)):
            arm_cur_packet = arm_cur_packet + wrist_down_3
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (ry[2] == 1)):
            arm_cur_packet = arm_cur_packet + wrist_down_4

        # Wrist Rotate Motion
        if (((rt[2] == 1) or (wrist_toggle == 1)) and (lt[2] == 0) and (rx[2] == -1)):
            arm_cur_packet = arm_cur_packet + wrist_left_4
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (lt[2] == 0) and (rx[2] == -.75)):
            arm_cur_packet = arm_cur_packet + wrist_left_3
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (lt[2] == 0) and (rx[2] == -.5)):
            arm_cur_packet = arm_cur_packet + wrist_left_2
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (lt[2] == 0) and (rx[2] == -.25)):
            arm_cur_packet = arm_cur_packet + wrist_left_1
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (lt[2] == 0) and (rx[2] == .25)):
            arm_cur_packet = arm_cur_packet + wrist_right_1
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (lt[2] == 0) and (rx[2] == .5)):
            arm_cur_packet = arm_cur_packet + wrist_right_2
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (lt[2] == 0) and (rx[2] == .75)):
            arm_cur_packet = arm_cur_packet + wrist_right_3
        elif (((rt[2] == 1) or (wrist_toggle == 1)) and (lt[2] == 0) and (rx[2] == 1)):
            arm_cur_packet = arm_cur_packet + wrist_right_4
        
        main_cur_packet = main_packet_skeleton
        # Forward and Backward Motion
        if ((rt[2] == 0) and (lt[2] == 0) and (ly[2] == -1)):
            main_cur_packet = main_cur_packet + move_backward_4
        elif ((rt[2] == 0) and (lt[2] == 0) and (ly[2] == -.75)):
            main_cur_packet = main_cur_packet + move_backward_3
        elif ((rt[2] == 0) and (lt[2] == 0) and (ly[2] == -.5)):
            main_cur_packet = main_cur_packet + move_backward_2
        elif ((rt[2] == 0) and (lt[2] == 0) and (ly[2] == -.25)):
            main_cur_packet = main_cur_packet + move_backward_1
        elif ((rt[2] == 0) and (lt[2] == 0) and (ly[2] == .25)):
            main_cur_packet = main_cur_packet + move_forward_1
        elif ((rt[2] == 0) and (lt[2] == 0) and (ly[2] == .5)):
            main_cur_packet = main_cur_packet + move_forward_2
        elif ((rt[2] == 0) and (lt[2] == 0) and (ly[2] == .75)):
            main_cur_packet = main_cur_packet + move_forward_3
        elif ((rt[2] == 0) and (lt[2] == 0) and (ly[2] == 1)):
            main_cur_packet = main_cur_packet + move_forward_4
        
        # Left and Right Motion
        if ((rt[2] == 0) and (lt[2] == 0) and (lx[2] == -1)):
            main_cur_packet = main_cur_packet + move_left_4
        elif ((rt[2] == 0) and (lt[2] == 0) and (lx[2] == -.75)):
            main_cur_packet = main_cur_packet + move_left_3
        elif ((rt[2] == 0) and (lt[2] == 0) and (lx[2] == -.5)):
            main_cur_packet = main_cur_packet + move_left_2
        elif ((rt[2] == 0) and (lt[2] == 0) and (lx[2] == -.25)):
            main_cur_packet = main_cur_packet + move_left_1
        elif ((rt[2] == 0) and (lt[2] == 0) and (lx[2] == .25)):
            main_cur_packet = main_cur_packet + move_right_1
        elif ((rt[2] == 0) and (lt[2] == 0) and (lx[2] == .5)):
            main_cur_packet = main_cur_packet + move_right_2
        elif ((rt[2] == 0) and (lt[2] == 0) and (lx[2] == .75)):
            main_cur_packet = main_cur_packet + move_right_3
        elif ((rt[2] == 0) and (lt[2] == 0) and (lx[2] == 1)):
            main_cur_packet = main_cur_packet + move_right_4

        #print "Arm packet:"
        #print arm_cur_packet
        print "Control Status (D-A-W): " + str(drive_toggle) + "-" + str(arm_toggle) + "-" + \
            str(wrist_toggle) + ". Arm Packet: " + str(hex(arm_cur_packet))
        #print "Main packet:"
        #print main_cur_packet
        #print hex(main_cur_packet)
        # Update and send packet.
        #if (arm_cur_packet != arm_prev_packet):
        #    arm_prev_packet = arm_cur_packet;
        #send("Arm")
        #time.sleep(.2)
        send(arm_cur_packet)
        time.sleep(1)
        #send("Body")
        #time.sleep(.2)
        #send(main_cur_packet)
        
        time.sleep(.2)

if __name__ == "__main__":
    main()
