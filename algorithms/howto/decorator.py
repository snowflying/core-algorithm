# decorator is one simple way to achieve closure feature
# but different from clouse is the decorator take func as parameter which been called and return in nested-function,
# the clouse is the nested-function keeping and using the data from en-closuing data from en-clousing function
# 
# the same points of clouse and decorator is the end of the enclosing function will return the reference of the nested-function

## key point 1: been decorated function with parameters
def make_pretty(func):

    def inner(a, b):
        if b == 0:
            print("Whooop! the parameter b can't equal to 0")
        else:
            return func(a, b)
    return inner


@make_pretty # here, caution: no (), so you need to call it like below example to make it run
def divide(a, b):
    print(a / b)

## test
# divide(4, 2) # from here begin the call(), divide(4, 2) == make_pretty(divide(4, 2))
# print('==__'*10)
# divide(4, 0)

## key point 2: the decorator function contains parameters while decorating other function 
def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(func):

        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])

        func()

    # reurning inner function
    return inner


@decorator(like="abc")  # here, caution: (), () means begin to call/run, so the my_func will be as one parameter passed into decorator(like="abc")(my_func), decorator(like='abc') == inner()
def my_func():
    print("Inside actual function")

# no need my_func()


## key point 3: 
def decodecorator(dataType, message1, message2):
    def decorator(fun):
        print(message1)
        def wrapper(*args, **kwargs):
            # print(message2)
            # if all([type(arg) == dataType for arg in args]):
            #     return fun(*args, **kwargs)
            # return "Invalid Input"
            print(args)
        return wrapper
    return decorator
 
# below, equal to decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")(stringJoin), but stop running at 'return wrapper'
@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
    st = ''
    for i in args:
        st += i
    return st

stringJoin('good job') #here, start running from wrapper('good, jobs')

@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ

## key point 4: decorating class
# A class decorator is a callable that takes a class as an argument (the decorated class) and modifies or replaces the decorated class with another class.
def decorator_function(target):

    def decorator_init(self):
        print("Decorator running")

    target.__init__ = decorator_init
    return target

@decorator_function
class Target:
    def __init__():
        print("Target running")

Target()
