import sys

l_stack = list(sys.stdin.readline().strip())
r_stack = []

n = int(sys.stdin.readline().strip())

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'L':
        if len(l_stack) >= 1:
            r_stack.append(l_stack.pop())
    elif command[0] == 'D':
        if len(r_stack) >= 1:
            l_stack.append(r_stack.pop())
    elif command[0] == 'B':
        if len(l_stack) >= 1:
            l_stack.pop()

    elif command[0] == 'P':
        l_stack.append(command[1])

l_stack.extend(reversed(r_stack))
print(''.join(l_stack))