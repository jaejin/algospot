import sys
import urllib


rl = lambda : sys.stdin.readline()
n = int(rl())

for j in range(n) :
    s = rl().replace("\n","")
    print urllib.unquote(s)
    
