import math
import random
from tkinter import *
import tkinter


#CONST
GRAVITY = -9.8
CANVAS_WIDTH = 1000  #x
CANVAS_HEIGHT = 1000 #y

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

velocityLabel = Label(text="\n\nVelocity:")
velocityLabel.pack(side=tkinter.TOP)
velocityEntry = Entry(width=5)
velocityEntry.pack(side=tkinter.TOP)
velocityEntry.insert(0,"?")

degreeLabel = Label(text="Degree:")
degreeLabel.pack(side=tkinter.TOP)
degreeEntry = Entry(width=5)
degreeEntry.pack(side=tkinter.TOP)
degreeEntry.insert(0,"?")

velocityYLabel = Label(text="\n\nVelocity Y:")
velocityYLabel.pack(side=tkinter.TOP)
velocityYEntry = Entry(width=5)
velocityYEntry.pack(side=tkinter.TOP)
velocityYEntry.insert(0,"?")

velocityXLabel = Label(text="Velocity X:")
velocityXLabel.pack(side=tkinter.TOP)
velocityXEntry = Entry(width=5)
velocityXEntry.pack(side=tkinter.TOP)
velocityXEntry.insert(0,"?")



#FUNCTIONS

def Run(VX_Text,VY_Text,Degree_Text,V_Text):
    if((VX_Text != "?") & (VY_Text != "?")):
        print("WE USE X&Y")
        # w.create_rectangle(450, 450, 550, 550)
    elif((V_Text != "?") & (Degree_Text != "?")):
      print("WE USE D&V")
    else:
        return 0


def UpdateView():
    print("Updated!")

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


nextButton = Button(fInfo,text="Run", command=lambda: Run(velocityXEntry.get(),velocityYEntry.get(),velocityEntry.get(),degreeEntry.get())).pack(side=tkinter.TOP)

window.mainloop()
