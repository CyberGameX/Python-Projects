from fractions import Fraction
import os
import math
import webbrowser
import pyfiglet


# Pre-Alpha Version
# Grundrechenarten
def addition(a, b):
    return a + b


def subtraktion(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


# Winkel funktionen
def pytharogas(a, b):  # Berechnet die Hypotenuse
    sumx = pow(a, 2) + pow(b, 2)  # a² + b² ²√sumx
    summ = math.sqrt(sumx)
    return summ


def sinus(a, b):  # Alpha Winkel berechnen
    sumx = a / b
    summ = math.asin(sumx)
    return math.degrees(summ)


def cosinus_site(a, b):
    c = a / math.cos(math.radians(b))
    return c


def cosinus_angle(a, b):  # Alpha Winkel
    sumx = a / b
    summ = math.acos(sumx)
    return math.degrees(summ)


def tangens(tan_value, opposite):
    return opposite / math.tan(math.radians(tan_value))  # Rechnung ist falsch


# Physik
def speed(a, b):  # b / 60 = in Minuten  a / b/60
    sumx = b / 60
    return a / sumx


def route(a, b):  # in km
    return b * a


def acceleration(a, b):  # in m/s
    return a * b


def mechanic_newton(a, b):  # in [N]
    return a * b


# Flächenberechnung
def rectangle(a, b):  # a * b
    return a * b


def circle(a):  # π * r²
    return pow(a, 2) * math.pi


def triangle_surface(a, b):  # g * h / 2
    sumx = a * b
    return sumx / 2


def trapezium(a, b, c):  # 1/2 * (a + b) * c
    sumx = a + b
    summ = sumx * c
    return summ / 2


# Volumen berechnung
def cubevol(a, b, c):  # a * b * c
    return a * b * c


def rectangle_volume(a, b, c):  # a * b * c
    return a * b * c


def pyramid_volume(a, b):  # a2 * b / 3
    sumx = pow(a, 2)
    summ = sumx * b
    return summ / 3


def sphere(a):
    sumx = (
        Fraction(4, 3) * math.pi
    )  # Fraction ist, die Bruchfunktion erst zähler dann kommt der nenner
    summ = sumx * pow(a, 3)  # 4/3 * π * a³
    return summ


# Intregralrechnung
def integrate():  # Fehlt ############
    pass


# Prozent
def percentage(a, b):  # a/b * 100
    summ = a / b
    return summ * 100


def basic_amount(a, b):  # a/b * 100
    summ = a / b
    return summ * 100


def percentage_value(a, b):  # a * b /100
    sumx = a * b
    return sumx / 100


# Potenzen u Wurzel ziehen
def potency(a, b):  # x√x
    return math.pow(a, b)


# Wurzel ziehen
def pull_root_2(a):  # ²√a
    return math.sqrt(a)


def pull_root_3(a):  # a1 / 3
    return math.pow(a, 1 / 3)


# Wurzelrechnen2
def root_addition(a, b):  # ²√ + a
    sumx = math.sqrt(a)
    summ = sumx + b
    return summ


def root_subtraction(a, b):  # ²√a - b
    sumx = math.sqrt(a)
    summ = sumx - b
    return summ


def root_multiplication(a, b):  # ²√a * b
    sumx = math.sqrt(a)
    summ = sumx * b
    return summ


def root_division(a, b):  # ²√a / b
    sumx = math.sqrt(a)
    summ = sumx / b
    return summ


# Strom berechnung
def voltageri(a, b):
    return a * b


def voltage_ri(a, b):
    return a / b


def voltage_pr(a, b):
    summ = a * b
    return math.sqrt(summ)


# Stromleistung berechnung


def urwatt(a, b):
    summ = math.pow(a, 2)
    sumx = summ / b
    return sumx


def urwatti(a, b):
    return a / b


# Bruchberechnung
def braddit(a, b, c, d):
    summ = Fraction(a, b) + Fraction(c, d)
    return summ


def brsubtrac(a, b, c, d):
    summ = Fraction(a, b) - Fraction(c, d)
    return summ


def brmulti(a, b, c, d):
    summ = Fraction(a, b) * Fraction(c, d)
    return summ


def brdivi(a, b, c, d):
    summ = Fraction(a, b) / Fraction(c, d)
    return summ


# App
def main():
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
                    ergebnis = division(zahl1, zahl2)
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
                    print("1. Pythagoras")
                    print("2. Angular functions")
                    print("3. Surface calc")
                    print("4. Volume calc")
                    print("5. Integral calc")
                    print("6. Percent")
                    print("7. Fractional calculation")
                    print("8. Advance math exit")

                    option = int(input("Choose a option: "))
                    os.system("cls")

                    if option == 1:
                        banner = pyfiglet.figlet_format("Pythagoras")
                        print(banner)
                        zahl1 = float(input("Put a number: "))
                        zahl2 = float(input("Put a number: "))
                        ergebnis = pytharogas(zahl1, zahl2)
                        print(f"The hypotenuse is {round(ergebnis, 2)}")
                    elif option == 2:
                        # Winkelfunktionen
                        banner = pyfiglet.figlet_format("Angular Functions")
                        print(banner)
                        while True:
                            print(
                                "Pay attention the triangle angle must be 90 degrees!"
                            )
                            print("Options")
                            print("1. Sinus α [angle]")
                            print("2. Cosines")
                            print("3. Tangents")
                            print("4. Advanced math exit")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                # Sinus
                                banner = pyfiglet.figlet_format("Sinus")
                                print(banner)
                                zahl1 = float(input("Put opposite side of the angle: "))
                                zahl2 = float(input("Put hypotenuse: "))
                                ergebnis = sinus(zahl1, zahl2)
                                print(f"The result is: {round(ergebnis, 2)} degrees")
                            elif option == 2:
                                # Cosinus
                                banner = pyfiglet.figlet_format("Cosines")
                                print(banner)
                                while True:
                                    print("Choose a option")
                                    print("1. Missing site [hypotenuse]")
                                    print("2. Missing α [angle]")
                                    print("3. Exit cosines")

                                    option = int(input("Choose a option: "))
                                    os.system("cls")

                                    if option == 1:
                                        print("Missing Site Cos")
                                        zahl1 = float(
                                            input("Put the site from the angle: ")
                                        )
                                        degr = float(input("Put the angle: "))
                                        ergebnis = cosinus_site(zahl1, degr)
                                        print(
                                            f"Cosines({degr}) hypotenuse is: {round(ergebnis, 2)} long"
                                        )
                                    elif option == 2:
                                        print("Missing angle Cos")
                                        zahl1 = float(
                                            input("Put the site from the angle: ")
                                        )
                                        zahl2 = float(input("Put hypotenuse: "))
                                        ergebnis = cosinus_angle(zahl1, zahl2)
                                        print(
                                            f"Cosines is: {round(ergebnis, 2)} degrees"
                                        )
                                    elif option == 3:
                                        print("Exit cosines.")
                                        break
                                    else:
                                        print("Invalid option!")
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Tangents")
                                print(banner)
                                zahl1 = float(input("Put the adjacent: "))
                                zahl2 = float(input("Put the angel: "))
                                ergebnis = tangens(zahl2, zahl1)
                                print(f"Tangents is: {round(ergebnis, 2)} long")
                            elif option == 4:
                                print("Angular functions exit.")
                                break
                            else:
                                print("Invalid option!")
                    elif option == 3:
                        while True:
                            # Flächenberechnung
                            banner = pyfiglet.figlet_format("Surface Calc")
                            print(banner)
                            print("Options")
                            print("1. Rectangle")
                            print("2. Circle")
                            print("3. Triangle")
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
                                zahl1 = float(input("Put the radius: "))
                                ergebnis = circle(zahl1)
                                print(
                                    f"The circle surface is {round(ergebnis, 2)} large"
                                )
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Triangle")
                                print(banner)
                                zahl1 = float(input("Put the baseline: "))
                                zahl2 = float(input("Put the height: "))
                                ergebnis = triangle_surface(zahl1, zahl2)
                                print(f"The triangle is {round(ergebnis, 2)} large")
                            elif option == 4:
                                banner = pyfiglet.figlet_format("Trapezium")
                                print(banner)
                                print(
                                    "This only works with the site a and c and the height!"
                                )
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
                            # Volumen berechnung
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
                                print(
                                    f"{zahl1} * {zahl2} * {zahl3} = {round(ergebnis, 2)}"
                                )
                            elif option == 2:
                                banner = pyfiglet.figlet_format("Rectangle")
                                print(banner)
                                zahl1 = float(input("Put the site a: "))
                                zahl2 = float(input("Put the site b: "))
                                zahl3 = float(input("Put the site c: "))
                                ergebnis = rectangle_volume(zahl1, zahl2, zahl3)
                                print(
                                    f"{zahl1} * {zahl2} * {zahl3} = {round(ergebnis, 2)}"
                                )
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Pyramid")
                                print(banner)
                                zahl1 = float(input("Put the baseline a: "))
                                zahl2 = float(input("Put the height hk: "))
                                ergebnis = pyramid_volume(zahl1, zahl2)
                                print(
                                    f"The volume from the pyramid is {round(ergebnis, 2)}"
                                )
                            elif option == 4:
                                banner = pyfiglet.figlet_format("Sphere")
                                print(banner)
                                zahl1 = float(input("Put the radius: "))
                                ergebnis = sphere(zahl1)
                                print(
                                    f"The volume from the sphere is {round(ergebnis, 2)}"
                                )
                            elif option == 5:
                                print("Volume calc exit")
                                break
                            else:
                                print("Invalid option!")
                    elif option == 5:
                        banner = pyfiglet.figlet_format("Integral")
                        print(banner)
                        print("In progress")
                    elif option == 6:
                        while True:
                            # Prozent
                            banner = pyfiglet.figlet_format("Percent")
                            print(banner)
                            print("Options:")
                            print("1. Percentage")  # Prozentsatz %
                            print("2. Basic amount")  # Grundwert G
                            print("3. Percentage value")  # Prozentwert W
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
                                ergebnis = basic_amount(zahl1, zahl2)
                                print(f"The basic amount is {ergebnis}")
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Percentage value")
                                print(banner)
                                zahl1 = float(input("Put the basic amount: "))
                                zahl2 = float(input("Put the percentage%: "))
                                ergebnis = percentage_value(zahl1, zahl2)
                                print(f"The percentage value is {ergebnis}")
                            elif option == 4:
                                print("Percent exit")
                                break
                            else:
                                print("Invalid option!")
                    elif option == 7:
                        while True:
                            banner = pyfiglet.figlet_format("Fractional Functions")
                            print(banner)
                            print("Options:")
                            print("1. Addition")
                            print("2. Subtraction")
                            print("3. Multiplication")
                            print("4. Division")
                            print("5. Fractional functions exit.")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                banner = pyfiglet.figlet_format("Addition")
                                print(banner)
                                try:
                                    zahler1 = int(
                                        input(
                                            "Enter the numerator of the first fraction: "
                                        )
                                    )
                                    nenner1 = int(
                                        input(
                                            "Enter the denominator of the first fraction: "
                                        )
                                    )
                                except ValueError:
                                    print(
                                        "Invalid Input. Please enter whole numbers for the numerator and denominator."
                                    )
                                except ZeroDivisionError:
                                    print("The denominator cannot be zero.")
                                try:
                                    zahler2 = int(
                                        input(
                                            "Enter the numerator of the second fraction:"
                                        )
                                    )
                                    nenner2 = int(
                                        input(
                                            "Enter the denominator of the second fraction: "
                                        )
                                    )
                                    ergebnis = braddit(
                                        zahler1, nenner1, zahler2, nenner2
                                    )
                                    print(f"The sum is : {ergebnis}")
                                except ValueError:
                                    print(
                                        "Invalid Input. Please enter whole numbers for the numerator and denominator."
                                    )
                                except ZeroDivisionError:
                                    print("The denominator cannot be zero.")
                            elif option == 2:
                                banner = pyfiglet.figlet_format("Subtraction")
                                print(banner)
                                try:
                                    zahler1 = int(
                                        input(
                                            "Enter the numerator of the first fraction: "
                                        )
                                    )
                                    nenner1 = int(
                                        input(
                                            "Enter the denominator of the first fraction: "
                                        )
                                    )
                                except ValueError:
                                    print(
                                        "Invalid Input. Please enter whole numbers for the numerator and denominator."
                                    )
                                except ZeroDivisionError:
                                    print("The denominator cannot be zero.")
                                try:
                                    zahler2 = int(
                                        input(
                                            "Enter the numerator of the second fraction:"
                                        )
                                    )
                                    nenner2 = int(
                                        input(
                                            "Enter the denominator of the second fraction: "
                                        )
                                    )
                                    ergebnis = brmulti(
                                        zahler1, nenner1, zahler2, nenner2
                                    )
                                    print(f"The sum is : {ergebnis}")
                                except ValueError:
                                    print(
                                        "Invalid Input. Please enter whole numbers for the numerator and denominator."
                                    )
                                except ZeroDivisionError:
                                    print("The denominator cannot be zero.")
                            elif option == 3:
                                banner = pyfiglet.figlet_format("Multiplication")
                                print(banner)
                                try:
                                    zahler1 = int(
                                        input(
                                            "Enter the numerator of the first fraction: "
                                        )
                                    )
                                    nenner1 = int(
                                        input(
                                            "Enter the denominator of the first fraction: "
                                        )
                                    )
                                except ValueError:
                                    print(
                                        "Invalid Input. Please enter whole numbers for the numerator and denominator."
                                    )
                                except ZeroDivisionError:
                                    print("The denominator cannot be zero.")
                                try:
                                    zahler2 = int(
                                        input(
                                            "Enter the numerator of the second fraction:"
                                        )
                                    )
                                    nenner2 = int(
                                        input(
                                            "Enter the denominator of the second fraction: "
                                        )
                                    )
                                    ergebnis = braddit(
                                        zahler1, nenner1, zahler2, nenner2
                                    )
                                    print(f"The sum is : {ergebnis}")
                                except ValueError:
                                    print(
                                        "Invalid Input. Please enter whole numbers for the numerator and denominator."
                                    )
                                except ZeroDivisionError:
                                    print("The denominator cannot be zero.")
                            elif option == 4:
                                banner = pyfiglet.figlet_format("Division")
                                print(banner)
                                try:
                                    zahler1 = int(
                                        input(
                                            "Enter the numerator of the first fraction: "
                                        )
                                    )
                                    nenner1 = int(
                                        input(
                                            "Enter the denominator of the first fraction: "
                                        )
                                    )
                                except ValueError:
                                    print(
                                        "Invalid Input. Please enter whole numbers for the numerator and denominator."
                                    )
                                except ZeroDivisionError:
                                    print("The denominator cannot be zero.")
                                try:
                                    zahler2 = int(
                                        input(
                                            "Enter the numerator of the second fraction:"
                                        )
                                    )
                                    nenner2 = int(
                                        input(
                                            "Enter the denominator of the second fraction: "
                                        )
                                    )
                                    ergebnis = brdivi(
                                        zahler1, nenner1, zahler2, nenner2
                                    )
                                    print(f"The sum is : {ergebnis}")
                                except ValueError:
                                    print(
                                        "Invalid Input. Please enter whole numbers for the numerator and denominator."
                                    )
                                except ZeroDivisionError:
                                    print("The denominator cannot be zero.")
                            elif option == 5:
                                print("Fractional functions exit.")
                                break
                    elif option == 8:
                        print("Advanced math exit.")
                        break
                    else:
                        print("Invalid option!")
            elif option == 6:
                while True:
                    # Physik
                    banner = pyfiglet.figlet_format("Physics")
                    print(banner)
                    print("Options:")
                    print("1. Speed and Route calc")
                    print("2. Acceleration in [m/s]")
                    print("3. Mechanic Newton [N]")
                    print("4. Electricity [⚡]")
                    print("5. Physics exit")

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
                                print(
                                    f"The vehicle is {round(ergebnis, 2)} km driven far"
                                )
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
                        ergebnis = mechanic_newton(zahl1, zahl2)
                        print(f"The force is {ergebnis} N")
                    # Strom berechnung
                    elif option == 4:
                        while True:
                            banner = pyfiglet.figlet_format("Electricity")
                            print(banner)
                            print("Options:")
                            print("1. Voltage [V]")
                            print("2. Watt [P]")
                            print("3. Ohm [R]")
                            print("4. Ampere [I]")
                            print("5. Electricity exit.")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                while True:
                                    banner = pyfiglet.figlet_format("Voltage")
                                    print(banner)
                                    print("Options:")
                                    print("1. R*I")
                                    print("2. P/I")
                                    print("3. √P*R")
                                    print("4. Voltage exit")

                                    option = int(input("Choose a option"))
                                    os.system("cls")

                                    if option == 1:
                                        banner = pyfiglet.figlet_format("R * I")
                                        print(banner)
                                        zahl1 = float(input("Put R: "))
                                        zahl2 = float(input("Put I: "))
                                        ergebnis = voltageri(zahl1, zahl2)
                                        print(f"The voltage is {ergebnis}")
                                    elif option == 2:
                                        banner = pyfiglet.figlet_format("R / I")
                                        print(banner)
                                        zahl1 = float(input("Put R: "))
                                        zahl2 = float(input("Put I: "))
                                        ergebnis = voltage_ri(zahl1, zahl2)
                                        print(f"The voltage is {ergebnis}")
                                    elif option == 3:
                                        banner = pyfiglet.figlet_format("√P*R")
                                        print(banner)
                                        zahl1 = float(input("Put P: "))
                                        zahl2 = float(input("Put R: "))
                                        ergebnis = voltage_pr(zahl1, zahl2)
                                        print(f"The voltage is {round(ergebnis, 2)}")
                                    else:
                                        print("Voltage exit.")
                                        break
                            elif option == 2:
                                while True:
                                    banner = pyfiglet.figlet_format("Watt")
                                    print(banner)
                                    print("Options:")
                                    print("1. U²/R")
                                    print("2. U/I")
                                    print("3. R * I")
                                    print("4. Watt exit")

                                    option = int(input("Choose a option: "))
                                    os.system("cls")

                                    if option == 1:
                                        banner = pyfiglet.figlet_format("U / R")
                                        print(banner)
                                        zahl1 = float(
                                            input(
                                                "Put U in square or say 1 for only the u: "
                                            )
                                        )
                                        if zahl1 == 1:
                                            zahl1 = float(input("Put U: "))
                                            zahl2 = float(input("Put R: "))
                                            ergebnis = urwatt(zahl1, zahl2)
                                            print(f"The Watt is {round(ergebnis, 2)}")
                                        else:
                                            zahl2 = float(input("Put R: "))
                                            ergebnis = urwatti(zahl1, zahl2)
                                            print(f"The Watt is {round(ergebnis, 2)} ")
                                    elif option == 2:
                                        banner = pyfiglet.figlet_format("U / I")
                                        print(banner)
                                        zahl1 = float(input(f"Put U: "))
                                        zahl2 = float(input(f"Put I: "))
                                        ergebnis = division(zahl1, zahl2)
                                        print(f"The Watt is {round(ergebnis, 2)}")
                                    elif option == 3:
                                        banner = pyfiglet.figlet_format("U / I")
                                        print(banner)
                                        zahl1 = float(input(f"Put R: "))
                                        zahl2 = float(input(f"Put I: "))
                                        ergebnis = multiplication(zahl1, zahl2)
                                        print(f"The Watt is {round(ergebnis, 2)}")
                                    elif option == 4:
                                        print("Watt exit.")
                                        break
                            elif option == 3:
                                while True:
                                    banner = pyfiglet.figlet_format("Ohm")
                                    print(banner)
                                    print("Options:")
                                    print("1. U / I")
                                    print("2. P / I²")
                                    print("3. U² / P")
                                    print("4. Ohm exit")

                                    option = int(input("Choose a option"))
                                    os.system("cls")

                                    if option == 1:
                                        banner = pyfiglet.figlet_format("U / I")
                                        print(banner)
                                        zahl1 = float(input(f"Put U: "))
                                        zahl2 = float(input(f"Put I: "))
                                        ergebnis = multiplication(zahl1, zahl2)
                                        print(f"The resistance is {round(ergebnis, 2)}")
                                    elif option == 2:
                                        banner = pyfiglet.figlet_format("P / I²")
                                        print(banner)
                                        zahl1 = float(input(f"Put P: "))
                                        zahl2 = float(input(f"Put I²: "))
                                        ergebnis = multiplication(zahl1, zahl2)
                                        print(f"The resistance is {round(ergebnis, 2)}")
                                    elif option == 3:
                                        banner = pyfiglet.figlet_format("U / I")
                                        print(banner)
                                        zahl1 = float(input(f"Put U: "))
                                        zahl2 = float(input(f"Put I²: "))
                                        ergebnis = multiplication(zahl1, zahl2)
                                        print(f"The resistance is {round(ergebnis, 2)}")
                                    elif option == 4:
                                        print("Ohm exit.")
                                        break
                            elif option == 4:
                                while True:
                                    banner = pyfiglet.figlet_format("Ampere")
                                    print(banner)
                                    print("Options:")
                                    print("1. √P/R")
                                    print("2. P/U")
                                    print("4. U/R")
                                    print("4. Ampere exit.")

                                    option = int(input("Choose a option:"))
                                    os.system("cls")

                                    if option == 1:
                                        banner = pyfiglet.figlet_format("√P/R")
                                        print(banner)
                    elif option == 5:
                        print("Physics exit.")
                        break
                    else:
                        print("Invalid option!")
            elif option == 7:
                while True:
                    # Potenzen u Wurzel ziehen
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
                        zahl1 = float(
                            input("Put the number that you want to potency: ")
                        )
                        zahl2 = float(input("Put the exponent: "))
                        ergebnis = potency(zahl1, zahl2)
                        print(f"The Sum is {ergebnis}")
                    elif option == 2:
                        while True:
                            # Wurzel ziehen
                            banner = pyfiglet.figlet_format(
                                "Pull root and calc with roots"
                            )
                            print(banner)
                            print("Options:")
                            print("1. Calc with roots2(Basic Math)")
                            print("2. Pull square2 root and cube3 root")
                            print("3. Pull-root exit")

                            option = int(input("Choose a option: "))
                            os.system("cls")

                            if option == 1:
                                while True:
                                    # Wurzel2 rechnen
                                    banner = pyfiglet.figlet_format("Calc with roots2")
                                    print(banner)
                                    print(
                                        "This works so example: the root x2 + number = result"
                                    )
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
                                        zahl1 = float(input("Put the radiant: "))
                                        zahl2 = float(input("Put a number: "))
                                        ergebnis = root_addition(zahl1, zahl2)
                                        print(f"The result is {ergebnis}")
                                    elif option == 2:
                                        banner = pyfiglet.figlet_format("Subtrac-root")
                                        print(banner)
                                        zahl1 = float(input("Put the radiant: "))
                                        zahl2 = float(input("Put the number: "))
                                        ergebnis = root_subtraction(zahl1, zahl2)
                                        print(f"The result is {ergebnis}")
                                    elif option == 3:
                                        banner = pyfiglet.figlet_format("Multipli-root")
                                        print(banner)
                                        zahl1 = float(input("Put the radiant: "))
                                        zahl2 = float(input("Put the the number: "))
                                        ergebnis = root_multiplication(zahl1, zahl2)
                                        print(f"The result is {round(ergebnis, 2)}")
                                    elif option == 4:
                                        banner = pyfiglet.figlet_format("Division-root")
                                        print(banner)
                                        zahl1 = float(input("Put the radiant: "))
                                        zahl2 = float(input("Put the number: "))
                                        ergebnis = root_division(zahl1, zahl2)
                                        print(f"The sum is {round(ergebnis, 2)}")
                                    elif option == 5:
                                        print("Calc with roots2 exit.")
                                        break
                                    else:
                                        print("Invalid option!")
                            elif option == 2:
                                while True:
                                    # Wurzeln ziehen
                                    banner = pyfiglet.figlet_format(
                                        "Pull square2 root and cube3 root"
                                    )
                                    print(banner)
                                    print("Options:")
                                    print("1. Exponent 2")
                                    print("2. Exponent 3")
                                    print("3. Pull square2 root and cube3 root exit")

                                    option = int(input("Choose a option: "))
                                    os.system("cls")

                                    if option == 1:
                                        zahl1 = float(input("Put the radiant: "))
                                        ergebnis = pull_root_2(zahl1)
                                        print(
                                            f"The square root from {zahl1} is {round(ergebnis, 2)}"
                                        )
                                    elif option == 2:
                                        zahl1 = float(input("Put the radiant: "))
                                        ergebnis = pull_root_3(zahl1)
                                        print(
                                            f"The cube root from {zahl1} is {round(ergebnis, 2)}"
                                        )
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
                        print("Yasin.Aslan")
                        print("MIT License Copyright (c) 2023 Yasin Aslan")
                    elif option == 2:
                        banner = pyfiglet.figlet_format("GitHub")
                        print(banner)
                        webbrowser.open("https://github.com/Yasin-Aslan")
                    elif option == 3:
                        print("Credits exit.")
                        break
                    else:
                        print("Invalid option!")
            elif option == 9:
                print("Program exit.")
                break
            else:
                print("Invalid option!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
