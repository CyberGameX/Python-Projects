import os
import math
import pyfiglet
from fractions import Fraction

# Alpha Version
# Grundrechenarten
def addition(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

#Winkel funktionen
def pytharogas(a, b):
    sumx = pow(a, 2) + pow(b, 2)
    summ = math.sqrt(sumx)
    return summ

def sinus(a, b):
    sumx = a / b
    summ = math.asin(sumx)
    return math.degrees(summ)

def cosinussite(a, b):
    c = a / math.cos(math.radians(b))
    return c

def cosinusangle(a, b):
    sumx = a / b
    summ = math.acos(sumx)
    return math.degrees(summ)

def tangens(tan_value, opposite):
    return opposite / math.tan(math.radians(tan_value)) # Rechnung ist falsch

#Physik
def speed(a, b):
    sumx = b / 60
    return a / sumx

def route(a, b):
    return b * a

def acceleration(a, b):
    return a * b

def mechanicnewton(a, b):
    return a * b

# Flaechenberechnung
def rectangle(a, b):
    return a * b

def circle(a):
    return pow(a, 2) * math.pi

def trianglesurface(a, b):
    sumx = a * b
    return sumx / 2

def trapezium(a, b, c):
    sumx = a + b
    summ = sumx * c
    return summ / 2 

#Volumen berechnung
def cubevol(a, b, c):
    return a * b * c

def rectanglevolume(a, b, c):
    return a * b * c

def pyramidvol(a, b):
    sumx = pow(a,2)
    summ = sumx * b
    return summ / 3

def sphere(a):
    sumx = Fraction(4, 3) * math.pi #Fraction ist die Bruchfunktion erst zaehler dann kommt der nenner
    summ = sumx * pow(a, 3)
    return summ 

#Intregralrechnung 
def integrate(): # Fehlt ############
    pass

# Prozent
def percentage(a, b):
    summ = a / b 
    return summ * 100

def basicamount(a, b):
    summ = a / b 
    return summ * 100

def percentagevalue(a, b):
    sumx = a * b
    return sumx / 100

# Potenzen u Wurzel ziehen 
def potency(a, b):
    return math.pow(a, b)
 # Wurzel ziehen 
def pullroot_2(a):
    return math.sqrt(a)

def pullroot_3(a):
    return math.pow(a, 1/3)

#Wurzelrechnen2
def rootaddition(a, b):
    sumx = math.sqrt(a)
    summ = sumx + b
    return summ 

def rootsubtraction(a, b):
    sumx = math.sqrt(a)
    summ = sumx - b
    return summ

def rootmultiplication(a, b):
    sumx = math.sqrt(a)
    summ = sumx * b
    return summ

def rootdivision(a, b):
    sumx = math.sqrt(a)
    summ = sumx / b
    return summ

#App
def taschenrechner():
    banner = pyfiglet.figlet_format("Calculator")
    print(banner)
    while True:
        try:
            print("Notice when you use a comma you will need to use a point .")
            print("Notice all results are rounded to two decimal figures")
            print()
            print("Basic math")
            print("Options:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Advanced math")
            print("6. Physics")
            print("7. Potency and pull root")
            print("8. Credits")
            print("9. Exit")

            option = int(input("Choose a option: "))
            os.system("cls")

            if option == 1:
                banner = pyfiglet.figlet_format("Addition")
                print(banner)
                zahl1 = float(input("Put a number: "))
                zahl2 = float(input("Put a number: "))
                ergebnis = addition(zahl1, zahl2)
                print(f"The result from {zahl1} + {zahl2} = {ergebnis}")
            elif option == 2:
                banner = pyfiglet.figlet_format("Subtraction")
                print(banner)
                zahl1 = float(input("Put a number: "))
                zahl2 = float(input("Put a number: "))
                ergebnis = subtraktion(zahl1, zahl2)
                print(f"The result from {zahl1} - {zahl2} = {ergebnis}")
            elif option == 3:
                banner = pyfiglet.figlet_format("Multiplication")
                print(banner)
                zahl1 = float(input("Put a number: "))
                zahl2 = float(input("Put a number: "))
                ergebnis = multiplication(zahl1, zahl2)
                print(f"The result from {zahl1} * {zahl2} = {ergebnis}")
            elif option == 4:
                banner = pyfiglet.figlet_format("Division")
                print(banner)
                zahl1 = float(input("Put a number: "))
                zahl2 = float(input("Put a number: "))
                try:
                    ergebnis = division(zahl1 ,zahl2)
                except ZeroDivisionError:
                    print("Cannot divide by zero!")
                else:
                    print(f"The result from {zahl1} : {zahl2} = {ergebnis}")
            elif option == 5:
                # Erweiterte Mathematik
                banner = pyfiglet.figlet_format("Advanced Math")
                print(banner)
                while True:
                    print("Options:")
                    print("1. Pytharogas")
                    print("2. Angular functions")
                    print("3. Surface calc")
                    print("4. Volume calc")
                    print("5. Intregral calc")
                    print("6. Percent")
                    print("7. Advance math exit")

                    option = int(input("Choose a option: "))
                    os.system("cls")

                    if option == 1:
                        banner = pyfiglet.figlet_format("Pytharogas")
                        print(banner)
                        zahl1 = float(input("Put a number: "))
                        zahl2 = float(input("Put a number: "))
                        ergebnis = pytharogas(zahl1, zahl2)
                        print(f"The hypotenuse is {round(ergebnis, 2)}")
                    elif option == 2:
                        #Winkelfunktionen
                        banner = pyfiglet.figlet_format("Angular Functions")
                        print(banner)
                        while True:
                            print("Pay attention the triangle angle must be 90 degrees!")
                            print("Options")
                            print("1. Sinus α [angle]")
                            print("2. Cosinus")
                            print("3. Tangens")
                            print("4. Adavanced math")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                #Sinus
                                banner = pyfiglet.figlet_format("Sinus")
                                print(banner)
                                zahl1 = float(input("Put opposide side of the angle: "))
                                zahl2 = float(input("Put hypotenuse: "))
                                ergebnis = sinus(zahl1, zahl2)
                                print(f"The result is: {round(ergebnis, 2)} degrees")
                            elif option == 2:
                                #Cosinus
                                banner = pyfiglet.figlet_format("Cosinus")
                                print(banner)
                                while True:
                                    print("Choose a option")
                                    print("1. Missing site [hypotenuse]")
                                    print("2. Missing α [angle]")
                                    print("3. Exit cosinus")

                                    option = int(input("Choose a option: "))
                                    os.system("cls")

                                    if option == 1:
                                        print("Missing Site Cos")
                                        zahl1 = float(input("Put the site from the angle: "))
                                        degr = float(input("Put the angle: "))
                                        ergebnis = cosinussite(zahl1, degr)
                                        print(f"Cosinus({degr}) hypotenuse is: {round(ergebnis, 2)} long")
                                    elif option == 2:
                                        print("Missing angle Cos")
                                        zahl1 = float(input("Put the site from the angle: "))
                                        zahl2 = float(input("Put hypotenuse: "))
                                        ergebnis = cosinusangle(zahl1, zahl2)
                                        print(f"Cosinus is: {round(ergebnis, 2)} degrees")
                                    elif option == 3:
                                        print("Exit cosinus.")
                                        break
                                    else:
                                        print("Invalid option!")
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Tangens")
                                print(banner)
                                zahl1 = float(input("Put the ajacent: "))
                                zahl2 = float(input("Put the angel: "))
                                ergebnis = tangens(zahl2, zahl1)
                                print(f"Tangens is: {round(ergebnis, 2)} long")
                            elif option == 4:
                                print("Angular function exit")
                                break
                            else:
                                print("Invalid option!")
                    elif option == 3:
                        while True:
                            # Flaechenberechnung
                            banner = pyfiglet.figlet_format("Surfache Calc")
                            print(banner)
                            print("Options")
                            print("1. Rectangle")
                            print("2. Circle")
                            print("3. Trianlge")
                            print("4. Trapezium")
                            print("5. Surface exit")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                banner = pyfiglet.figlet_format("Rectangle")
                                print(banner)
                                zahl1 = float(input(f"Put the site a: "))
                                zahl2 = float(input(f"Put the site b: "))
                                ergebnis = rectangle(zahl1, zahl2)
                                print(f"The rectangle is {round(ergebnis, 2)} large")
                            elif option == 2:
                                banner = pyfiglet.figlet_format("Circle")
                                print(banner)
                                zahl1 = float(input("Put the raidius: "))
                                ergebnis = circle(zahl1)
                                print(f"The circle surface is {round(ergebnis, 2)} large")
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Triangle")
                                print(banner)
                                zahl1 = float(input("Put the baseline: "))
                                zahl2 = float(input("Put the height: "))
                                ergebnis = trianglesurface(zahl1, zahl2)
                                print(f"The triangle is {round(ergebnis, 2)} large")
                            elif option == 4:
                                banner = pyfiglet.figlet_format("Trapezium")
                                print(banner)
                                print("This only works with the site a and c and the height!")
                                zahl1 = float(input("Put the site a: "))
                                zahl2 = float(input("Put the site c: "))
                                zahl3 = float(input("Put the height: "))
                                ergebnis = trapezium(zahl1, zahl2, zahl3)
                                print(f"The Trapezium is {round(ergebnis, 2)} large")

                            elif option == 5:
                                print("Surface calc exit")
                                break
                            else:
                                print("Invalid option")
                    elif option == 4:
                        banner = pyfiglet.figlet_format("Volume calc")
                        print(banner)
                        while True:
                            #Volumen berechnung
                            print("Options:")
                            print("1. Cube")
                            print("2. Rectangle")
                            print("3. Pyramid")
                            print("4. Sphere")
                            print("5. Volume calc exit")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                banner = pyfiglet.figlet_format("Cube")
                                print(banner)
                                zahl1 = float(input("Put the site a: "))
                                zahl2 = float(input("Put the site a: "))
                                zahl3 = float(input("Put the site a: "))
                                ergebnis = cubevol(zahl1, zahl2, zahl3)
                                print(f"{zahl1} * {zahl2} * {zahl3} = {round(ergebnis, 2)}")
                            elif option == 2:
                                banner = pyfiglet.figlet_format("Rectangle")
                                print(banner)
                                zahl1 = float(input("Put the site a: "))
                                zahl2 = float(input("Put the site b: "))
                                zahl3 = float(input("Put the site c: "))
                                ergebnis = rectanglevolume(zahl1, zahl2, zahl3)
                                print(f"{zahl1} * {zahl2} * {zahl3} = {round(ergebnis, 2)}")
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Pyramid")
                                print(banner)
                                zahl1 = float(input("Put the baseline a: "))
                                zahl2 = float(input("Put the height hk: "))
                                ergebnis = pyramidvol(zahl1, zahl2)
                                print(f"The volume from the pyramid is {round(ergebnis,2)}")
                            elif option == 4:
                                banner = pyfiglet.figlet_format("Spehere")
                                print(banner)
                                zahl1 = float(input("Put the radius: "))
                                ergebnis = sphere(zahl1)
                                print(f"The volume from the sphere is {round(ergebnis,2)}")
                            elif option == 5:
                                print("Volume calc exit")
                                break
                            else:
                                print("Invalid option!")
                    elif option == 5:
                        banner = pyfiglet.figlet_format("Intregral")
                        print(banner)
                        print("In progress")
                    elif option == 6:
                        while True:
                            #Prozent
                            banner = pyfiglet.figlet_format("Percent")
                            print(banner)
                            print("Options:")
                            print("1. Percentage") # Prozentsatz %
                            print("2. Basic amount") # Grundwert  G
                            print("3. Percentage value") # Prozentwert W
                            print("4. Percent exit")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                banner = pyfiglet.figlet_format("Percentage")
                                print(banner)
                                zahl1 = float(input("Put the percentage value: "))
                                zahl2 = float(input("Put the basic amount: "))
                                ergebnis = percentage(zahl1, zahl2)
                                print(f"The Percent age is {ergebnis}%")
                            elif option == 2:
                                banner = pyfiglet.figlet_format("Basic Amount")
                                print(banner)
                                zahl1 = float(input("Put the percentage value: "))
                                zahl2 = float(input("Put the percentage%: "))
                                ergebnis = basicamount(zahl1, zahl2)
                                print(f"The basic amount is {ergebnis}")
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Percentage value")
                                print(banner)
                                zahl1 = float(input("Put the basic amount: "))
                                zahl2 = float(input("Put the percentage%: "))
                                ergebnis = percentagevalue(zahl1, zahl2)
                                print(f"The percentage value is {ergebnis}")
                            elif option == 4:
                                print("Percent exit")
                                break
                            else:
                                print("Invalid option!")
                    elif option == 7:
                        print("Advanced math exit.")
                        break
                    else:
                        print("Invalid option!")
            elif option == 6:
                while True:
                    #Physik
                    banner = pyfiglet.figlet_format("Physics")
                    print(banner)
                    print("Options:")
                    print("1. Speed and Route calc")
                    print("2. Acceleration in m/s")
                    print("3. Mechanic Newton [N]")
                    print("4. Physics exit")

                    option = int(input("Choose a option: "))
                    os.system("cls")

                    if option == 1:
                        while True:
                            banner = pyfiglet.figlet_format("Speed and Route")
                            print(banner)
                            print("Options:")
                            print("1. Speed [km/h]")
                            print("2. Route [km]")
                            print("3. Speed exit")
                        
                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                banner = pyfiglet.figlet_format("Speed")
                                print(banner)
                                print(" The result is only in km/h")
                                zahl1 = float(input("Put the distance: "))
                                zahl2 = float(input("Put the time in minutes: "))
                                ergebnis = speed(zahl1, zahl2)
                                print(f"The vehicle is {round(ergebnis, 2)} km/h fast")
                            elif option == 2:
                                banner = pyfiglet.figlet_format("Route")
                                print(banner)
                                zahl1 = float(input("Put the time in ours: "))
                                zahl2 = float(input("Put the speed in km/h: "))
                                ergebnis = route(zahl1, zahl2)
                                print(f"The vehicle is {round(ergebnis, 2)} km driven far")
                            elif option == 3:
                                print("Speed and Route calc exit.")
                                break
                            else:
                                print("Invalid option!")
                    elif option == 2:
                        banner = pyfiglet.figlet_format("Acceleration")
                        print(banner)
                        print("The output is only in m/s")
                        zahl1 = float(input("Put the Acceleration only in m/s: "))
                        zahl2 = float(input("Put the time: "))
                        ergebnis = acceleration(zahl1, zahl2)
                        print(f"The acceleration is {ergebnis} m/s")
                    elif option == 3:
                        banner = pyfiglet.figlet_format("Mechanic Newton")
                        print(banner)
                        print("The acceleration must be in m/s and the weight in kg!")
                        zahl1 = float(input("Put the weight in kg: "))
                        zahl2 = float(input("Put the acceleration in m/s: "))
                        ergebnis = mechanicnewton(zahl1, zahl2)
                        print(f"The force is {ergebnis} N")
                    elif option == 4:
                        print("Physics exit.")
                        break
                    else:
                        print("Invalid option!")
            elif option == 7:
                while True:
                    #Potenzen u Wurzel ziehen 
                    banner = pyfiglet.figlet_format("Potency and pull root")
                    print(banner)
                    print("Options:")
                    print("1. Potency")
                    print("2. Pull root and calc with roots")
                    print("3. Potency and pull root exit")

                    option = int(input("Choose a option: "))
                    os.system("cls")

                    if option == 1:
                        banner = pyfiglet.figlet_format("Potency")
                        print(banner)
                        zahl1 = float(input("Put the number that you want to potency: "))
                        zahl2 = float(input("Put the exponent: "))
                        ergebnis = potency(zahl1, zahl2)
                        print(f"The Sum is {ergebnis}")
                    elif option == 2:
                        while True:
                            #Wurzel ziehen
                            banner = pyfiglet.figlet_format("Pull root and calc with roots")
                            print(banner)
                            print("Options:")
                            print("1. Calc with roots2(Basic Math)")
                            print("2. Pull square2 root and cube3 root")
                            print("3. Pullroot exit")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                while True:
                                    #Wurzeln rechnen
                                    banner = pyfiglet.figlet_format("Calc with roots2")
                                    print(banner)
                                    print("This works so example: the root x2 + number = result")
                                    print("Options")
                                    print("1. Addition")
                                    print("2. Subtraction")
                                    print("3. Multiplication")
                                    print("4. Division")
                                    print("5. Calc with roots2 exit")

                                    option = int(input("Choose a number: "))
                                    os.system("cls")

                                    if option == 1:
                                        banner = pyfiglet.figlet_format("Addition-root")
                                        print(banner)
                                        zahl1 = float(input("Put the radikant: "))
                                        zahl2 = float(input("Put a number: "))
                                        ergebnis = rootaddition(zahl1, zahl2)
                                        print(f"The result is {ergebnis}")
                                    elif option == 2:
                                        banner = pyfiglet.figlet_format("Subtrac-root")
                                        print(banner)
                                        zahl1 = float(input("Put the radikant: "))
                                        zahl2 = float(input("Put the number: "))
                                        ergebnis = rootsubtraction(zahl1, zahl2)
                                        print(f"The result is {ergebnis}")
                                    elif option == 3:
                                        banner = pyfiglet.figlet_format("Multipli-root")
                                        print(banner)
                                        zahl1 = float(input("Put the radikant: "))
                                        zahl2 = float(input("Put the the number: "))
                                        ergebnis = rootmultiplication(zahl1 ,zahl2)
                                        print(f"The result is {round(ergebnis, 2)}")
                                    elif option == 4:
                                        banner = pyfiglet.figlet_format("Division-root")
                                        print(banner)
                                        zahl1 = float(input("Put the radikant: "))
                                        zahl2 = float(input("Put the number: "))
                                        ergebnis = rootdivision(zahl1 ,zahl2)
                                        print(f"The sum is {round(ergebnis, 2)}")
                                    elif option == 5:
                                        print("Calc with roots2 exit.")
                                        break
                                    else:
                                        print("Invalid option!")
                            elif option == 2:
                                while True:
                                    #Wurzeln ziehen
                                    banner = pyfiglet.figlet_format("Pull square2 root and cube3 root")
                                    print(banner)
                                    print("Options:")
                                    print("1. Exponent 2")
                                    print("2. Exponent 3")
                                    print("3. Pull square2 root and cube3 root exit")


                                    option = int(input("Choose a option: "))
                                    os.system("cls")
                              
                                    if option == 1:
                                       zahl1 = float(input("Put the radikant: "))
                                       ergebnis = pullroot_2(zahl1)
                                       print(f"The root2 from {zahl1} is {round(ergebnis, 2)}")
                                    elif option == 2:
                                       zahl1 = float(input("Put the radikant: "))
                                       ergebnis = pullroot_3(zahl1)
                                       print(f"The root3 from {zahl1} is {round(ergebnis, 2)}")
                                    elif option == 3:
                                        print("Pull root exit.")
                                        break
                                    else:
                                        print("Invalid option!")
                            elif option == 3:
                                print("Pull root exit.")
                                break
                            else:
                                print("Invalid option!")
                    elif option == 3:
                        print("Potency and pull root exit.")
                        break
                    else:
                        print("Invalid option!")
            elif option == 8:
                while True:
                    banner = pyfiglet.figlet_format("Credits")
                    print(banner)
                    print("Options:")
                    print("1. Creator")
                    print("2. GitHub")
                    print("3. Credits exit")

                    option = int(input("Choose a option: "))
                    os.system("cls")

                    if option == 1:
                        banner = pyfiglet.figlet_format("Creator")
                        print(banner)
                        print("Yasin")
                    elif option == 2:
                        banner = pyfiglet.figlet_format("GitHub")
                        print(banner)
                        print("In progress")
                    elif option == 3:
                        print("Credits exit.")
                        break
                    else:
                        print("Invalid option!")
            elif option == 9:
                print("Programm exit.")
                break
            else:
                print("Invalid option!")
        except ValueError:
             print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    taschenrechner()
