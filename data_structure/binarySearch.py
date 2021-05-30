#Binary search
# def binary_search(list, target):
#     first = 0
#     last = len(list) - 1

#     while first <= last:
#         midpoint = (first + last)//2
#         if list[midpoint] == target:
#             return midpoint
#         elif list[midpoint] < target:
#             first = midpoint + 1
#         else:
#             last = midpoint - 1
#     return None

# def verify(index):
#     if index is not None:
#         print("Target found at index: ", index)
#     else:
#         print("Target not found in list")

# number = [1,2,3,4,5,6,7,8,9,10]

# result = binary_search(number, 5)
# verify(result)


# Recursive_Binary_Search
def rec_bin_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        # print(midpoint)
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return rec_bin_search(list[midpoint + 1:], target)
            else:
                return rec_bin_search(list[:midpoint], target)


def verify(result):
    print("Target found: ", result)


number = list(range(100))
print(number)

result = rec_bin_search(number, 100)
verify(result)