"""
This is templates for frequently used built-in modules.
"""

"""
Basic built-in types & libs
"""
list, dict, set, tuple


from collections import Counter
from collections import defaultdict

# call basic operators as functions
from operator import truediv, mul, add, sub

sorted(iterable, key=lambda x: x, reversed=True)

# pretty print
import pprint
pp = pprint.PrettyPrinter()


# namedtuple asign meaning to each position, it is more readable.
from collections import namedtuple


# create a new type. pass in the new type name and field names
Book = namedtuple('Book', 'author title genre year price instock')

# create namedtuple instance.
book = Book('Suzane Collins','The Hunger Games', 'Fiction', 2008, 6.96, 20),

# namedtuple is immutable. _replace() method creates a new namedtuple.
book._replace(author='Adam Smith')

# useful when using csv & sqlite. just pass tuples to ._make() method
import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print emp.name, emp.title

import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print emp.name, emp.title


"""
breakpoint / debug
"""
# <= python 3.6
import pdb
pdb.set_trace()

# >= python 3.7, just use this:
breakpoint()


"""
Functional programming
"""
# map(function, iterable): apply function to each element of iterable.

def add_one(x):
    return x+1
elems = [1,2,3]
x = map(add_one, elems)  # returns a map object.

# but this is equivalent to writing:
x = (add_one(el) for el in elems)
# or:
x = [add_one(el) for el in elems]

# so for map(), let's stick to genrator syntax.

# filter(function, iterable): keep elements that the function returns True.
# but equivalent to:
x = [el for el in elems if should_keep(el)]

# reduce(function, iterable): return a single value for the iterable. 


"""
logging
"""
import logging

# Best practice: create a Logger object, instead of directly 
# using logging module. Especially when the program has multiple 
# modules, so we know which module emitted the record.

# Inside each module, set the logger's name to __name__
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# remember a Logger object can have multiple Handlers.
# if writing log to console
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
logger_format = logging.Formatter('%(levelname)s (%(name)s) : %(message)s')
handler.setFormatter(logger_format)
logger.addHandler(handler)

# if writing log to file
handler = logging.FileHandler('file.log')
handler.setLevel(logging.ERROR)
logger_format = logging.Formatter('%(asctime)s| %(name)s | %(levelname)s: %(message)s')
handler.setFormatter(logger_format)
logger.addHandler(handler)


# debug, info, warning, error, critical
logging.error("Exception occurred", exc_info=True)


# we can even load logger configurations from file.
#logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)


"""
itertools
"""

# flatten a nested list
