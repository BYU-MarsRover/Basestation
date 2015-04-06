#!/usr/bin/python
# Simple program taking input a pipe and printing it out.

import os, time

def main():
    pipe_name = '/home/joseph/xbox_to_java'
    pipein = open(pipe_name, 'r')
    while True:
        line = pipein.readline()[:-1]
        print 'got "%s" at %s' % (line, time.time( ))
        time.sleep(.025)

if __name__ == "__main__":
    main()
