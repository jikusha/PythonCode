# Lambda Functions
# Anonymous functions => function with no name

add = lambda n: n+4  # this lambda function is taking n as argument and returning n+4

print(add(4))
print(add(100))


mul = lambda x,y: x*y # taking x, y as arguments and returning x*y

# return keyword is not needed

print(mul(8,9))

# lambda with filter

l = [34,55,67,64,31,2,88]
odd = lambda n: n%2 != 0
odds = filter(odd, l) # it will return a iterable
odds = list(odds)
print(odds)

even = lambda n: 'T' if n%2 == 0 else 'F'
m = list(map(even, l))
print(m)

# lambda with map

l = [2,3,4,5,6,7]
square = lambda n: n**2
squares = list(map(square, l))
print(squares)

#lambda with list comprehension
squares = [lambda n = n:n**2 for n in l]
print(squares)
for s in squares:
    print(s())




# Python collection module

# Counter
from collections import Counter, deque, ChainMap
l = [1,2,1,3,4,2,4,5,6,7,6, 1]
c = Counter(l) # count the hashable objects
print(c)

d = deque()
d.append(5)
d.appendleft(78)
d.append(90)
print(d)
d.pop()
print(d)


d1 = {'name': 'Jiku', 'Age': 25}
d2 = {'Age': '23', 'Add': 'Nagaon'}

l = list(ChainMap(d1, d2)) # will make a list of the keys from the two dictionaries
print(l)


# decorator
# it takes function as an argument and return a function after modifying its behaviour
# so basically decorator is used to modify the behaviour of other functions


def greet(fn):
    def mfn(*args, **kwargs):
        print("Good Morning")
        fn(*args, **kwargs)
        print("Thanks for coming")

    return mfn

@greet
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a+b)

hello()
add(8,9)


# reduce
from functools import reduce

l = [1,4,5,3,2,6]
sum = reduce(lambda x,y: x+y, l)
print(sum)


# generator
# generator generates the values on the fly
# yield is used to return the value generated by generator
# yield returns a value, and suspends the function temporarily
# on the other hand, return returns a value and terminates the function
# generator generated the value when it is needed
# by doing so, it doesn't store all the values
# due to which, it is memory efficient and time efficient

def my_gen():
    for i in range(100):
        yield i

gen = my_gen()

print(next(gen))
print(next(gen))
print(next(gen))