import math
from time import sleep
import sys

def toBinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

if sys.argv < 1:
    recv_file = open(sys.argv[1], "rt")

file = open("word.txt", "r")
word = file.read()
print(f"string: {word}")
sleep(1)
print(toBinary(word))
