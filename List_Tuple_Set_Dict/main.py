# Interpreted Language: Python does not require compilation,
# allowing rapid development and testing. It uses Interpreter instead of Compiler.


# List
# List is a collection of various data types
# It is mutable
# It can hold sequence of data
# List items can be accessed by index (random access)

a = [3,4, "Jiku"]
b = [3,4,"Jiku"]
c = [3,"Jiku",4]

print(a==b)
print(a==c)
print(a+c) #cancatenation

b.append(56)
print(b)
b.remove(56)
print(b)
print(len(b))
d = [32,78,4]
print(max(d))
print(min(d))

b.append([7,8]) # it will always add new elements to the end of the list
print(b)

b.insert(2, "Biki") #postion and value
print(b)

b.insert(0, 9)
print(b)

b.extend([9,"Jiks", (8,)]) # this will add multiple elements at the same time to the end of the list
print(b)

# Note: append() and extend() methods can only add elements at the end

# reverse a list
b.reverse()
print(b)

# reversed returns a reverse iterator which can be convert into list using list()
b_rev = list(reversed([12,13,14,15]))
print(b_rev)

# remove
l = [1,1,4,5,6,5]
l.remove(1) # removes the first occurance of element 1
print(l)

# pop
l.pop(0) # removes element from a particular index
print(l)

l.pop() # removes element from last
print(l)


# Tuple
# A comma sepearted inside (), can hold various data types
# immutable
# we can't alter the elements once created like lists
# It is a ordered sequence like lists
# Tuple is faster than list
# Tuple prevents accidental modification of elements as it is mutable
# Tuple can be utilized as dictionary keys due to its immutable nature. On the other hand, lists can't be used as dictionary keys
# Tuple is more memory efficient than Lists for bigger no of elements. As Tuple is immutable.
# Python allocates bigger chunks of memory with minimal overhead. Python,
# on the contrary, allots smaller memory chunks for lists. The tuple would therefore have less memory
# than the list. If we have a huge number of items, this makes tuples a little more memory-efficient than lists.

a = 4,5 # or (4,5)
print(a)
print(a[0])
print(a[1])
print(a[-1])

b = (4,5,"df",(4,5,6), "ds")
print(b[3][2]) # accessing a nested tuple
print(b[1:3]) #slicing
#del b[0] # tuple element can' be deleted also as it is immutable
# a[0] = 56 # it will rasie error asn tuple is immutable

b = b*2 #repetiiton is possible. It will create a new tuple and assign it to b. It will not change the existing tuple.
print(b)

print(len(b))
print(b.count((4, 5, 6)))
print(b.index(5))

print(a+b) # concatenation


# Similarities
# Both List and Tuples are ordered, sequential and can be accessed via index, we can iterate over the elements.
# Both can store different data types

print(dir(a)) # Tuple build in methods # less
print(dir([])) # List build in methods # more



# List Comprehensions
nums = [4,5,6,7]
n = [x**2 for x in nums]
print(n)
