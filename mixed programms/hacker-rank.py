import textwrap
# 01 Given an integer, , perform the following conditional actions:

#(If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird)

def racker(n):
    if (n % 2 == 1):
        print("Weired")
    elif (n % 2 == 0 and 2 <= n <= 5):
        print("Not Weierd")
    elif (n % 2 == 0 and 6 <= n <= 20):
        print("Weired")
    else:
        print("Not Weired")

# racker(3)
# racker(4)
# racker(24)


# 02 Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):
    leap = False
    if year%4==0:
        if year%100!=0 or year%400==0:
            leap = True
        else:
            leap = False
    else:
        leap = False
    return leap

# # print(is_leap(1992))


# 03 Without using any string methods, try to print the following:
# 123...n

# Note that "...." represents the consecutive values in between.
def nmbr(n):
    for i in range(1, n+1):
        print(i, end="")

# nmbr(3)

# 04 You are given a string s and width w.
# Your task is to wrap the string into a paragraph of width w.
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

# print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 3))

# 05 You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (x, y, z) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x;0<=j<=y;0<=k<=z. Please use list comprehensions rather than multiple loops.

def list(x, y, z, n):
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

# list(1, 1, 1, 2)

# 06 