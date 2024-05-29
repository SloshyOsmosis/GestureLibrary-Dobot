# version: Python3  
#Don't set robot speed higher than 60%
AccJ(100)#Joint acceleration, feel free to lower this number if the individual joint acceleration is too fast.
VelJ(100)#Joint velocity, lower this number if individual joint numbers are too fast.
CP(30)#Sets continuous positioning, allows for smoother motion between the points.

def stand():
  MovJ(P13)

stand()#Default position

def wave():
  for number in range (3): #Performs the action 3 times. It looks like it's waving!
    MovJ(P7, {"a":100, "v" :100}) # {"a":100, "v" :100} - Adjusts acceleration and velocity.
    MovJ(P8, {"a":100, "v" :100})
  ResetElapsedTime()#Resets internal timer
  stand()#Resets robot position
  Wait(2000)#Milliseconds, 2 second wait before moving onto the next action.
      
def spin():
  for number in range (2):
    MovJ(P13, {"a":100, "v" :100})
    MovJ(P14, {"a":100, "v" :100})
  ResetElapsedTime()
  stand()
  Wait(2000)
  
def nod():
  MovJ(P17)
  for number in range (1, 3):
    MovJ(P17, {"a":100, "v" :100})
    MovJ(P18, {"a":100, "v" :100})
    MovJ(P17)
  ResetElapsedTime()
  stand()
  Wait(2000)

def shake():
  for number in range (2):
    MovJ(P19 , {"a":100, "v" : 100})
    MovJ(P20 , {"a":100, "v" : 100})
  ResetElapsedTime()
  stand()
  Wait(2000)

def rockpaperscissors():
  for number in range (3):
    MovJ(P21 , {"a":100, "v" : 100})
    MovJ(P22 , {"a":100, "v" : 100})
    Wait(500)
  ResetElapsedTime()
  stand()
  Wait(2000)

def fistbump():
  for number in range (2):
    MovJ(P23, {"a":100, "v" : 100})
    MovJ(P24, {"a":100, "v" : 100})
    MovJ(P23, {"a":100, "v" : 100})
  ResetElapsedTime()
  stand()
  Wait(2000)
  
def shakehead():
  for number in range (3):
    MovJ(P25, {"a":100, "v" : 100})
    MovJ(P26, {"a":100, "v" : 100})
  ResetElapsedTime()
  stand()
  Wait(2000)

#Executes the gestures in the order they are written.
#My original plan was to introduce a way to have the user have the robot perform an action via a button pad or using voice control. Unfortunately due to hardware limitations this was the best I could do.
#In the future i hope to implement this, once I have access to the Dobot E6 magician accessories.
wave()
spin()
nod()
shake()
rockpaperscissors()
fistbump()
shakehead()