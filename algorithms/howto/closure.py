# out this file is belong the built-in namespace
# this is the global namespace
def print_msg(msg):
    # This is the outer enclosing function
    # 'msg' is belong to enclosing namespaces 

    def printer():
        # This is the nested function
        # this is the local namespace
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()


## three points to achieve closure ##
# We must have a nested function (function inside a function).
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.(attention: return nested function's 
# reference, not call nexted function)

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

# On a concluding note, it is good to point out that the values that get enclosed in the closure function can be found out.
# All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function. Referring to the example above, we know times3 and times5 are closure functions.

>>> make_multiplier_of.__closure__
>>> times3.__closure__
(<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)
The cell object has the attribute cell_contents which stores the closed value.

>>> times3.__closure__[0].cell_contents
3
>>> times5.__closure__[0].cell_contents
5