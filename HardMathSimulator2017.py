# -*- coding: iso-8859-15 -*-
 #!/usr/bin/env Python
import math
from decimal import *
import time
import os
import random
from fractions import gcd

def clear():
    os.system("clear")

def trinomialFactoring():
    if Ain == 1:
        #Decide what the things should start as
        if Bin < 0 and Cin < 0:
            multdiv = Bin + Cin
        if Bin < 0:
            multdiv = ((Bin) - Cin)
        if Cin < 0:
            multdiv = (-1*Bin) + Cin
        if Bin > 0 and Cin > 0:
            multdiv = Bin + Cin
        originMultDiv = multdiv#Fun fact, multdiv was a typo and I just kinda rolled with it out of laziness.
        if multdiv > 0:
             Anchor = multdiv#Anchor
        if multdiv < 0:
            Anchor = -1*multdiv
        multdivTwo = multdiv
        while (multdiv <= Anchor):
            #==========
            while (multdivTwo <= Anchor):
                if multdiv + multdivTwo == Bin and multdiv * multdivTwo == Cin:
                    break
                multdivTwo += 1;
            #</multdivTwo_count>
            #==========
            if multdiv + multdivTwo == Bin and multdiv * multdivTwo == Cin:
                break
            multdiv += 1;
            multdivTwo = originMultDiv
            #</multdiv_count>
        #Print Result
        if (multdiv + multdivTwo == Bin) and (multdiv * multdivTwo == Cin):
            if multdiv < 0 and multdivTwo < 0:
                print ("(" + variable + " - " + format(-1*multdiv) + ")(" + variable + " - " + format(-1*multdivTwo) + ")")
            if multdiv > 0 and multdivTwo < 0:
                print ("(" + variable + " + " + format(multdiv) + ")(" + variable + " - " + format(-1*multdivTwo) + ")")
            if multdiv < 0 and multdivTwo > 0:
                print ("(" + variable + " - " + format(-1*multdiv) + ")(" + variable + " + " + format(multdivTwo) + ")")
            if multdiv > 0 and multdivTwo > 0:
                print ("(" + variable + " + " + format(multdiv) + ")(" + variable + " + " + format(multdivTwo) + ")")
        else:
            print ("It's probably prime lol")
        #</factoring>
    else:
        #=======SPLIT THE MIDDLE=======
        #Decide what the things should start as
        xFin = Ain * Cin

        if Bin < 0 and xFin < 0:
            multdiv = Bin + xFin
        if Bin < 0:
            multdiv = ((Bin) - xFin)
        if xFin < 0:
            multdiv = (-1*Bin) + xFin
        if Bin > 0 and xFin > 0:
            multdiv = Bin + xFin
        originMultDiv = multdiv#Fun fact, multdiv was a typo and I just kinda rolled with it out of laziness.
        if multdiv > 0:
             Anchor = multdiv#Anchor
        if multdiv < 0:
            Anchor = -1*multdiv
        multdivTwo = multdiv
        while (multdiv <= Anchor):
            #==========
            while (multdivTwo <= Anchor):
                if multdiv + multdivTwo == Bin and multdiv * multdivTwo == xFin:
                    break
                multdivTwo += 1;
            #</multdivTwo_count>
            #==========
            if multdiv + multdivTwo == Bin and multdiv * multdivTwo == xFin:
                break
            multdiv += 1;
            multdivTwo = originMultDiv
            #</multdiv_count>
        #Print Result
        print ("(" + format(Ain) + variable + "^2 + " + format(multdiv) + variable + ") | (" + format(multdivTwo) + variable + " + " + format(Cin) + ")")#This is about halfway through splitting the middle.
        xAI = Ain
        xAII = multdiv

        xBI = multdivTwo
        xBII = Cin

        runningOutOfVariableNames = gcd(xAI, xAII)
        yAI = xAI / runningOutOfVariableNames
        yAII = xAII / runningOutOfVariableNames
        runningOutOfVariableNamesTwo = gcd(xBI, xBII)
        yBI = xBI / runningOutOfVariableNamesTwo
        yBII = xBII / runningOutOfVariableNamesTwo

        print ("(" + format(-runningOutOfVariableNames) + variable + " + " + format(-runningOutOfVariableNamesTwo) + ")(" + format(-yAI) + variable + " + " + format(-yAII) + ")")#Done


