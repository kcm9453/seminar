import sys
input = lambda: sys.stdin.readline().rstrip()  # 빠른 입력을 위한 람다 함수 정의

# 정점(V) 수와 간선(E) 수 입력
V, E = map(int, input().split())

# 간선 정보를 저장할 리스트
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())  # A와 B는 연결된 두 정점, C는 가중치
    edges.append((A, B, C))              # (정점 A, 정점 B, 가중치 C)를 튜플로 저장

# 간선 리스트를 가중치(C)를 기준으로 오름차순 정렬
edges.sort(key=lambda x: x[2])  # 최소 가중치부터 MST에 포함시키기 위함

# -----------------------------
# Union-Find(서로소 집합) 구현
# -----------------------------

# 각 정점의 부모 노드를 자기 자신으로 초기화 (1-based 인덱스)
parent = [i for i in range(V + 1)]

# 특정 원소의 루트(parent)를 찾는 함수 (경로 압축 적용)
def get_parent(x):
    if parent[x] == x:        # 자기 자신이 루트라면 그대로 반환
        return x
    parent[x] = get_parent(parent[x])  # 재귀적으로 루트까지 찾아가면서 경로 압축
    return parent[x]

# 두 원소가 속한 집합을 합치는 함수
def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    # 번호가 더 작은 루트를 부모로 정함 (일관성 유지)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 두 원소가 같은 집합에 속하는지 확인하는 함수
def same_parent(a, b):
    return get_parent(a) == get_parent(b)

# -----------------------------
# 크루스칼 알고리즘 실행
# -----------------------------

answer = 0  # 최소 스패닝 트리의 총 비용 (최종 결과)

# 정렬된 간선을 하나씩 확인
for a, b, cost in edges:
    # 현재 간선을 연결했을 때 사이클이 발생하지 않는다면 (== 서로 다른 집합이라면)
    if not same_parent(a, b):
        union_parent(a, b)  # 두 정점을 연결 (집합 병합)
        answer += cost      # 해당 간선의 비용을 누적

# 최종적으로 모든 정점을 연결한 최소 비용 출력
print(answer)
