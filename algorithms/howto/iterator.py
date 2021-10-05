# reference: https://www.programiz.com/python-programming/iterator

# Iterators are everywhere in Python. They are elegantly implemented
# within for loops, comprehensions, generators etc

# Iterator in Python is simply an object that can be iterated upon.
# An object which will return data, one element at a time. An object
# is called iterable if we can get an iterator from it.

# Most built-in containers in Python like: list, tuple, string etc. are iterables.

# The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
# We use the next() function to manually iterate through all the items of an iterator. When we reach the end and
# there is no more data to be returned, it will raise the StopIteration Exception.

# __iter__ --> only those object containing __iter__ can call iter() on itself to 
#              generate one iterable object/one iterator. yield contains __iter__
# __next__ --> only those object containing __next__ can call next() on itself to
#              iterate the iterator, yield contains __next__
# yield will help you deal with StopIteration Exception automatically

# Technically speaking, a Python iterator object must implement two special methods, __iter__() and __next__(), 
# collectively called the iterator protocol.


# write one your own iterable class
class Event():
    def __init__(self, size):
        self.n = 2
        self._max = size

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self._max:
            value = self.n
            self.n = self.n + 2
            return value
        else:
            raise StopIteration


eve = Event(25)
print(dir(eve))
print('-=' * 10)
print(eve)
print('-=' * 10)
print(next(eve))
print(next(eve))
print(next(eve))
print(next(eve))

print('-=' * 10)

# below, the for loop like always make next() to call method __next__ in the eve 
for item in eve:
    print(item)