def quadraticFormula():
    try:#stealing this code. Copyright © Will Nilges 2014-2017
        if (math.sqrt((b*b)-4*a*c)).is_integer():
            print ("Plus")
            print ("Square Root: " + format(math.sqrt((b*b)-4*a*c)))
            print ("")
            print (format(-b) + " + √" + format(b) + "^2 - 4(" + format(a) + ")(" + format(c) + ")" + "/2" + "(" + format(a) + ")")
            print (format(-b) + " + √" + format((b*b)-4*a*c) + ''')
––––––––––––
''' + format(a*2))
            print ("")
            print ("x = " + format(((-b)+math.sqrt((b*b)-4*a*c))/2*a))
            print ('''Minus
            ''')
            print ("Square Root: " + format(math.sqrt((b*b)-4*a*c)))
            print ("")
            print (format(-b) + " - √" + format(b) + "^2 - 4(" + format(a) + ")(" + format(c) + ")" + "/2" + "(" + format(a) + ")")
            print (format(-b) + " - √" + format((b*b)-4*a*c) + ''')
––––––––––––
''' + format(a*2))
            print ("")
            print ("x = " + format(((-b)-math.sqrt((b*b)-4*a*c))/2*a))
        else:
            print ("Square Root: " + format(math.sqrt((b*b)-4*a*c)))
            print ("")
            print (format(-b) + " ± √" + format(b) + "^2 - 4(" + format(a) + ")(" + format(c) + ")" + "/2" + "(" + format(a) + ")")
            print ("x = (" + format(-b) + " ± √" + format((b*b)-4*a*c) + ''')
––––––––––––
''' + format(a*2))
            print ("")
    except ValueError:
        print ('''NO REAL SOLUTION
        ''')
        print (format(-b) + " ± √" + format(b) + "^2 - 4(" + format(a) + ")(" + format(c) + ")" + ''')
––––––––––––
2''' + "(" + format(a) + ")")
        print ("x = (" + format(-b) + " ± i√" + format(-1*((b*b)-4*a*c)) + ''')
––––––––––––
''' + format(a*2))
        discriminant = -1*((b*b)-4*a*c)
        #Need a whole other logic tree here. Or maybe not. Maybe you just needed that if statement down there right after the while loop.
        i = 2
        while ((discriminant % i != 0) or i < 1000):
            i += 1
        if (discriminant % i == 0):
            imaginaryMultiplier = discriminant / i
            print ("x = " + format(-b) + " ± " + format(i) + "i√" + format(imaginaryMultiplier) + '''
––––––––––––
''' + format(a*2))
            #Quick, Rewrite it
            if math.sqrt(imaginaryMultiplier).is_integer():
                discriminantTimesIMultiplier = math.sqrt(imaginaryMultiplier)*i
                if discriminantTimesIMultiplier % (a*2) == 0:
                    if -b % (a*2) == 0:
                        print ("x = " + format(-b/(a*2)) + " ± " + format(discriminantTimesIMultiplier/(a*2)) + "i")
                    else:
                        print ("x = " + format(-b) + "/" + format(a*2) + " ± " + format(discriminantTimesIMultiplier/(a*2)) + "i")
                else:
                    if -b % (a*2) == 0:
                        print ("x = " + format(-b/(a*2)) + " ± " + format(discriminantTimesIMultiplier) + "/" + format(a*2) + "i")
                    else:
                        print ("x = " + format(-b) + "/" + format(a*2) + " ± √" + format(discriminantTimesIMultiplier) + "/" + format(a*2) + "i")
            else:
                if -b % (a*2) == 0:
                    print ("x = " + format(-b/(a*2)) + " ± ((√" + format(imaginaryMultiplier) + ")/" + format(a*2) + ")i")
                else:
                    print ("x = " + format(-b) + " ± " + format(i) +" "+ format(imaginaryMultiplier) + "i" + '''
––––––––––––
''' + format(a*2))

def quadrinomialFactoring():
    takeOut = gcd(a,b)
    new_a = a/gcd(a,b)
    new_b = b/gcd(a,b)
    if (aPwr >= bPwr):
        takeOutPwr = bPwr
        new_aPwr = aPwr-bPwr
        new_bPwr = 0
    if (bPwr >= aPwr):
        takeOutPwr = aPwr
        new_aPwr = 0
        new_bPwr = bPwr - aPwr

    takeOutTwo = gcd(c,d)
    new_c = c/gcd(c,d)
    new_d = d/gcd(c,d)
    if (cPwr >= dPwr):
        takeOutPwrTwo = dPwr
        new_cPwr = cPwr-dPwr
        new_dPwr = 0
    if (dPwr >= cPwr):
        takeOutPwrTwo = cPwr
        new_cPwr = 0
        new_dPwr = dPwr - cPwr

    clear()
    print (format(a) + variable + "^" + format(aPwr) + " + " + format(b) + variable + "^" + format(bPwr) + " + " + format(c) + variable + "^" + format(cPwr) + " + " + format(d) + variable + format(dPwr))
    print ('''
goes to
    ''')
    print ("(" + format(new_a) + variable + "^" + format(new_aPwr) + " + " + format(new_b) + variable + "^" + format(new_bPwr) +  ")(" + format(takeOut) + variable + "^" + format(takeOutPwr) + " + " + format(takeOutTwo) + variable + "^" + format(takeOutPwrTwo) +  ")")
    if (gcd(new_a,new_b).is_integer):
        print("Look out, you might be able to factor out an integer still. Said integer is " + format(gcd(new_a,new_b)) + " in the first equation")
    if (gcd(takeOut,takeOutTwo).is_integer):
        print("Look out, you might be able to factor out an integer still. Said integer is: " + format(gcd(takeOut,takeOutTwo)) + " in the second equation")
    if (takeOutPwr > 2 or takeOutPwrTwo > 2 or new_aPwr > 2 or new_bPwr > 2 or new_cPwr > 2 or new_dPwr > 2):
        print ("Watch out, this might still be factorable! A sum of squares can be factored, but a difference of squares cannot.")
    #To Do: Make this work
    # if (sqrt(new_a).is_integer or sqrt(new_b).is_integer and new_aPwr % 2 == 0 or new_bPwr % 2 == 0):
    #     if sqrt(new_a).is_integer:
    #         new_new_a = sqrt(new_a)
    #
    # if (sqrt(takeOut).is_integer or sqrt(takeOutTwo).is_integer and takeOutPwr % 2 == 0 or takeOutPwrTwo % 2 == 0):


