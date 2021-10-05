# reference: https://www.programiz.com/python-programming/generator
# Python generators are a simple way of creating iterators. otherwise you need to write __iter__ & __next__
# All the work we mentioned to create __iter__ & __next__ are automatically handled by generators in Python.
# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

# If a function contains at least one yield statement (it may contain other yield or return statements),
#  it becomes a generator function. Both yield and return will return some value from a function.

# The difference is that while a return statement terminates a function entirely, yield statement pauses
#  the function saving all its states and later continues from there on successive calls.

# Here is how a generator function differs from a normal function.
# Generator function contains one or more yield statements.
# When called, it returns an object (iterator) but does not start execution immediately.
# Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between successive calls.
# Finally, when the function terminates, StopIteration is raised automatically on further calls.

# yield contains: 1/ __iter__, 2/ __next__, 3/ consume StopIteration exception
from typing import Coroutine


def fabonacci(num):
    n1, n2 = 0, 1
    while n1 <= num:
        yield n1
        n1, n2 = n2, n1+n2

# fabonacci() --> call __new__/__init__ return one object
# for loop make the below two things
# 1/ call method __iter__ of fabonacci(10) --> return one iterator 
# 2/ call __next__ method of the fabonacci(10) to iterate the fabonacci()
for item in fabonacci(10):
    print(item)


# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

# below, althrough the function my_gen been called, but as this function 
# contains keyword yield that will just returns an object (iterator) but
# does not start execution immediately.  hence, the first print statement
# shouldn't been run until the first next() function to trigger it
>>> # It returns an object but does not start execution immediately.
>>> a = my_gen()

>>> # We can iterate through the items using next().
>>> next(a)
This is printed first
1
>>> # Once the function yields, the function is paused and the control is transferred to the caller.

>>> # Local variables and theirs states are remembered between successive calls.
>>> next(a)
This is printed second
2

>>> next(a)
This is printed at last
3

>>> # Finally, when the function terminates, StopIteration is raised automatically on further calls.
>>> next(a)
Traceback (most recent call last):
...
StopIteration
>>> next(a)
Traceback (most recent call last):
...
StopIteration


### Python Generator Expression ###
# simple generators can be easily created with generator expressions,

# The syntax for generator expression is similar to that of a list comprehension in Python. 
# But the square brackets are replaced with round parentheses.

# The major difference between a list comprehension and a generator expression 
# is that a list comprehension produces the entire list while the generator 
# expression produces one item at a time.

# generator has lazy execution ( producing items only when asked for ). For this reason, 
# a generator expression is much more memory efficient than an equivalent list comprehension.

# Initialize the list
my_list = [1, 3, 6, 10]

list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)


for item in list_:
    pass

for item in generator:
    pass

## generator using scenario ###

# 1. Easy to Implement
class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

# The above program was lengthy and confusing. Now, let's do the same using a generator function.

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

# 2. Memory Efficient
# A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill, if the number of items in the sequence is very large.

# Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.

# 3. Represent Infinite Stream
# Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.

# The following generator function can generate all the even numbers (at least in theory).

def all_even():
    n = 0
    while True:
        yield n
        n += 2


# 4. Pipelining Generators
# Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.

# Suppose we have a generator that produces the numbers in the Fibonacci series. And we have another generator for squaring numbers.

# If we want to find out the sum of squares of numbers in the Fibonacci series, we can do it in the following way by pipelining the output of generator functions together.

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
Output

4895



##### conception #####
## Coroutine # 协程，
## subroutine # 子程序， Subroutines are special cases of coroutines, both subroutine and coroutine are in same layer in programming
             # subroutine can be achieved in function and procedure
   # procedure # 步骤, will not return anything but just finish some flows
   # function # 函数, will return value to main program

## coroutine VS subroutine:

