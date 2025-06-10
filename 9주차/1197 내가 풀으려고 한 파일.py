import sys
input = sys.stdin.readline()

V, E = map(int,input().split()) # 정점(V)와 간선(E)듸 개수를 불러옴
parent = [i for i in range(V + 1)] # 부모 테이블(자기 자신을 초기화 해줌)

def parent_find(parent, x):
    if parent[x] != x:
        parent[x] = parent_find(parent, parent[x])
        return parent[x]

def union_find(parent, a, b):
    root_a = union_find(parent, a)
    root_b = union_find(parent, b)
    if root_a < root_b:
        parent[root_a] = b
    else:
        parent[root_b] = a

edges = [] # 간선의 개수를 리스트 안에 저장

for _ in range(E):
    a, b, cost = map(int,sys.stdin.readline().split())
    edges.append()

edges.sort()




