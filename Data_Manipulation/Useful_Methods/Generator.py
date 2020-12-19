# Often all we need to do is iterate over the collection using for an in. In this case we can create generators,
# which can be iterated over like lists, but generate their values lazily on demand

# one way to create generator is with 'yield'
def generate_range(n):
    i = 0
    while i< n:
        yield i     # every call to yield produces a value of the generator
        i+= 1

evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)


# ENUMERATE turns values into pairs (index, value)
names = ["Alice", "Bob", "Charlie", "Debbie"]

for i, name in enumerate(names):
    print(f"name {i} is {name}")


    