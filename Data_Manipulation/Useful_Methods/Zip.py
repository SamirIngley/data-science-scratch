# zip two iterables together - transforms multiple iterables into a single iterable of tuples

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy so first we do something like this
[pair for pair in zip(list1, list2)]    # is [('a', 1), ('b', 2), ('c', 3)]

# if the lists are different lengths, zip stops as soon as the first list ends

# UNZIP: * performs argument unpacking which uses elements of pairs as individual arguments to zip. 
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

# equivalent..
letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))



# can use argument unpacking with any function
def add(a,b): return a + b

add(1,2)    # returns 3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")
    
add(*[1, 2])    # returns 3