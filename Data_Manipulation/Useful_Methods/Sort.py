# by default smallest to largest

x = [4, 1, 2, 3]
y = sorted(x)       # order of x is preserved
x.sort()            # now x is sorted 

# can specify with sorted
# reverse = True (largest to smallest)
# instead of comparing the elements themselves, you can compare the results of a function that you specify with key

x = sorted([-4, 1, -2, 3], key=abs, reverse=True)   # is [-4, 3, -2, 1]








