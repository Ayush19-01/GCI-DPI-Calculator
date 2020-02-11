# Created for the sole purpose of GCI 2019
import math
def dpi():
    a=float(input("Enter the width of your screen in pixels:"))
    b=float(input("Enter the height of your screen in pixels:"))
    di=float(input("Enter the advertised length of the screen in inches:"))
    dp=math.sqrt(a**2 +b**2)
    dpi=round(dp/di)
    print("The dpi of your monitor is:", dpi,"dots per inch","\n")
def aratio(width: int, height: int) -> str:
    r=gcd(width, height)
    x=int(width / r)
    y=int(height / r)

    print("Your Aspect ratio is= "f"{x}:{y}","\n")
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
    
while True:
    print("Welcome to DPI and aspect ratio calculator!")
    print("Choose from the following options:")
    print("1)DPI of the screen\n2)Aspect Ratio\n3)Exit")
    choice=int(input("Enter your choice(enter the numbber 1 2 or 3):"))
    if choice==1:
        dpi()
    if choice==2:
        a=float(input("Enter the width of your screen in pixels:"))
        b=float(input("Enter the height of your screen in pixels:"))
        aratio(a,b)
    if choice>=3:
        print("Thank You for using the program!")
        break
    
