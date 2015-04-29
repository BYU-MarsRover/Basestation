#!/usr/bin/python
# Joseph DeVictoria - BYU ECEn 493 Mars Rover - 2015.
# Simple program taking input from an xbox controller using pygame library
# and sending this data over a linux pipe to a java aplication.

import sys, os, pygame, serial, time
from contextlib import contextmanager

# Global Declarations.
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
arm_packet_skeleton  = int('0x02CA000000000000000000000000', 16)
turret_mask          = int('0x0000FFFF00000000000000000000', 16)
shoulder_mask        = int('0x00000000FFFF0000000000000000', 16)
elbow_mask           = int('0x000000000000FFFF000000000000', 16)
wrist_vert_mask      = int('0x0000000000000000FFFF00000000', 16)
wrist_rotate_mask    = int('0x00000000000000000000FFFF0000', 16)
wrist_actuate_on     = int('0x00000000000000000000000003E8', 16)
wrist_actuate_off    = int('0x000000000000000000000000FC18', 16)
main_packet_skeleton = int('0x01C800000000000000000000', 16)
move_left_mask       = int('0x00000000FFFF000000000000', 16)
move_right_mask      = int('0x000000000000FFFF00000000', 16)
camera_pan_right     = int('0x000000000000000003E80000', 16)
camera_pan_left      = int('0x0000000000000000FC180000', 16)
camera_tilt_up       = int('0x0000000000000000000003E8', 16)
camera_tilt_down     = int('0x00000000000000000000FC18', 16)
turret_offset        = 80
shoulder_offset      = 64
elbow_offset         = 48
wrist_vert_offset    = 32
wrist_rotate_offset  = 16
wrist_actuate_offset = 0
move_left_offset     = 48
move_right_offset    = 32
camera_pan_offset    = 16
camera_tilt_offset   = 0
arm_prev_packet = 0
main_prev_packet = 0
arm_toggle = 0
wrist_toggle = 0
drive_toggle = 1
wrist_actuate_toggle = 0

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
    global wrist_actuate_on, wrist_actuate_off, wrist_actuate_toggle
    done=False
    while done==False:
        arm_cur_packet = arm_packet_skeleton
        main_cur_packet = main_packet_skeleton
        # Control variable updates.
        for event in pygame.event.get():
            # Button press handling.
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    a[2] = 1
		    wrist_actuate_toggle = 1
                    #print "a pressed"
                elif event.button == 1:
                    b[2] = 1
		    wrist_actuate_toggle = 0
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
                # Left trigger
                if event.axis == 2:
                    if event.value > 0:
                        if lt[2] != 1:
                            lt[2] = 1
                            drive_toggle = 0
                            arm_toggle = 1
                            wrist_toggle = 0
                    elif event.value <= 0:
                        if lt[2] != 0:
                            lt[2] = 0
                            drive_toggle = 1
                            arm_toggle = 0
                            wrist_toggle = 0
                # Right trigger
                if event.axis == 5:
                    if event.value > 0:
                        if rt[2] != 1:
                            rt[2] = 1
                            drive_toggle = 0
                            arm_toggle = 0
                            wrist_toggle = 1
                    elif event.value <= 0:
                        if rt[2] != 0:
                            rt[2] = 0
                            drive_toggle = 1
                            arm_toggle = 0
                            wrist_toggle = 0
                if event.axis == 0:
                    lx[2] = int(event.value * -1000)
                if event.axis == 1:
                    ly[2] = int(event.value * 1000)
                if event.axis == 3:
                    rx[2] = int(event.value * -1000)
                if event.axis == 4:
                    ry[2] = int(event.value * -1000)
        
        # Update Packet.
        if (arm_toggle == 1):
            if (wrist_toggle == 0):
                if (lx[2] > 80 or lx[2] < -80):
                    arm_cur_packet  += ((lx[2] << turret_offset) & turret_mask)
                if (ly[2] > 80 or ly[2] < -80):
                    arm_cur_packet  += ((ly[2] << shoulder_offset) & shoulder_mask)
                if (ry[2] > 80 or ry[2] < -80):
                    arm_cur_packet  += ((ry[2] << elbow_offset) & elbow_mask)
            else:
                if (rx[2] > 80 or rx[2] < -80):
                    arm_cur_packet  += ((rx[2] << wrist_rotate_offset) & wrist_rotate_mask)
                if (ry[2] > 80 or ry[2] < -80):
                    arm_cur_packet  += ((ry[2] << wrist_vert_offset) & wrist_vert_mask)
        else:
            if (wrist_toggle == 0):
                if (ly[2] > 80 or ly[2] < -80):
                    main_cur_packet += ((ly[2] << move_left_offset) & move_left_mask)
                if (ry[2] > 80 or ry[2] < -80):
                    main_cur_packet += ((ry[2] << move_right_offset) & move_right_mask)
            else:
                if (rx[2] > 80 or rx[2] < -80):
                    arm_cur_packet  += ((rx[2] << wrist_rotate_offset) & wrist_rotate_mask)
                if (ry[2] > 80 or ry[2] < -80):
                    arm_cur_packet  += ((ry[2] << wrist_vert_offset) & wrist_vert_mask)
        if (wrist_actuate_toggle == 1):
	    arm_cur_packet += wrist_actuate_on
	else:
	    arm_cur_packet += wrist_actuate_off
	if (hu[2] == 1):
            main_cur_packet += camera_tilt_up
        elif (hd[2] == 1):
            main_cur_packet += camera_tilt_down
        if (hr[2] == 1):
            main_cur_packet += camera_pan_right
        elif (hl[2] == 1):
            main_cur_packet += camera_pan_left

        # Print python code status (controller).
        print "Control Status (D-A-W): " + str(drive_toggle) + "-" + \
              str(arm_toggle) + "-" + str(wrist_toggle) + ". Arm Packet: " + \
              str(hex(arm_cur_packet)) + " Main Packet: " + \
              str(hex(main_cur_packet))
        
        # Update and send packet.
        send(arm_cur_packet)
        time.sleep(.01)
        send(main_cur_packet) 
        time.sleep(.01)

if __name__ == "__main__":
    main()
