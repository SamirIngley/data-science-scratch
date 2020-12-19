# ordered collection, an array with more functionality

# GET or SET nth element
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

four = x[4]
ten = x[-1]

# SLICE the list, i:j means all elements i (inclusive) to j(not inclusive)
first_three = x[:3]
one_to_four = x[1:5]

copy_of_x = x[:]

# third argument - stride
every_third = x[::3]
five_to_three =x[5:2:-1]    # [5, 4, 3]   backwards

# IN operator to check for MEMBERSHIP
1 in [1,2,3]    # True
0 in [1,2,3]    # False


# CONCATENATING lists together
x = [1,2,3]
x.extend([4,5,6])   # x is now [1,2,3,4,5]

# new list
y = x + [4,5,6]     # x is untouched

# APPEND
x.append(0)

# convenient to unpack lists if you know how many elements they contain
x, y = [1, 2]

# replace x or y in the above with _ if you're not going to use that variable
