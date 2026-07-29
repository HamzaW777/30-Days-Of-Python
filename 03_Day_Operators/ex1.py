import math

def q21():
    years = int(input("Enter the number of years: "))
    seconds = years * 365 * 24 * 60 * 60
    print(f"{years} years is {seconds} seconds")


def q23():
    for i in range(1, 6):
        print(i, 1, i, i**2, i**3)


q23()