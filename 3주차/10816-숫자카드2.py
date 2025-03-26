import sys
input = sys.stdin.readline

n = int(input())
sangen = sorted(list(map(int, input().split())))
m = int(input())
cards = list(map(int, input().split()))

dic1 = {}
for x in sangen:
    if x in dic1:
        dic1[x] += 1
    else:
        dic1[x] = 1
for element in cards:
    if element in dic1:
        print(dic1[element], end='')
    else:
        print(0, end='')

