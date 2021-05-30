# Pattern using for loop
# Using for loop
# def pattern_of(value):
#     for i in range (0, value):
#         for j in range (0, i + 1):
#             print("*", end = " ")
#         print()

# value = int(input("Enter the value: "))
# pattern_of(value)

# Pattern Using while loop
# def pattern_of2(value):
#     i = 1
#     while i <= 5:
#         j = 1
#         while j <= i:
#             print("*", end = " ")
#             j = j + 1
#         print()
#         i = i + 1

# pattern_of2(5)

#  square pattern
def sq_pattern(value):
    for i in range(value):
        for j in range(value):
            if i == 0 or i == value - 1 or j == 0 or j == value - 1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()

sq_pattern(5)