# Subroutines are special cases of coroutines.[3] When subroutines are invoked, 
# execution begins at the start, and once a subroutine exits, it is finished; 
# an instance of a subroutine only returns once, and does not hold state between invocations. 
# By contrast, coroutines can exit by calling other coroutines, which may later return to the point 
# where they were invoked in the original coroutine; from the coroutine's point of view, 
# it is not exiting but calling another coroutine.[3] Thus, a coroutine instance holds state, 
# and varies between invocations; there can be multiple instances of a given coroutine at once. 
# The difference between calling another coroutine by means of "yielding" to it 
# and simply calling another routine (which then, also, would return to the original point), 
# is that the relationship between two coroutines which yield to each other is not that of caller-callee, but instead symmetric.
# Any subroutine can be translated to a coroutine which does not call yield.[4]
# Here is a simple example of how coroutines can be useful. Suppose you have a consumer-producer relationship 
# where one routine creates items and adds them to a queue and another removes items from the queue and uses them.
#  For reasons of efficiency, you want to add and remove several items at once. The code might look like this:

# var q := new queue

# coroutine produce
#    loop
#        while q is not full
#            create some new items
#            add the items to q
#        yield to consume

# coroutine consume
#    loop
#        while q is not empty
#            remove some items from q
#            use the items
#        yield to produce

# call produce
# The queue is then completely filled or emptied before yielding control to the other coroutine using the yield command. 
# The further coroutines calls are starting right after the yield, in the outer coroutine loop.

# Although this example is often used as an introduction to multithreading, two threads are not needed for this: 
# the yield statement can be implemented by a jump directly from one routine into the other.

## coroutine VS mulithreading
# Coroutines are very similar to threads. However, coroutines are cooperatively multitasked, whereas threads are typically preemptively multitasked.
  # cooperatively multitasked(coroutine, achieved in language level)
    # The term preemptive multitasking is used to distinguish a multitasking operating system, which permits preemption of tasks,
    # from a cooperative multitasking system wherein processes or tasks must be explicitly programmed to yield when they do not 
    # need system resources

  # preemptively multitasked(mutiple-thread, achieved in system level)
    # Preemptive multitasking involves the use of an interrupt mechanism which suspends the currently executing process 
    # and invokes a scheduler to determine which process should execute next. Therefore, all processes will get some amount of CPU time at any given time.
    # In preemptive multitasking, the operating system kernel can also initiate a context switch to satisfy the scheduling 
    # policy's priority constraint, thus preempting the active task.

## advance of coroutine
# Coroutines provide concurrency but not parallelism. The advantages of coroutines over threads are that they may be used 
# in a hard-realtime context (switching between coroutines need not involve any system calls or any blocking calls whatsoever), there is no need for synchronisation primitives such as mutexes, semaphores, etc. in order to guard critical sections, and there is no need for support from the operating system.


## coroutine VS generator
# Generators, also known as semicoroutines,[5] are a subset of coroutines. Specifically, while both can yield multiple times, suspending their execution and allowing re-entry at multiple entry points, they differ in coroutines' ability to control where execution continues immediately after they yield, while generators cannot, instead transferring control back to the generator's caller.[6] That is, since generators are primarily used to simplify the writing of iterators, the yield statement in a generator does not specify a coroutine to jump to, but rather passes a value back to a parent routine.
# However, it is still possible to implement coroutines on top of a generator facility, with the aid of a top-level dispatcher routine (a trampoline, essentially) that passes control explicitly to child generators identified by tokens passed back from the generators:

# var q := new queue

# generator produce
#    loop
#        while q is not full
#            create some new items
#            add the items to q
#        yield consume

# generator consume
#    loop
#        while q is not empty
#            remove some items from q
#            use the items
#        yield produce

# subroutine dispatcher
#    var d := new dictionary(generator → iterator)
#    d[produce] := start produce
#    d[consume] := start consume
#    var current := produce
#    loop
#        call current
#        current := next d[current]

# call dispatcher

# implemention
# greenlet(basic notion), with no implicit scheduling
# evenlet, based on greenlet
# gevent, based on greenlet
  

# concurrency # 并发
# parallelism # 并行