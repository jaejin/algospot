import sys

    
rl = lambda : sys.stdin.readline()
n = int(rl())

for j in range(n):
    count , string =rl().split(" ")
    print "%s %s" % (j+1, string[:int(count)-1]+string[int(count):])

