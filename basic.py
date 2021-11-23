
from collections import Counter
from collections import namedtuple
from collections import OrderedDict  # Dictionary that remembers insertion order
from collections import defaultdict
from collections import deque
from itertools import product
from itertools import permutations
from timeit import default_timer as timer
mydict = {"name": "max", "age": 28, "city": "New york"}
print(mydict)

# mydict["name"] = "a"
# print(mydict)
# del mydict["name"]
# mydict.pop("age")
# mydict.popitem()
if "name" in mydict:
    print(mydict["name"])
# to access a key which may or may not exist
try:
    print(mydict["nama"])
except:
    print("ERROR")
print("___")
# loop in dict
for key in mydict.keys():
    print(key)

for a in mydict:
    print(a)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

mydict_copy = mydict  # both dictonary points to same dict
mydict_copy["name"] = "Sri Ram"

mydict_copy_new = dict(mydict)
mydict_copy_new = mydict.copy()
mydict_copy_new["name"] = "Sri Krishna"
print(mydict)

new_dict = dict(name="Mahipal", age=21)
mydict.update(new_dict)  # overwrites old dict with new dict data
print(mydict)

# a tuple can be a key to dictionary, but not a list because list is mutable and can be chaged later on
mytuple = (2, 4)
mydict = {mytuple: 12}
print(mydict)

# A set in python is a data structure that contains an unordered collection of unique and immutable objects.
# Set in Python is a data structure equivalent to sets in mathematics.

# It may consist of various elements
# the order of elements in a set is undefined. You can add and delete elements of a set, you can iterate the elements of the set,

# ou can perform standard operations on sets(union, intersection, difference).
# Besides that, you can check if an element belongs to a set.

# Though sets can’t contain mutable objects, sets are mutable. But since they are unordered, indexing have no meaning. We cannot access or change an element of set using indexing or slicing. Set does not support it.
# set; Unordered, unmutable,don't allow duplicates, arbitrary order
myset = {3, 4, 5}  # just like dict but without key value pair
myset = set([23, 3, 3, 3, 4, 5, 5])
myset = set("hello")  # to find no of words in your word
emptyset = {}
print(type(emptyset))

emptyset = set()
print(type(emptyset))
emptyset.add(1)
emptyset.add(2)
emptyset.add(3)
emptyset.remove(1)  # give error if not found in the set
print(emptyset)

myset.discard(32)  # no error even if element is not in the set

print(myset.pop())  # remove arbitrary element
print(myset)

for x in myset:
    print(x)

if "h" in myset:
    print("YES")


# union and intersection of sets
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 0}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

I = odds.intersection(evens)
print(I)

I2 = odds.intersection(primes)
print(I2)

diff = primes.difference(evens)
print(diff)

diff = odds.difference(evens)
print(diff)

diff = primes.symmetric_difference(evens)  # same vale nhi aayenge
print(diff)
primes = {2, 3, 5, 7}
print(primes)  # {2, 3, 5, 7}
print(evens)
# primes.update(evens) #don't duplicate elements
# {0, 2, 3, 4, 5, 6, 7, 8}


# primes.intersection_update(evens) #keeps same things
print(primes)  # {2}

primes.difference_update(evens)
print(primes)


# Q. What's the difference between these two set methods?

# A. The update version subtracts from an existing set, mutating it, and potentially leaving it smaller than it originally was. The non-update version produces a new set, leaving the originals unchanged.

# Q. Because the difference_update updates set s, what precautions should be taken to avoid receiving a result of None from this method?

# A. Mutating methods in Python generally return None as a way to indicate that they have mutated an object. The only "precaution" is to not assign the None result to a variable.

# Q. In terms of speed, shouldn't set.difference_update be faster since you're only removing elements from set s instead of creating a new set like in set.difference()?

# A. Yes, the algorithm of the update version simply discards values.

# In contrast, the algorithm for the non-updating version depends on the size of the sets.

