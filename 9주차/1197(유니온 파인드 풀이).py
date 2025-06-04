import sys
input = sys.stdin.readline()

# 서로소 집합 (Union-Find)을 위한 함수 정의

# 특정 원소가 속한 집합을 찾는 함수 (경로 압축 사용)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 재귀적으로 루트 노드 찾기 및 경로 압축
    return parent[x]

# 두 집합을 합치는 함수 (작은 번호 기준으로 루트 병합)
def union_parent(parent, a, b):
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)
    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root

# 정점(V), 간선(E) 입력 받기
V, E = map(int, input().split())  # V: 정점 개수, E: 간선 개수

# 부모 테이블 초기화 (자기 자신이 부모)
parent = [i for i in range(V + 1)]

# 간선 정보를 담을 리스트
edges = []

# 모든 간선 정보 입력 받기
for _ in range(E):
    a, b, cost = map(int, input().split())  # 정점 a, 정점 b, 간선의 가중치 cost
    edges.append((cost, a, b))  # cost 기준으로 정렬하기 위해 cost를 제일 앞에 저장

# 간선 리스트를 가중치 기준으로 오름차순 정렬
edges.sort()

# MST 구성 시 총 가중치 합
total_cost = 0

# 간선들을 하나씩 확인하며 MST를 구성
for cost, a, b in edges:
    # 사이클이 발생하지 않는 경우 (두 정점이 서로 다른 집합에 속할 경우)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)  # 두 정점을 연결 (집합 병합)
        total_cost += cost         # 해당 간선의 가중치를 결과에 더함

# 최종적으로 구한 최소 스패닝 트리의 총 비용 출력
print(total_cost)
