# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# how to import a core python module.

#core modules
import datetime 
#just importing the date then the time, but the second one you chain on must be on a second row.
from datetime import date 
# import time
# or
from time import time

# Pip module
from camelcase import CamelCase

today = date.today()
# timestamp = time.time()
timestamp = time()
# today = datetime.date.today()

#Makes every word start with an uppercase
c = CamelCase()

print(today)
print(timestamp)
# converts words first letter to uppercase # Hello There Big World Of Python from camelcase pip
print(c.hump('hello there big world of python'))

# installing pip3 install camelcase