# If the size of s is four or more times larger that t, the new set version first copies the main set and then discards values from it. So "s - t is implemented as n = s.copy(); n.difference_update(t)). That algorithm is used when s is much larger than t

# Otherwise, the algorithm for the non-updating version is to create an empty new set n, loop over the elements of s and add them to n if they are not present in t.


setA = {3, 4, 5, 6, 7, 8}
setB = {3, 4, 1, 2}
setC = {3}
setD = {33}
print(setA.issubset(setB))
print(setA.issuperset(setB))
print(setA.issuperset(setC))
print(setA.isdisjoint(setD))  # if no same element, means have null intersecion

# copy
setE = setA
setE.add(333)
print(setA)  # A gets 333 also
setE = {2, 11, 22}
# now A and E are different
print(setE)
print(setA)

# to make a new set by copying data
set_copyA = set(setA)
set_copyA2 = setA.copy()

# it is frozen, no changes allowed, no add or remove can be made here
a = frozenset([2, 3, 4])
print(a)
# a.add(33) AttributeError: 'frozenset' object has no attribute 'add'

# union, update and difference methods works on frozenset


# set is mutable but with immutable elements.
setA = {2, [33, 3]}
TypeError: unhashable type: 'list'

for letter in set(“apple”):
    print(letter)
# p l e a


my_string = """hi
hey this is multiple
line string"""


my_string = """hi
hey this is multiple

line string"""


print(my_string[0])

# my_string[0] = "H"
# TypeError: 'str' object does not support item assignment
# strings are ordered, immutable, text representation

print(my_string[1:5])  # index 5 is excluded

# use + for concatanation
# TO LOOP OVER CHARACTERS
for i in my_string:
    # print(i)
    pass

# TO check
if "l" in my_string:
    print("YES")

my_string = '    here is lot of white   space     '
print(my_string)
my_string = my_string.strip()
print(my_string)  # removes leading and trailing whitespace
# doen't change string in place because string is immutable

print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("U"))
print(my_string.endswith("e"))
print(my_string.find('o'))  # return index starting from 0
print(my_string.find("P"))  # return -1 if not present
print(my_string.count('o'))  # counts charaters present in total
# if pattern to replace don't find, it don't change
print(my_string.replace("lot of a", "NO"))
print(my_string.replace("lot of", "NO"))

# here is lot of white   space
list_from_string = my_string.split()
print(list_from_string)  # delimiter used by default is space
# ['here', 'is', 'lot', 'of', 'white', 'space']

list_from_string = my_string.split(",")
print(list_from_string)
# ['here is lot of white   space']

# list_from_string = my_string.split("")
print(list_from_string)
# ValueError: empty separator

string_from_list = "".join(my_string)
print(string_from_list)  # here is lot of white   space
# ['here', 'is', 'lot', 'of', 'white', 'space']
list_from_string = my_string.split()
string_from_list = "".join(list_from_string)
print(string_from_list)  # hereislotofwhitespace

string_from_list = ".".join(list_from_string)  # puts . between each element
# here.is.lot.of.white.space
print(string_from_list)
string_from_list = ".".join(my_string)  # if you pass string in place of list
# h.e.r.e. .i.s. .l.o.t. .o.f. .w.h.i.t.e. . . .s.p.a.c.e


string_from_list = " ".join(list_from_string)  # puts . between each element
# JOIN: Concatenate any number of strings. The string whose method is called is inserted in between each given string. The result is returned as a new string.

print(string_from_list)  # here is lot of white space

my_list = ['a'] * 40
# print(my_list)

start = timer()
# a bad and expensive method to create string from this list
new_string = ""
for i in my_list:
    new_string += i
stop = timer()
print(stop-start)
# print(new_string)

# convert list ['a', 'a', 'a', 'a'] into string : aaaa
# because string is immutable, it every time creates a new string for concatanation
# hence join method is used.
start = timer()
new_string = "".join(my_list)
stop = timer()
print(stop-start)
# print(new_string)  # aaaa

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
#[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]

