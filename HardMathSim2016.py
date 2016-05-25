#!/usr/bin/env Python
# -*- coding: iso-8859-15 -*-
import math
import time
import os

while True:
    os.system("clear")
    print ('''
    Laws of Sine and (not quite yet) Cosine Simulator 2016 (and more!)

    Select an operation to get started.

    1 : LAW OF SINES

    2 : LAW OF COSINES

    3 : COORDINATE PLANE CALCULATIONS

    4 : SURFACE AREA

    |0 : Close|
    ''')
    Begin = input ("> ")
    if Begin == 1:
        print ('''
    LAW OF SINES
    ––––––––––
    1 : Find Measure b

    2 : Find Angle B

    |0 : Close|
        ''')
        Start1 = input ("> ")
        if Start1 == 1:
            # Enter values
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
            print equals

            Fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if Fin == 1:
                continue
            else:
                exit(0)
            pass
        elif Start1 == 2:
            #Not entirely sure if this all works. I think it does.
                Atwo = input ("Please Enter (A): ")
                atwo = input ("Please Enter (a): ")
                btwo = input ("Please Enter (b): ")

                radianAtwo = math.radians(Atwo)
                processedAtwo = math.sin(radianAtwo)

                igualmente = ((btwo * processedAtwo) / atwo)
                equalstwo = (math.asin(igualmente))
                equalsyas = math.degrees(equalstwo)
                print equalsyas
                Fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
                if Fin == 1:
                    continue
                else:
                    exit(0)
        elif Start1 == 0:
            exit(0)
        else:
            print ("INVALID INPUT")
            time.sleep(1)
            continue
    elif Begin == 2:
        Start2 = input ("> ")
        print ('''
    LAW OF COSINES
    ––––––––––
    1 : Find Measure a

    2 : Find Angle A (In development)

    |0 : Close|
        ''')
        if Start2 == 1:
            os.system("clear")
            # Get the values from the user
            bside = input ("Please Enter (b): ")
            cside = input ("Please Enter (c): ")
            Aangl = input ("Please Enter (A): ")

            #Convert angle to radians, cosine it, then put it back in degrees.
            Aanglrad = math.radians(Aangl)
            Aanglcos = math.cos(Aanglrad)
            Aanglnew = math.degrees(Aanglcos)

            finsim = ((bside * bside) + (cside + cside) - (2 * bside * cside) * Aanglcos)
            print finsim
            Fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if Fin == 1:
                continue
            else:
                exit(0)
        elif Start2 == 2:
            os.system("clear")
            alength = input ("Please enter (a): ")
            blength = input ("Please enter (b): ")
            clength = input ("Please enter (c): ")

            at = (alength * alength)
            bt = (blength * blength)
            ct = (clength * clength)

            ting = (bt + ct - at)
            tingtwo = (2 * blength * clength)

            amazingmath = (math.acos(ting / tingtwo))
            mathzz = math.degrees(amazingmath)
            print mathzz
            Fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if Fin == 1:
                continue
            else:
                exit(0)
        elif Start2 == 0:
            exit(0)
        else:
            print ("INVALID INPUT")
            time.sleep(1)
            continue
    elif Begin == 3:
        Start3 = input ("> ")
        print ('''
    COORDINATE PLANE
    ––––––––––
    1 : Find distance on a coordinate plane

    |0 : Close|
        ''')
        if Start3 == 1:
            os.system("clear")
            print ("Find distance on coordinate planes!")
            Axdist = input ("Please enter (x1): ")
            Aydist = input ("Please enter (y1): ")
            Bxdist = input ("Please enter (x2): ")
            Bydist = input ("Please enter (y2): ")

            xdistdone = (Bxdist - Axdist) * (Bxdist - Axdist)
            ydistdone = (Bydist - Aydist) * (Bydist - Aydist)

            done = (xdistdone + ydistdone)
            doner = math.sqrt(done)
            print
            print doner
            Fin = input ('''
    1 - Return to Main Menu
    2 - Close
    > ''')
            if Fin == 1:
                continue
            else:
                exit(0)
        elif Start3 == 0:
            exit(0)
        else:
            print ("INVALID INPUT")
            time.sleep(1)
            continue
    elif Begin == 4:
        print ('''
    SURFACE AREA
    ––––––––––
    1 : Lateral Area/Surface Area of a Prism

    2 : Lateral Area/Surface Area of a Cylinder

    3 : Lateral Area/Surface Area of a Pyramid (for height)

    4 : Lateral Area/Surface Area of a Pyramid (for slant height)

    |0 : Close|
        ''')
        Start4 = input ("> ")
        if Start4 == 1:
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
            print lateralArea
            print units
            print
            print ("Surface Area is")
            print surfaceArea
            print units
            Fin = input ('''
        1 - Return to Main Menu
        2 - Close
        > ''')
            if Fin == 1:
                os.system("clear")
                continue
            else:
                exit(0)
        elif Start4 == 2:
            units = raw_input ("What units are you using? > ")
            radius = input ("Please enter (r) > ")
            height = input ("Please enter (h) > ")

            Base = (math.pi * (radius * radius))
            circumference = (2 * math.pi * radius)

            lateralArea = (circumference * height)
            surfaceArea = (lateralArea + (2 * Base))
            print ("Lateral Area is")
            print lateralArea
            print units
            print
            print ("Surface Area is")
            print surfaceArea
            print units
            Fin = input ('''
        1 - Return to Main Menu
        2 - Close
        > ''')
            if Fin == 1:
                os.system("clear")
                continue
            else:
                exit(0)
        elif Start4 == 3:
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
            print lateralArea
            print units
            print
            print ("Surface Area is")
            print surfaceArea
            print units
            Fin = input ('''
        1 - Return to Main Menu
        2 - Close
        > ''')
            if Fin == 1:
                os.system("clear")
                continue
            else:
                exit(0)
        elif Start4 == 4:
            units = raw_input ("What units are you using? > ")
            baseSideLength = input ("Please enter (b) > ")
            slantHeight = input ("Please enter (l) > ")

            baseSideLengthSquared = (baseSideLength * baseSideLength)

            perimeter = (4 * baseSideLength)
            lateralArea = (.5 * perimeter * slantHeight)
            surfaceArea = (lateralArea + baseSideLengthSquared)
            print ("Lateral Area is")
            print lateralArea
            print units
            print
            print ("Surface Area is")
            print surfaceArea
            print units
            Fin = input ('''
        1 - Return to Main Menu
        2 - Close
        > ''')
            if Fin == 1:
                os.system("clear")
                continue
            else:
                exit(0)
        elif Start4 == 0:
            exit(0)
        else:
            print ("INVALID INPUT")
            time.sleep(1)
            continue
    elif Begin == 0:
        exit (0)
    else:
        print ("INVALID INPUT")
        time.sleep(1)
        continue
