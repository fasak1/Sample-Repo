import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
greeting = "Hello, {}".format(who_to_greet)
return greeting


# print(greet('World'))
# print(greet('Sandeep'))

r = requests.get("https://coreyms.com")
print(r.status_code)

name = input("Your name? ")
print("Hello,", name)

