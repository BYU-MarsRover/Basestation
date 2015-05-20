#!/usr/bin/python
# Joseph DeVictoria - BYU ECEn 493 Mars Rover - 2015.
# Simple program taking input from an xbox controller using pygame library
# and sending this data over a linux pipe to a java aplication.

import sys, os, pygame, time, socket, signal, string, thread, threading, struct
from contextlib import contextmanager
from array import *

# Global Declarations.
xbox = 0
send_file_path = r'bin\xbox_to_java'
default_base_ip = '192.168.10.3'
default_arm_ip = '192.168.10.4'
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
arm_packet_skeleton  = int('0x02CA0000000000000000000000000000', 16)
turret_mask          = int('0x0000FFFF000000000000000000000000', 16)
shoulder_mask        = int('0x00000000FFFF00000000000000000000', 16)
elbow_mask           = int('0x000000000000FFFF0000000000000000', 16)
wrist_vert_mask      = int('0x0000000000000000FFFF000000000000', 16)
wrist_rotate_mask    = int('0x00000000000000000000FFFF00000000', 16)
wrist_actuate_on     = int('0x00000000000000000000000003E80000', 16)
wrist_actuate_off    = int('0x000000000000000000000000FC180000', 16)
camera_one           = int('0x00000000000000000000000000001000', 16)
camera_two           = int('0x00000000000000000000000000002000', 16)
camera_three         = int('0x00000000000000000000000000003000', 16)
laser_zero           = int('0x00000000000000000000000000000000', 16)
laser_one            = int('0x00000000000000000000000000000001', 16)
main_packet_skeleton = int('0x01C800000000000000000000', 16)
move_right_mask      = int('0x00000000FFFF000000000000', 16)
move_left_mask       = int('0x000000000000FFFF00000000', 16)
camera_pan_right     = int('0x000000000000000003E80000', 16)
camera_pan_left      = int('0x0000000000000000FC180000', 16)
camera_tilt_up       = int('0x0000000000000000000003E8', 16)
camera_tilt_down     = int('0x00000000000000000000FC18', 16)
turret_offset        = 96
shoulder_offset      = 80
elbow_offset         = 64
wrist_vert_offset    = 48
wrist_rotate_offset  = 32
wrist_actuate_offset = 16
ctl_toggle_offset    = 0
move_right_offset    = 48
move_left_offset     = 32
camera_pan_offset    = 16
camera_tilt_offset   = 0
arm_prev_packet = 0
main_prev_packet = 0
arm_toggle = 0
wrist_toggle = 0
drive_toggle = 1
rover_base_client = 0
rover_arm_client = 0
camera_toggle = 1
laser_toggle = 0

def main():
    global rover_base_client, rover_arm_client
    # Registering interrupt handler.
    signal.signal(signal.SIGINT, signal_handler)
    # Initializing server object.
    if (len(sys.argv) > 3 and sys.argv[3].isdigit()):
        print "Starting mars rover client..."
		# Initializing controller.
        controller_init()
        # Instantiating client object.
        rover_base_client = m_client(sys.argv[1], int(sys.argv[3]))
        rover_arm_client = m_client(sys.argv[2], int(sys.argv[3]))
        control()
    else:
        print "Client Usage: \"xbox.py <IP-BASE> <IP-ARM> <PORT>\""
        sys.exit(1)
    sys.exit(0)

