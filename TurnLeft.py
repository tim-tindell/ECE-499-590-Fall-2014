import dynamixel
import time
from DynDefs import *

def TurnLeft(net,myActuators):

 	#set the starting position, standing straight
    for actuator in myActuators:
		if actuator.id==RHY or actuator.id==LHY:
			actuator.goal_position = rad2dyn(-.78)
		else:
			actuator.goal_position = rad2dyn(0)
    net.synchronize()
    time.sleep(3)
#<PHASE 1>MOVE CENTER OF MASS OVER RIGHT FOOT
    setGoal(myActuators,LHR,.22)
    setGoal(myActuators,RHR,.22)
    setGoal(myActuators,RAR,.22)
    setGoal(myActuators,LAR,.22)
    net.synchronize()
    time.sleep(1)

#<PHASE 2>PICK UP LEFT LEG
    amount=0
    while(amount<=.72):
        setGoal(myActuators,LHP,amount)
        setGoal(myActuators,LKN,2*amount)
        setGoal(myActuators,LAP,-amount)
        net.synchronize()		
        time.sleep(0.5)
        amount +=0.1
    net.synchronize()
    time.sleep(1)

#<PHASE 3>TWIST LEFT LEG TOWARD LEFT 30 DEGREES
    amount=0
    while(amount<=.52):
        setGoal(myActuators,LHY,((-.78) - amount))
        net.synchronize()		
        time.sleep(0.5)
        amount +=0.1
    net.synchronize()
    time.sleep(1)

#<PHASE 4>PUT LEFT LEG DOWN
    amount=0
    while(amount<=.72):
        setGoal(myActuators,LHP,(.72 - amount))
        setGoal(myActuators,LKN,(1.44 - (2*amount)))
        setGoal(myActuators,LAP,((-.72) + amount))
        net.synchronize()		
        time.sleep(0.5)
        amount +=0.1
    net.synchronize()
    time.sleep(1)    

#<PHASE 5>MOVE CENTER OF MASS TO CENTER    
    setGoal(myActuators,LHR,0)
    setGoal(myActuators,RHR,0)
    setGoal(myActuators,RAR,0)
    setGoal(myActuators,LAR,0)
    net.synchronize()
    time.sleep(1)

#<PHASE 6>MOVE CENTER OF MASS TO OVER THE LEFT FOOT    
    setGoal(myActuators,LHR,-.22)
    setGoal(myActuators,RHR,-.22)
    setGoal(myActuators,RAR,-.22)
    setGoal(myActuators,LAR,-.22)
    net.synchronize()
    time.sleep(1)

#<PHASE 7>PICK UP RIGHT LEG
    amount=0
    while(amount<=.72):
        setGoal(myActuators,RHP,-amount)
        setGoal(myActuators,RKN,-2*amount)
        setGoal(myActuators,RAP,amount)
        net.synchronize()		
        time.sleep(0.5)
        amount +=0.1
    net.synchronize()
    time.sleep(1)

#<PHASE 8>UNTWIST LEFT LEG TOWARD LEFT 30 DEGREES
    amount=0
    while(amount<=.52):
        setGoal(myActuators,LHY,((-1.3) + amount))
        net.synchronize()		
        time.sleep(0.5)
        amount +=0.1
    net.synchronize()
    time.sleep(1)

#<PHASE 9>PUT DOWN RIGHT LEG
    amount=0
    while(amount<=.72):
        setGoal(myActuators,RHP,-0.72 + amount)
        setGoal(myActuators,RKN,-1.44 + (2*amount))
        setGoal(myActuators,RAP, 0.72 - amount)
        net.synchronize()		
        time.sleep(0.5)
        amount +=0.1
    net.synchronize()
    time.sleep(1)

#<PHASE 10>GO BACK TO STARTING POSITION
    #set the starting position, standing straight
    for actuator in myActuators:
        if actuator.id==RHY or actuator.id==LHY:
	    actuator.goal_position = rad2dyn(-.78)
        else:
            actuator.goal_position = rad2dyn(0)
    net.synchronize()
    time.sleep(1)

