## Set up project folder and .venv; write hello.py; print name, goal and today's date.
import datetime

print("Pramod")
print("Goal is to learn AI/ML")
print(datetime.datetime.now())

## Data types , Variables

name = "Pramod" ## this is string
number = 100
numberfloat = 100.00
print(name , number , numberfloat)

isFlag = True
x = 1j
b = b'abcb'
print(b)
print(x)

print(type(name))
print(type(number))
print(type(isFlag))
print(type(numberfloat))

z = {}
print(type(z))

list1 = list((1,2,3,4))
print(list1)

tuple1 = (1,2,3,4)
print(tuple1)

set1 = {1, 2, 3, 4}
set2 = set((1,2,3,4))
print(set1)
print(set2)

dict1 = dict(name="john" , age=36)
print(dict1)
xbool = bool(0)
print(xbool)

xbytes = bytes(5)
print(xbytes)
x = bytearray(5)
print(x)


# Creating bytes directly
data = b"Hello"
print(type(data))  # <class 'bytes'>
print(data[0])     # 72 (the ASCII number for 'H')
print(data[1])

def calculateBMI(height, weight):
    return height / weight / 100
