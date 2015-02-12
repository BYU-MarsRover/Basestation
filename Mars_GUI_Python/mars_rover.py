#!/usr/bin/python
#Server for recieving UDP packets for Mars rover commands.
#This program can be run as a server or as a client depending on runtime flags.
#To run as a server the usage is: "mars_rover.py -S <IP> <SOCKET>"
#to run as a client the usage is: "mars_rover.py -C <IP> <SOCKET>"
#Joseph DeVictoria - 2014

# -- External Modules --
import socket
import signal
import sys
import string
import Tkinter
import thread
bound = 0

def main():
    # Registering interrupt handler.
    signal.signal(signal.SIGINT, signal_handler)
    # Initializing server object.
    if (len(sys.argv) > 3 and ((sys.argv[1] == "-S") or (sys.argv[1] == "-C")) \
    and sys.argv[3].isdigit()):
        if (sys.argv[1] == "-S"):
            print "Starting mars rover dedicated server..."
            # Instantiate server object.
            dedicated_server = m_server(sys.argv[2], int(sys.argv[3]))
            bound = 1
            # Begin server operation loop.
            dedicated_server.run_server()
        if (sys.argv[1] == "-C"):
            print "Starting mars rover client..."
            # Instantiating client object.
            rover_client = m_client(sys.argv[2], int(sys.argv[3]))
            bound = 1
            cgui = m_gui(None)
            cgui.title('Mars Rover Client')
            # Begin client operation loop.
            rover_client.run_client(cgui)
    else:
        print "Please specify whether this is a server or client."
        print "Server Usage: \"mars_rover.py -S <IP> <PORT>\""
        print "Client Usage: \"mars_rover.py -C <IP> <PORT>\""
        sys.exit(1)
    sys.exit(0)

def signal_handler(signal, frame):
    if (sys.argv[1] == "-S"):
        print "\n\rClosing down server..."
        if bound:
            dedicated_server.m_socket.close()
        sys.exit(1)
    if (sys.argv[1] == "-C"):
        print "\n\rClosing down client..."
        if bound:
            rover_client.m_socket.close()
        sys.exit(1)

class m_server:
    def __init__(self, server_ip, server_socket):
        self.m_address = (server_ip, server_socket)
        self.m_socket = server_socket
        self.build_socket()

    def build_socket(self):
        try:
            self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except:
            sys.exit('Unable to create socket.')
        try:
            self.m_socket.bind(self.m_address)
        except:
            sys.exit('Unable to bind socket to port.')

    def run_server(self):
        running = 1
        # Main listening loop.
        while running:
            data, addr = self.m_socket.recvfrom(1024)
            print "received message: ", data

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

    def run_client(self, cgui):
        running = 1
        # Main sending loop.
        while running:
            data = raw_input('Please give me a string to send: ')
            data = cgui.inputBox.get()
            self.m_socket.sendto(str(data), self.m_address)

class m_gui(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        #self.quitButton = Tkinter.Button(self, text='Quit', command=self.quit)
        self.inputName = Tkinter.Label(self, text='Enter a string to send:')
        self.inputBox = Tkinter.Entry(self)
        #self.quitButton.grid()
        self.inputName.grid()
        self.inputBox.grid()

if __name__ == "__main__":
    main()