while True:
    clear()
    print ('''
    Hard Math Simulator 2017

    Select an operation to get started.

    1 : LAW OF SINES

    2 : LAW OF COSINES

    3 : COORDINATE PLANE CALCULATIONS

    4 : SURFACE AREA

    5 : GRAPHED EQUATION CALCULATIONS

    6 : FACTORING

    |0 : Close|
    ''')
    Begin = input ("> ")
    if Begin == 1:
        clear()
        print ('''
    LAW OF SINES
    ––––––––––
    1 : Find Measure b

    2 : Find Angle B

    |0 : Back|
        ''')
        Start1 = input ("> ")
        if Start1 == 1:
            clear()
            # Enter values
            units = raw_input ("What units are you using? > ")
            A = input ("Please Enter (A): ")
            a = input ("Please Enter (a): ")
            B = input ("Please Enter (B): ")

            # Radians > Sine > Degrees
            radianA = math.radians(A)
            radianB = math.radians(B)
            processedA = math.sin(radianA)
            processedB = math.sin(radianB)
            moreprocessedA = math.degrees(processedA)
            moreprocessedB = math.degrees(processedB)

            # Ze operation
            equals = ((a * moreprocessedB) / moreprocessedA)
            print (equals)
            print (units)
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
            pass
        elif Start1 == 2:
            clear()
            #Not entirely sure if this all works. I think it does.
            units = raw_input ("What units are you using? > ")
            Atwo = input ("Please Enter (A): ")
            atwo = input ("Please Enter (a): ")
            btwo = input ("Please Enter (b): ")

            radianAtwo = math.radians(Atwo)
            processedAtwo = math.sin(radianAtwo)

            igualmente = ((btwo * processedAtwo) / atwo)
            equalstwo = (math.asin(igualmente))
            equalsyas = math.degrees(equalstwo)
            print (equalsyas)
            print (units)
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
    elif Begin == 2:
        clear()
        print ('''
    LAW OF COSINES
    ––––––––––
    1 : Find Measure c

    2 : Find Angle C

    |0 : Back|
        ''')
        Start = input ("> ")
        if Start == 1:
            clear()
            # Get the values from the user
            units = raw_input ("What units are you using? > ")
            bside = input ("Please Enter (a): ")
            cside = input ("Please Enter (b): ")
            Aangl = input ("Please Enter (C): ")

            #Convert angle to radians, cosine it, then put it back in degrees.
            Aanglrad = math.radians(Aangl)
            Aanglcos = math.cos(Aanglrad)
            Aanglnew = math.degrees(Aanglcos)

            finsim = ((bside * bside) + (cside + cside) - (2 * bside * cside) * Aanglcos)
            print (finsim)
            print (units)
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
        elif Start == 2:
            clear()
            alength = input ("Please enter (a): ")
            blength = input ("Please enter (b): ")
            clength = input ("Please enter (c): ")

            #1.0 is cheese
            cosAnswer = math.degrees(math.acos(1.0*((alength**2)+(blength**2)-(clength**2))/(2*(alength)*(blength))))
            print format(cosAnswer) + " degrees"
            #What the heck is even the point of any of this?
            # at = (alength * alength)
            # bt = (blength * blength)
            # ct = (clength * clength)
            #
            # ting = (bt + ct - at)
            # tingtwo = (2 * blength * clength)
            #
            # amazingmath = (math.acos(ting / tingtwo))
            # mathzz = math.degrees(amazingmath)
            # print (mathzz)
            # print (units)
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
    elif Begin == 3:
        clear()
        print ('''
    COORDINATE PLANE
    ––––––––––
    1 : Find distance on a coordinate plane

    2 : Find line formats from points and slope

    |0 : Back|
        ''')
        Start = input ("> ")
        if Start == 1:
            clear()
            units = raw_input ("What units are you using? > ")
            Axdist = input ("Please enter (x1): ")
            Aydist = input ("Please enter (y1): ")
            Bxdist = input ("Please enter (x2): ")
            Bydist = input ("Please enter (y2): ")

            xdistdone = (Bxdist - Axdist) * (Bxdist - Axdist)
            ydistdone = (Bydist - Aydist) * (Bydist - Aydist)

            done = (xdistdone + ydistdone)
            doner = math.sqrt(done)
            print ()
            print (doner)
            print (units)
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
        elif Start == 2:
            x  = input ("Please enter x (_,y): ")
            y = input ("Please enter y (" + format(x) + ",_): ")
            slopeRise = input ("Please enter the rise of the slope (__/run): ")
            slopeRun = input ("Please enter the run of the slope (" + format(slopeRise) + ",__): ")
            stringSlope = (format(slopeRise) + "/" + format(slopeRun))
            numericalSlope = float(slopeRise)/float(slopeRun)
            # Ugh CALCULATIONS
            print (numericalSlope)
            if x > 0:
                pointSlope = "y - " + format(y) + " = " + format(stringSlope) + "(x - " + format(x) + ")"
                negX = -x
                slopeInterceptYIntercept = (numericalSlope * int(negX)) - int(y)
            else:
                pointSlope = "y - " + format(y) + " = " + format(stringSlope) + "(x + " + format(abs(x)) + ")"
                slopeInterceptYIntercept = (numericalSlope * int(abs(int(x)))) - int(y)
            print (slopeInterceptYIntercept)
            if slopeInterceptYIntercept >= 0:
                print ("yes")
                slopeIntercept = "y = " + format(stringSlope) + "x + " + format(slopeInterceptYIntercept)
            else:
                print ("no")
                slopeIntercept = "y = " + format(stringSlope) + "x - " + format(abs(slopeInterceptYIntercept))
            print (pointSlope)
            print (slopeIntercept)
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)

    elif Begin == 4:
        clear()
        print ('''
    SURFACE AREA
    ––––––––––
    1 : Lateral Area/Surface Area of a Prism

    2 : Lateral Area/Surface Area of a Cylinder

    3 : Lateral Area/Surface Area of a Pyramid

    |0 : Back|
        ''')
    #
    # 4 : **UNDER CONSTRUCTION**
    #
    # 5 : Lateral Area/Surface Area of a Cone
        Start = input ("> ")
        if Start == 1:
            units = raw_input ("What units are you using? > ")
            base = input ("Please enter (b) > ")
            width = input ("Please enter (w) > ")
            height = input ("Please enter (h) > ")

            perimeter = ((2 * base) + (2 * width))
            Base = (base * width)

            lateralArea = (perimeter * height)
            surfaceArea = (lateralArea + (2 * Base))
            #LateralAreaFlag
            print ("Lateral Area is")
            print (lateralArea)
            print (units)
            print
            print ("Surface Area is")
            print (surfaceArea)
            print (units)
            fin = input ('''
        1 - Return to Main Menu
        2 - Close
        > ''')
            if fin == 1:
                clear()
                continue
            else:
                exit(0)
        elif Start == 2:
            clear()
            units = raw_input ("What units are you using? > ")
            radius = input ("Please enter (r) > ")
            height = input ("Please enter (h) > ")

            Base = (math.pi * (radius * radius))
            circumference = (2 * math.pi * radius)

            lateralArea = (circumference * height)
            surfaceArea = (lateralArea + (2 * Base))
            print ("Lateral Area is")
            print (lateralArea)
            print (units)
            print
            print ("Surface Area is")
            print (surfaceArea)
            print (units)
            fin = input ('''
        1 - Return to Main Menu
        2 - Close
        > ''')
            if fin == 1:
                clear()
                continue
            else:
                exit(0)
        elif Start == 3:
            clear()
            print('''
    SA OF PYRAMID
    ––––––––––
    1 : For Height

    2 : For Slant Height
            ''')
            Startp5 = input ("> ")
            if Startp5 == 1:
                    clear()
                    units = raw_input ("What units are you using? > ")
                    baseSideLength = input ("Please enter (b) > ")
                    height = input ("Please enter (h) > ")

                    halfBaseSideLength = (.5 * baseSideLength)
                    halfBaseSideLengthSquared = (halfBaseSideLength * halfBaseSideLength)
                    baseSideLengthSquared = (baseSideLength * baseSideLength)
                    heightSquared = (height * height)

                    perimeter = (4 * baseSideLength)
                    slantHeight = (math.sqrt(halfBaseSideLengthSquared + heightSquared))
                    lateralArea = (.5 * perimeter * slantHeight)
                    surfaceArea = (lateralArea + baseSideLengthSquared)
                    print ("Lateral Area is")
                    print (lateralArea)
                    print (units)
                    print
                    print ("Surface Area is")
                    print (surfaceArea)
                    print (units)
                    fin = input ('''
        1 - Return to Main Menu
        2 - Close
        > ''')
                    if fin == 1:
                        clear()
                        continue
                    else:
                        exit(0)
            elif Startp5 == 2:
                clear()
                units = raw_input ("What units are you using? > ")
                baseSideLength = input ("Please enter (b) > ")
                slantHeight = input ("Please enter (l) > ")

                baseSideLengthSquared = (baseSideLength * baseSideLength)

                perimeter = (4 * baseSideLength)
                lateralArea = (.5 * perimeter * slantHeight)
                surfaceArea = (lateralArea + baseSideLengthSquared)
                print ("Lateral Area is")
                print (lateralArea)
                print (units)
                print
                print ("Surface Area is")
                print (surfaceArea)
                print (units)
                fin = input ('''
        1 - Return to Main Menu
        2 - Close
        > ''')
                if fin == 1:
                    clear()
                    continue
                else:
                    exit(0)
            elif Start == 0:
                clear()
                exit(0)
            else:
                print ("INVALID INPUT")
                time.sleep(1)
                continue
    elif Begin == 5:
        clear()
        print ('''
    GRAPHED EQUATION CALCULATIONS
    ––––––––––
    1 : Properties of a vertex form equation   - y = a (x - h)^2 + k

    2 : Properties of a standard form equation - y = ax^2 + bx + c

    3 : Properties of a vertex and point (UNDER CONSTRUCTION)

    4 : Find standard form function with 3 points - y = ax^2 + bx + c

    |0 : Back|
        ''')
        Start = input ("> ")
        if Start == 1:
            print ("Enter a")
            a = input("y = _ (x - h)^2 + k > ")
            print ("Enter h")
            h = input("y = " + format(a) + " (x - _)^2 + k > ")
            print ("Enter k")
            k = input("y = " + format(a) + " (x - " + format(h) + ")^2 + _ > ")
            #Now do the hard part
            equation = "y = " + format(a) + " (x - " + format(h) + ")^2 + " + format(k)
            vertex = "(" + format(h) + "," + format(k) + ")"
            AoS = "x = " + format(h)
            if a < 0:
                minnerMax = "Min = " + format(k)
                rangeOfY = "(-infinity, " + format(k) + ")"
            else:
                minnerMax = "Max = " + format(k)
                rangeOfY = "(" + format(k) + ", infinity)"
            rangeOfX = "(-infinity, infinity)"
            print ('''
    Results:
            ''')
            print (equation)
            print (vertex)
            print (AoS)
            print (minnerMax)
            print (rangeOfX)
            print (rangeOfY)
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
        elif Start == 2:
            a = input("_x^2 + bx + c > ")
            b = input(format(a) + "x^2 + _x + c > ")
            c = input(format(a) + "x^2 + " + format(b) + "x + _ > ")
            clear()
            x = (-b)/(2*a)
            y = (a*(x*x)) + (b*x) + c
            vertexFormat = "y = " + format(a) + "(x - " + format(x) + ")^2 + " + format(y)
            vertex = "(" + format(x) + "," + format(y) + ")"
            h = x
            k = y
            AoS = "x = " + format(h)
            if a < 0:
                minnerMax = "Min = " + format(k)
                rangeOfY = "(-infinity, " + format(k) + ")"
            else:
                minnerMax = "Max = " + format(k)
                rangeOfY = "(" + format(k) + ", infinity)"
            rangeOfX = "(-infinity, infinity)"
            xWork = "x = -(b/2a) = -(" + format(b) + "/2" + format(a) + ") = " + format(-(b/(2*a)))
            yWork = format(y) + " = + " + format(a) + "(" + format(x) + "^2) + " + format(b) + "(" + format(x) + ")" + format(c)
            print ('''
    Work:
            ''')
            print (xWork)
            print (yWork)
            print ('''
    Results:
            ''')
            print (vertex)
            print (vertexFormat)
            print (AoS)
            print (minnerMax)
            print (rangeOfX)
            print (rangeOfY)
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
        elif Start == 3:
            print ("Under Construction")#Christ I have to finish this. I have to finish all of it lol.
            print ("Enter Vertex")
            x = input("(_, y)")
            y = input("("+ x + ", _)")
            vertex = "("+ x + ", " + y + ")"
            print ("Enter point")
            xPoint = input("(_, y)")
            yPoint = input("("+ x + ", _)")
            point = "("+ x + ", " + y + ")"
        elif Start == 4:
            #You fuckers better be grateful for this shit because it's hard as fuck. I'm smarter than Bill Fucking Gates.
            print ("REMEMBER! ENTER POINTS IN DECENDING Y VALUE!")
            print ("Enter Point One")
            xOn = input("(_, y) > ")
            yOn = input("("+ format(xOn) + ", _) > ")
            xOne = float(xOn)
            yOne = float(yOn)
            vertexOne = "("+ format(xOn) + ", " + format(yOn) + ")"
            equationA = format(yOn) + " = " + format(xOne*xOne) + "a + " + format(xOn) + "b + c"
            eaXSquared = xOne*xOne
            print ("Enter Point Two")
            xTw = input("(_, y) > ")
            yTw = input("("+ format(xTw) + ", _) > ")
            xTwo = float(xTw)
            yTwo = float(yTw)
            vertexTwo = "("+ format(xTw) + ", " + format(yTw) + ")"
            equationB = format(yTw) + " = " + format(xTwo*xTwo) + "a + " + format(xTw) + "b + c"
            print ("Enter Point Three")
            xTh = input("(_, y) > ")
            yTh = input("("+ format(xTh) + ", _) > ")
            xThree = float(xTh)
            yThree = float(yTh)
            vertexThree = "("+ format(xTh) + ", " + format(yTh) + ")"
            equationC = format(yTh) + " = " + format(xThree*xThree) + "a + " + format(xTh) + "b + c"
            #Done with input, now yuo chalclimilate
            equationD = format(yOn-yTw) + " = " + format((xOne*xOne)-(xTwo*xTwo)) + "a + " + format(xOn-xTw) + "b"
            xD = xOne-xTwo
            xDSquared = (xOne*xOne)-(xTwo*xTwo)
            yD = yOne-yTwo

            equationE = format(yOn-yTh) + " = " + format((xOne*xOne)-(xThree*xThree)) + "a + " + format(xOn-xTh) + "b"
            xE = xOne-xThree
            xESquared = (xOne*xOne)-(xThree*xThree)
            yE = yOne-yThree

            xF = (xD*xE)-(xE*xD)
            xFSquared = (xDSquared*xE)-(xESquared*xD)
            yF = (yD*xE)-(yE*xD)
            equationF = format(yF) + " = " + format(xFSquared) + "a"

            if xF < 0 and yF >= 0:
                a = -(yF/xF)
            else:
                print (yF)#Debug
                print (xFSquared)#Debug
                a = yF/xFSquared
            #Remember, it's equation E
            b = (yE-(xESquared*a))/xE
            c = yOne - ((eaXSquared*a) + (xOne*b))
            #Kazoo 'The Final Countdown'
            finalEquation = "y = " + format(a) + "x^2 + " + format(b) + "x + " + format(c)

            clear()
            print ('''
    Work:
            ''')
            print ("points")
            print (vertexOne)
            print (vertexTwo)
            print (vertexThree)

            print ("")

            print ("Equations from points")
            print (equationA + " Equation A")
            print (equationB + " Equation B")
            print (equationC + " Equation C")

            print ("")

            print ("Equation F was obtained by multiplying equation D by the b amount of E and equation E by the b amount of D and then subtracting E from D.")
            print (equationD + "  is Equation D (Obtained from Equation A minus Equation B)")
            print (equationE + " is Equation E (Obtained from Equation A minus Equation C)")

            print ("")

            print (equationD + "(Equation D) Times " + format(xE))
            print ("makes")
            print (format(xE*(yOn-yTw)) + " = " + format(xE*((xOne*xOne)-(xTwo*xTwo))) + "a + " + format(xE*(xOn-xTw)) + "b <NEW>")
            print ("and")
            print (equationE + "(Equation E) Times " + format(xD))
            print ("makes")
            print (format(xD*(yOn-yTh)) + " = " + format(xD*((xOne*xOne)-(xThree*xThree))) + "a + " + format(xD*((xOn-xTh))) + "b <NEW>")
            print ("Subtracting those new equations equals equation F")
            print (equationF)
            print ("a = " + format(yF) + "/" + format(xFSquared))
            print ("a = " + format(a))

            print ("")
            print ("b is found by plugging the A value back into equation E (after canceling c) like so: b = (y-(x^2*a))/x")
            print (format(yE) + "=" + format(xESquared) + "*" + format(a) + " + " + format(xE) + "b")
            print (format(yE-(xESquared*a)) + "=" + format(xE) + "b")
            print ("so b = (" + format(yE) + "-(" + format(xESquared) + "*" + format(a) + "))/" + format(xE))
            print ("b = " + format(b))
            print ("")
            print ("(This next bit is how to find C which is sometimes given in the first 3 equations but here's how to solve for it.)")
            print ("Solve for C by plugging into Equation A.")
            print ("c = " + format(yOne) + " - ((" + format(eaXSquared) + "*" + format(a) + ") + (" + format(xOne) + "*" + format(b) + "))")
            print (format(yOne) + "=" + format(eaXSquared)+ "*" + format(a) + "+" + format(xOne) + "*" + format(b) + " + c")
            print (format(yOne) + "=" + format((eaXSquared*a)+(xOne*b)) + "+ c")
            print ("c = " + format(yOne) + "/" + format((eaXSquared*a)+(xOne*b)))
            print ("c = " + format(c))
            #Christ on a chimney. You loosers better worship me.
            print ("")

            print ("a, b, c values")
            print (a)
            print (b)
            print (c)
            print ('''
    Result:
            ''')
            print (finalEquation)

            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
    elif Begin == 6:
        clear()
        print('''
    FACTORING
    ––––––––––
    1 : Binomial Factoring

    2 : Trinomial Factoring

    3 : Quadrinomial Factoring

    4 : Quadratic Formula Solver #UNDER CONSTRUCTION

    5 : Quadrinomial Equation Solver #UNDER CONSTRUCTION

    6 : Cubic Binomial Factoring #UNDER CONSTRUCTION

    7 : Cubic Binomial Equaiton Solver #UNDER CONSTRUCTION

    |0 : Back|
        ''')
        Start = input ("> ")
        if Start == 1:
            clear()
            letter = raw_input("What letter is your variable?> ")
            #To Do: Make this work at some point.
            # isTwoX = input("Is there an x on the 2nd monomial? (y/n) >")
            # if (isTwoX == "y"):
            # else:
            a = input("___x^2 + b > ")
            b = input(format(a) + "x^2 + ___ > ")
            if b < 0:
                b = -b
                if a != 0:
                    out = gcd(a,b)
                    afuckyou = a/gcd(a,b)
                    bfuckyou = b/gcd(a,b)
                    a = afuckyou
                    b = bfuckyou
                    print (format(out) + "(x + " + format(math.sqrt(b)) + ")(x - " + format(math.sqrt(b)) + ")")
                else:
                    print ("(x + " + format(math.sqrt(b)) + ")(x - " + format(math.sqrt(b)) + ")")
            else:
                print ("Can't factor sum of squares.")
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            else:
                exit(0)
        elif Start == 2:
            #Quick, rewrite it
            variable = raw_input("What letter is your variable? > ")
            Ain = input("_" + variable + "^2 + B" + variable + " + C > ")
            Bin = input(format(Ain) + variable + "^2 + _" + variable + " + C > ")
            Cin = input(format(Ain) + variable + "^2 + " + format(Bin) + variable + " + _ > ")
            a = Ain
            b = Bin
            c = Cin
            clear()
            print ("calculating...")
            print ("")
            trinomialFactoring()
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            elif fin == 2:
                exit(0)
            else:
                print ("INVALID INPUT")
                time.sleep(1)
                continue
        elif Start == 3:
            clear()
            variable = raw_input("What variable are you using? > ")
            a = input("___" + variable + "^aPwr + b" + variable + "^bPwr + c" + variable + "^cPwr + d" + variable + "^dPwr > ")
            clear()
            aPwr = input(format(a) + variable + "^___ + b" + variable + "^bPwr + c" + variable + "^cPwr + d" + variable + "^dPwr > ")
            clear()
            b = input(format(a) + variable + "^" + format(aPwr) + " + ___" + variable + "^bPwr + c" + variable + "^cPwr + d" + variable + "^dPwr > ")
            clear()
            bPwr = input(format(a) + variable + "^" + format(aPwr) + " + " + format(b) + variable + "^___ + c" + variable + "^cPwr + d" + variable + "^dPwr > ")
            clear()
            c = input(format(a) + variable + "^" + format(aPwr) + " + " + format(b) + variable + "^" + format(bPwr) + " + ___" + variable + "^cPwr + d" + variable + "^dPwr > ")
            clear()
            cPwr = input(format(a) + variable + "^" + format(aPwr) + " + " + format(b) + variable + "^" + format(bPwr) + " + " + format(c) + variable + "^___ + d" + variable + "^dPwr > ")
            clear()
            d = input(format(a) + variable + "^" + format(aPwr) + " + " + format(b) + variable + "^" + format(bPwr) + " + " + format(c) + variable + "^" + format(cPwr) + " + ___" + variable + "^dPwr > ")
            clear()
            dPwr = input(format(a) + variable + "^" + format(aPwr) + " + " + format(b) + variable + "^" + format(bPwr) + " + " + format(c) + variable + "^" + format(cPwr) + " + " + format(d) + variable + "^___ > ")
            clear()
            # A E S T H E T I C

            takeOut = gcd(a,b)
            new_a = a/gcd(a,b)
            new_b = b/gcd(a,b)
            if (aPwr >= bPwr):
                takeOutPwr = bPwr
                new_aPwr = aPwr-bPwr
                new_bPwr = 0
            if (bPwr >= aPwr):
                takeOutPwr = aPwr
                new_aPwr = 0
                new_bPwr = bPwr - aPwr

            takeOutTwo = gcd(c,d)
            new_c = c/gcd(c,d)
            new_d = d/gcd(c,d)
            if (cPwr >= dPwr):
                takeOutPwrTwo = dPwr
                new_cPwr = cPwr-dPwr
                new_dPwr = 0
            if (dPwr >= cPwr):
                takeOutPwrTwo = cPwr
                new_cPwr = 0
                new_dPwr = dPwr - cPwr

            clear()
            print (format(a) + variable + "^" + format(aPwr) + " + " + format(b) + variable + "^" + format(bPwr) + " + " + format(c) + variable + "^" + format(cPwr) + " + " + format(d) + variable + format(dPwr))
            print ('''
goes to
            ''')
            print ("(" + format(new_a) + variable + "^" + format(new_aPwr) + " + " + format(new_b) + variable + "^" + format(new_bPwr) +  ")(" + format(takeOut) + variable + "^" + format(takeOutPwr) + " + " + format(takeOutTwo) + variable + "^" + format(takeOutPwrTwo) +  ")")
            # if (gcd(new_a,new_b).is_integer):
            #     if (gcd(takeOut,takeOutTwo).is_integer):
            #         print(format(gcd(new_a,new_b)) + "(" + format(new_a/gcd(new_a,new_b)) + variable + "^" + format(new_aPwr) + " + " + format(new_b/gcd(new_a,new_b)) + variable + "^" + format(new_bPwr) +  ")(" + format(takeOut/gcd(takeOut,takeOutTwo)) + variable + "^" + format(takeOutPwr) + " + " + format(takeOutTwo/gcd(takeOut,takeOutTwo)) + variable + "^" + format(takeOutPwrTwo) +  ")")
            #     else:
            #         print (format(gcd(new_a,new_b)) + "(" + format(new_a/gcd(new_a,new_b)) + variable + "^" + format(new_aPwr) + " + " + format(new_b/gcd(new_a,new_b)) + variable + "^" + format(new_bPwr) +  ")(" + format(takeOut) + variable + "^" + format(takeOutPwr) + " + " + format(takeOutTwo) + variable + "^" + format(takeOutPwrTwo) +  ")")
            # elif (gcd(takeOut,takeOutTwo).is_integer):
            #     if (gcd(new_a,new_b).is_integer):
            #         print(format(gcd(new_a,new_b)) + "(" + format(new_a/gcd(new_a,new_b)) + variable + "^" + format(new_aPwr) + " + " + format(new_b/gcd(new_a,new_b)) + variable + "^" + format(new_bPwr) +  ")(" + format(takeOut/gcd(takeOut,takeOutTwo)) + variable + "^" + format(takeOutPwr) + " + " + format(takeOutTwo/gcd(takeOut,takeOutTwo)) + variable + "^" + format(takeOutPwrTwo) +  ")")
            #     else:
            #         print (format(gcd(takeOut,takeOutTwo)) + "(" + format(new_a) + variable + "^" + format(new_aPwr) + " + " + format(new_b) + variable + "^" + format(new_bPwr) +  ")(" + format(takeOut/gcd(takeOut,takeOutTwo)) + variable + "^" + format(takeOutPwr) + " + " + format(takeOutTwo/gcd(takeOut,takeOutTwo)) + variable + "^" + format(takeOutPwrTwo) +  ")")
            # else:
            #     print ("(" + format(new_a) + variable + "^" + format(new_aPwr) + " + " + format(new_b) + variable + "^" + format(new_bPwr) +  ")(" + format(takeOut) + variable + "^" + format(takeOutPwr) + " + " + format(takeOutTwo) + variable + "^" + format(takeOutPwrTwo) +  ")")
            if (takeOutPwr > 2 or takeOutPwrTwo > 2 or new_aPwr > 2 or new_bPwr > 2 or new_cPwr > 2 or new_dPwr > 2):
                print ("Watch out, this might still be factorable! A sum of squares can be factored, but a difference of squares cannot.")
            #It's a good start. It'll do for now. To Do: Write a loop that keeps on factoring.
                #print ("BUT WAIT, THERE'S MORE!")
            # if math.sqrt(new_aPwr).is_integer > 1 and math.sqrt(new_bPwr).is_integer > 1  and math.sqrt(new_a).is_integer and math.sqrt(-new_b).is_integer and new_b < 0:
            #     print ("(" + format(math.sqrt(new_a)) + variable + "^" + format(math.sqrt(new_aPwr))) + " + " + format(math.sqrt(new_b)) + variable + "^" + format(math.sqrt(new_bPwr))) + ")(" + format(math.sqrt(new_a)) + variable + "^" + format(math.sqrt(new_aPwr))) + " - " + format(math.sqrt(new_b)) + variable + "^" + format(math.sqrt(new_bPwr))) + ")"
            # if math.sqrt(takeOutPwr).is_integer > 1 and math.sqrt(takeOutPwrTwo).is_integer > 1 and takeOutTwo < 0:
            fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if fin == 1:
                continue
            elif fin == 2:
                exit(0)
            else:
                print ("INVALID INPUT")
                time.sleep(1)
                continue
        elif Start == 4:
            a = input("Enter a: ")
            b = input("Enter b: ")
            c = input("Enter c: ")
            quadraticFormula()
        elif Start == 5:
            print ("UNDER CONSTRUCTION")
            clear()
            var = raw_input("Enter your variable: ")
            clear()
            a = input("___" + var + "^3 + b > ")
            clear()
            b = input(format(a) + var + "^3 + ___ > ")
            clear()

        elif Start == 6:
            print ("UNDER CONSTRUCTION")
        elif Start == 7:
            print ("UNDER CONSTRUCTION")
    elif Begin == 0:
        exit(0)
    else:
        print ("INVALID INPUT")
        time.sleep(1)
        continue
