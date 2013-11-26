import sys


metric = {"kg": 2.2046, "lb":0.4536, "g": 3.7854, "l":0.2642}
metric2 = {"kg": "lb", "lb":"kg", "g": "l", "l":"g"}
rl = lambda : sys.stdin.readline()
n = int(rl())

for j in range(n):
    num , string =rl().split(" ")
    string = string.replace("\n","")
    s = "{:.4f}".format(float(num)*metric[string])
    print "%s %s  %s" % (j+1,s ,metric2[string])

