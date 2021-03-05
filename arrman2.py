from Tkinter import *
import tkFont
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
GPIO.output(32, GPIO.LOW)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)
GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.LOW)

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 8, weight = 'bold')

def testThisMsg():
   	print("HIHIHIH")
def setLow(pinNum):
	GPIO.output(pinNum,GPIO.LOW)
def setHigh(pinNum):
	GPIO.output(pinNum,GPIO.HIGH)
def checkOn(pinNum):
	if GPIO.input(pinNum):
		return True
	else:
		return False

def spinRight():
	print("spinRight button pressed")
	# Set Direction first
	setHigh(36)
	setHigh(40)
	time.sleep(.000005) #comment out for fastest
	setLow(40)
	#time.sleep(.1) #need for led testing

def spinLeft():
	print("spinLeft button pressed")
	# Set Direction first
	setLow(36)
	setHigh(40)
	time.sleep(.000005) #comment out for fastest
	setLow(40)
	#time.sleep(.1) #need for led testing

def spinHold():
	print("spinHold button pressed")
	setHigh(32)
	time.sleep(.1)
	setLow(32)
	time.sleep(.1)

def spin():
	#print("spinFuncRunning")
	if checkOn(40) :
		setLow(40)
		#spinButton["text"] = "SPIN ON"
	else:
		setHigh(40)
		#spinButton["text"] = "SPIN OFF"

def spinForSetTime():
	loopCount=10000000
	interval=.15015 #seconds, halved due to on/off
	while loopCount>0:
		spin()
		time.sleep(interval)
		loopCount=loopCount-1
		#print(loopCount)
	if checkOn(40):
		setLow(40)

def exitProgram():
	print("Exit Button pressed")
	GPIO.cleanup()
	win.quit()	


win.title("First GUI")
win.geometry('800x480')

exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 10) 
exitButton.pack(side = BOTTOM)

spinButton = Button(win, text = "SPIN ON", font = myFont, command = spin, height = 2, width =10 )
spinButton.pack()

spinForSetTimeButton = Button(win, text = "SpinForSetTime", font = myFont, command = spinForSetTime, height = 2, width =10)
spinForSetTimeButton.place(x=100,y=100)

#RepeatIsIn(ms)
spinHoldButton = Button(win, text = "spinHoldButton", repeatdelay=1, repeatinterval=1, command=spinHold, height = 2, width =10 )
spinHoldButton.place(x=100,y=200)

spinRightButton = Button(win, text = "RIGHT", repeatdelay=1, repeatinterval=1, command=spinRight, height = 5, width =10 )
spinRightButton.place(x=500,y=300)

spinLeftButton = Button(win, text = "LEFT", repeatdelay=1, repeatinterval=1, command=spinLeft, height = 5, width =10 )
spinLeftButton.place(x=200,y=300)

win.mainloop()