# other use of MAP
# Return double of n


def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
[2, 4, 6, 8]
# OR
# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


# FORMATTING A STRING
# by %, format() or f-string

var = "Tom"
my_string = "the variable is %s" % var
print(my_string)
# use %f for float, %.2f (2 digit after float)

var = 3.44
my_string = "the variable is {}".format(var)
print(my_string)

var1 = "a"
var2 = 32
my_string = "the variable is {}, {}".format(var1, var2)
print(my_string)
my_string = f"the variable is {var1} and {var2}"
my_string = f"the variable is {var1*22} and {var2}"  # can do operations
print(my_string)


print("_____________________________________________________")

print("COLLECTIONS IN PYTHON")

# Collectors: Counter, namedtuple, orderedDict, defaultdict, deque

# counter is the container that stores Elements which are
# stored as dictionary keys
# and their counts are stored as dictionary values.

a = "aaabbbbccccc"
my_counter = Counter(a)
print(my_counter)  # Counter({'c': 5, 'b': 4, 'a': 3})
print(my_counter.items())
print(my_counter.keys())  # dict_keys(['a', 'b', 'c'])
print(my_counter.values())  # dict_values([3, 4, 5]) <class 'dict_values'>
#dict_items([('a', 3), ('b', 4), ('c', 5)])
print(my_counter.most_common(1))  # [('c', 5)]

# gives 2 most common types [('c', 5), ('b', 4)]
print(my_counter.most_common(2))
print(my_counter.most_common(2)[0])  # ('c', 5)<class 'tuple'>
print(my_counter.most_common(2)[0][0])  # c  <str>
# a = "aaabbbbccccc" then we created my_counter from it and now list


# to create a list from COUNTER
print(my_counter.elements())  # <itertools.chain object at 0x7f7f82b3efd0>
# Iterator over elements repeating each as many times as its count.
print(list(my_counter.elements()))
#['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']

# Returns a new subclass of tuple with named fields.
Point = namedtuple('Point', 'x, y')
# now you can create your own Point
pt = Point(1, -4)
print(pt)  # Point(x=1, y=-4) its type is <class '__main__.Point'>

print(pt.x, pt.y)  # 1, -4

# after python 3.7 even regular dict remembers order, so it became less important now

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)  # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

ordered_dict = {}  # even simple dict also remembers the order
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['c'])  # it gives 0, because 0 is default value of int

d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d)  # defaultdict(<class 'float'>, {'a': 1, 'b': 2})
print(d['c'])  # it gives 0.0, because 0.0 is default value of float
# in normal dictionary this accessing of element which do not exist would have raised key error.

# double ended queue

d = deque()
d.append(1)
d.append(3)
d.appendleft(94)
print(d)  # deque([94, 1, 3])

d.pop()
print(d)  # deque([94, 1])

d.popleft()
print(d)  # deque([1])

d.clear()
d.extend([4, 5, 3])
print(d)  # deque([4, 5, 3])
d.extendleft([1, 2, 33])
print(d)  # deque([33, 2, 1, 4, 5, 3])


d.rotate(1)  # rotate 1 place right
print(d)  # deque([3, 33, 2, 1, 4, 5])

d.rotate(-1)
print(d)  # deque([3, 33, 2, 1, 4, 5])

# itertools


#from itertools import product, permutations
a = [2, 3]
b = [1, 4]

prod = product(a, b)
print((prod))  # <itertools.product object at 0x7fc6ef947740>
# convert it to a list
print(list(prod))  # [(2, 1), (2, 4), (3, 1), (3, 4)]

prod = product(a, b, repeat=2)
# print(list(prod))
perm = permutations([1, 2, 3])
print(list(perm))
#[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# to get permutation of length 2 only
perm = permutations([1, 2, 3], 2)
print(perm)  # <itertools.permutations object at 0x7fae8d33c8b0>
print(list(perm))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
