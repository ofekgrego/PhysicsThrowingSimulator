import math
import random
from tkinter import *
import tkinter


#CONST
GRAVITY = -9.8
CANVAS_WIDTH = 1000  #x
CANVAS_HEIGHT = 1000 #y

#FUNCTIONS

def Run():
    print("hi")


def findDegree(V0_X, V0_Y):
    if (V0_X == 0):
        return 180;
    return math.degrees(math.atan(V0_Y / V0_X))


def totalVelocity(V0_X, V0_Y):
    return math.sqrt(math.pow(V0_X, 2) + math.pow(V0_Y, 2))


def findVelocityX(V0, degree):
    return math.cos(math.radians(degree)) * V0


def findVelocityY(V0, degree):
    return math.sin(math.radians(degree)) * V0


def findX(t, X0, V0_X, A_X):
    return X0 + (V0_X * t) + (A_X * t * t) / 2


def findY(t, Y0, V0_Y, A_Y):
    return Y0 + (V0_Y * t) + (A_Y * t * t) / 2


def timeY0(Y0, V0_Y):
    T0 = (-V0_Y+math.sqrt(V0_Y*V0_Y-2*GRAVITY*Y0))/GRAVITY
    T1 = (-V0_Y-math.sqrt(V0_Y*V0_Y-2*GRAVITY*Y0))/GRAVITY
    return max(T0, T1)


window = Tk()
window.title("Corona Simulator")
window.resizable(False,False) #disable resize
fCan = Frame(window, width=CANVAS_WIDTH, height=CANVAS_WIDTH+260)
fCan.pack(side=tkinter.LEFT)
w = Canvas(fCan, width=CANVAS_WIDTH,height=CANVAS_HEIGHT, background="gray")
w.pack()

graphCanvas = Canvas(fCan,width=CANVAS_WIDTH,height=260)
graphCanvas.pack()

graphCanvas.create_text(70,30, text="X", font="helvetica 20")
graphCanvas.create_line(50,50,50,250, width=3)
graphCanvas.create_line(50,250,500,250, width=3)
graphCanvas.create_text(580,30, text="Y", font="helvetica 20")
graphCanvas.create_line(550,50,550,250, width=3)
graphCanvas.create_line(550,250,1000,250, width=3)

fInfo = Frame(window, width=200, height=CANVAS_HEIGHT)
fInfo.pack()

creditLabel = Label(fInfo, text="Made By Ofek Grego").pack()
spaceLabel = Label(fInfo,text="").pack()

explainLabel = Label(fInfo, text="Enter Velocity and Degree \nOR\n Velocity X and Velocity Y \n(Leave the other with '?')").pack()

velocityLabel = Label(text="\n\nVelocity:").pack(side=tkinter.TOP)
velocityEntry = Entry(width=5).pack(side=tkinter.TOP)
degreeLabel = Label(text="Degree:").pack(side=tkinter.TOP)
degreeEntry = Entry(width=5).pack(side=tkinter.TOP)
velocityYLabel = Label(text="\n\nVelocity Y:").pack(side=tkinter.TOP)
velocityYEntry = Entry(width=5).pack(side=tkinter.TOP)
velocityXLabel = Label(text="Velocity X:").pack(side=tkinter.TOP)
velocityXEntry = Entry(width=5).pack(side=tkinter.TOP)

nextButton = Button(fInfo,text="Run", command=Run).pack(side=tkinter.TOP)

window.mainloop()
