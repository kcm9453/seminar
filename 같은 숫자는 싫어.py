import sys
n = int(sys.stdin.readline())

answer = []

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
       if len(answer) == 0 or answer[-1] != command[1]:
           answer.append(command[1])

print(answer)