import sys
from DynDefs import *
import curses

try:

    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)
    stdscr.addstr(0,2,"Here are a list of the keys that can be pressed and what they do:")
    stdscr.addstr(2,2,"w: Walk Forward")
    stdscr.addstr(3,2,"s: Walk Backward")
    stdscr.addstr(4,2,"a: Turn Left")
    stdscr.addstr(5,2,"d: Turn Right")
    stdscr.addstr(6,2,"q: Exit Program")
    stdscr.refresh()
    key = ''

    while key != ord('q'):
        stdscr.addstr(10,2," ")
        key = stdscr.getch()
        #w
        if key == 119:
            stdscr.addstr(8,10,"Walking Forward             ")
          #  WalkForward(net,myActuators)
            stdscr.addstr(8,10,"Finished Walking Forward    ")
        #s
        elif key == 115: 
            stdscr.addstr(8,10,"Walking Backward            ")
       #     WalkBackward(net,myActuators)
            stdscr.addstr(8,10,"Finished Walking Backward   ")

        #a
        elif key == 97: 
            stdscr.addstr(8,10,"Turning Left                ")
     #       TurnLeft(net,myActuators)
            stdscr.addstr(8,10,"Finished Turning Left       ")

        #d
        elif key == 100:
            stdscr.addstr(8,10,"Turning Right               ")
    #        TurnRight(net,myActuators)
            stdscr.addstr(8,10,"Finished Turning Right      ")
        stdscr.addstr(10,2," ")
        stdscr.refresh()
    curses.endwin()   
except:
    curses.endwin()
    print "error occurred."
