import sys


import pip._vendor.requests


print(sys.version)


def f():
    test = 1


r = pip._vendor.requests.get('https://coreyms.com')
print(r.__str__)
