
import math

#string = input().split()
vuurkracht = float(input())
zw = float(input())
afstand = float(input())

v = vuurkracht * vuurkracht
toparse = zw * afstand / v
x = math.asin(toparse) / 2

print("{0:.2f}".format(x))