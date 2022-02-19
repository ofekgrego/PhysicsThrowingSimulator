import math

GRAVITY = -9.8

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