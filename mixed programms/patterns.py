# Pattern using for loop
# Using for loop
def pattern_of(value):
    for i in range (0, value):
        for j in range (0, i + 1):
            print("*", end = " ")
        print()

# value = int(input("Enter the value: ")) #To call function "pattern_of" uncomment value
# pattern_of(value) #To call function "pattern_of" uncomment pttern_of()

# Pattern Using while loop
def pattern_of2(value):
    i = 1
    while i <= 5:
        j = 1
        while j <= i:
            print("*", end = " ")
            j = j + 1
        print()
        i = i + 1

# pattern_of2(5) #To call function "pattern_of2" uncomment pttern_of2()

#  square pattern
def sq_pattern(value):
    for i in range(value):
        for j in range(value):
            if i == 0 or i == value - 1 or j == 0 or j == value - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

# sq_pattern(5) #To call function "sq_pattern" uncomment sq_pttern()

# Pyramid
def pyramid(size):
    for i in range(0, size):
        for j in range(0, size - i):
            print(" ", end = "")
        for k in range(0, 2*i+1):
            print("0", end = "")
        print("")

# pyramid(5)