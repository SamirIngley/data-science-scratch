# Way to specify that a function takes arbitrary arguments
# we use argument unpacking

def magic(*args, **kwargs):
    print("unnamed args: ", args)
    print("keyword args: ", kwargs)

magic(1, 2, key="word", key2="word")

# args is a tuple of its unnamed arguments
# kwargs is a dict of its named arguments

def other_way_magic(x, y, z):
    return x + y + z

x_y_z_list = [1, 2]
z_dict = {"z": 3}

assert other_way_magic(*x_y_z_list, **z_dict) == 6, "1 + 2 + 3 should be 6"
