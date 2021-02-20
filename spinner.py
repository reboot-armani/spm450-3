from Tkinter import *
import tkFont
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
running = False
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)

win = Tk()

def ledON(event):
#     global running
#     running = True
    test=0
    while True:
        print("inWhile")
        if(test == 5):
            break
        else:
            moveRight["text"] = "STARTED"
            frequency()
            test=test+1
            print(test)
    if GPIO.input(40) :
 		GPIO.output(40,GPIO.LOW)

def ledOFF(event):
#     global running
#     running = FALSE
    GPIO.output(40,GPIO.LOW)
    time.sleep(0.001)
    moveRight["text"] = "OFF"

def frequency():
    ledON()
    time.sleep(.0003)
    if GPIO.input(40) :
        GPIO.output(40,GPIO.LOW)
        time.sleep(.0003)
    
def onOFF():
	print("button pressed")
	if GPIO.input(40) :
 		GPIO.output(40,GPIO.LOW)
	else:
        GPIO.output(40,GPIO.HIGH)
        

def exitProgram():
	print("Exit Button pressed")
        GPIO.cleanup()
	win.quit()	


win.title("First GUI")
win.geometry('800x480')


moveRight = Button(win, text = "Right", height = 2, width =5 )
moveRight.place(x=100,y=10)
moveRight.bind('<ButtonPress-1>', ledON)
moveRight.bind('<ButtonRelease-1>', ledOFF)


mainloop()