def controller_init():
    # Pygame initialziation
    pygame.init()
    pygame.joystick.init()
    global xbox
    xbox = pygame.joystick.Joystick(0)
    xbox.init()
    if not xbox.get_name() == "Controller (XBOX 360 For Windows)":
        sys.exit("Error, wrong gamepad: " + xbox.get_name())
    else:
        print "Controller initialization complete!"
		
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
    global wrist_actuate_on, wrist_actuate_off, rover_base_client
    global rover_arm_client, camera_toggle, laser_toggle
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
                    lx[2] = int(event.value * 1000)
                if event.axis == 1:
                    ly[2] = int(event.value * -1000)
				
                if event.axis == 2:
                    # Left trigger
                    if event.value > .5:
                        if lt[2] != 1:
                            lt[2] = 1
                            drive_toggle = 0
                            arm_toggle = 1
                            wrist_toggle = 0
                    # Right trigger
                    elif event.value <= -.5:
                        if rt[2] != 1:
                            rt[2] = 1
                            drive_toggle = 0
                            arm_toggle = 0
                            wrist_toggle = 1
                    else:
                        lt[2] = 0
                        rt[2] = 0
                        drive_toggle = 1
                        arm_toggle = 0
                        wrist_toggle = 0
						
                if event.axis == 3:
                    ry[2] = int(event.value * -1000)
                if event.axis == 4:
                    rx[2] = int(event.value * 1000)
        
        # Update Packet.
        if (arm_toggle == 1):
            if (wrist_toggle == 0):
                if (lx[2] > 110 or lx[2] < -110):
                    arm_cur_packet  += ((lx[2] << turret_offset) & turret_mask)
                if (ly[2] > 110 or ly[2] < -110):
                    rev_s = -ly[2]
                    arm_cur_packet  += ((rev_s << shoulder_offset) & shoulder_mask)
                if (ry[2] > 110 or ry[2] < -110):
                    arm_cur_packet  += ((ry[2] << elbow_offset) & elbow_mask)
            else:
                if (rx[2] > 110 or rx[2] < -110):
                    arm_cur_packet  += ((rx[2] << wrist_rotate_offset) & wrist_rotate_mask)
                if (ry[2] > 110 or ry[2] < -110):
                    arm_cur_packet  += ((ry[2] << wrist_vert_offset) & wrist_vert_mask)
        else:
            if (wrist_toggle == 0):
                if (ly[2] > 110 or ly[2] < -110):
                    rev_ld = -ly[2]
                    main_cur_packet += ((rev_ld << move_left_offset) & move_left_mask)
                if (ry[2] > 110 or ry[2] < -110):
                    rev_rd = -ry[2]
                    main_cur_packet += ((rev_rd << move_right_offset) & move_right_mask)
            else:
                if (rx[2] > 110 or rx[2] < -110):
                    arm_cur_packet  += ((rx[2] << wrist_rotate_offset) & wrist_rotate_mask)
                if (ry[2] > 110 or ry[2] < -110):
                    arm_cur_packet  += ((ry[2] << wrist_vert_offset) & wrist_vert_mask)
        
        # Update actuator.
	    if (a[2] == 1):
	        arm_cur_packet += wrist_actuate_on
	    elif (b[2] == 1):
	        arm_cur_packet += wrist_actuate_off

        # Update camera position.
        if (hu[2] == 1):
            main_cur_packet += camera_tilt_up
        elif (hd[2] == 1):
            main_cur_packet += camera_tilt_down
        if (hr[2] == 1):
            main_cur_packet += camera_pan_right
        elif (hl[2] == 1):
            main_cur_packet += camera_pan_left

        # Update laser toggle.
        if (x[2] == 1):
            if (laser_toggle == 0):
                laser_toggle = 1
            else:
                laser_toggle = 0
        if (laser_toggle == 0):
            arm_cur_packet += laser_zero
        elif (laser_toggle == 1):
            arm_cur_packet += laser_one

        # Update camera toggle.
        if (y[2] == 1):
            if (camera_toggle == 1):
                camera_toggle = 2
            elif (camera_toggle == 2):
                camera_toggle = 3
            elif (camera_toggle == 3):
                camera_toggle = 1
        if (camera_toggle == 1):
            arm_cur_packet += camera_one
        elif (camera_toggle == 2):
            arm_cur_packet += camera_two
        elif (camera_toggle == 3):
            arm_cur_packet += camera_three

        # Print python code status (controller).
        print "Control Status (D-A-W): " + str(drive_toggle) + "-" + \
              str(arm_toggle) + "-" + str(wrist_toggle) + ". \nArm Packet: " + \
              str(hex(arm_cur_packet)) + "\nMain Packet: " + \
              str(hex(main_cur_packet))

        
        send_file = open(send_file_path, 'w')
        if (drive_toggle == 1):
            send_file.write('1')
        elif (arm_toggle == 1):
            send_file.write('2')
        elif (wrist_toggle == 1):
            send_file.write('3')
        send_file.close()
        
        # Update and send packet.
        main_byte_packet = array('B')
        arm_byte_packet = array('B')
        main_byte_packet.fromlist(get_bytes(11, main_cur_packet))
        arm_byte_packet.fromlist(get_bytes(15, arm_cur_packet))
        rover_base_client.send(main_byte_packet) 
        time.sleep(.01)
        rover_arm_client.send(arm_byte_packet)
        time.sleep(.01)
		
def signal_handler(signal, frame):
    global rover_base_client, rover_arm_client
    print "\n\rClosing down client..."
    #if bound:
    #    rover_base_client.m_socket.close()
    #    rover_arm_client.m_socket.close()
    sys.exit(1)

def get_bytes(size, data):
    new_array = []
    for i in range(size, 0, -1):
        new_array.append((data >> (i*8)) & 0xFF)
    return new_array

class m_client:
    def __init__(self, client_ip, client_socket):
        print client_ip
        self.m_address = (client_ip, client_socket)
        self.mc_socket = client_socket
        self.build_socket()

    def build_socket(self):
        try:
            self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except:
            sys.exit('Unable to create socket.')

    def send(self, data):
        self.m_socket.sendto(data, self.m_address)
		
if __name__ == "__main__":
    main()
