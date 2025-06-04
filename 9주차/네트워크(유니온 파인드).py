# 경로 압축을 적용한 find 함수
def find(parent, x):
    # x의 부모 노드가 자기 자신이 아니라면, 루트 노드까지 재귀적으로 올라가서 갱신
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 노드를 하나의 집합으로 합치는 union 함수
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    # 루트 노드가 더 작은 값이 되도록 병합
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

# 네트워크 개수를 계산하는 메인 함수
def solution(n, computers):
    # 초기 부모 테이블 구성 (1-based 인덱스를 위해 크기 n+1)
    parent = [i for i in range(n + 1)]

    # 2차원 연결 행렬을 통해 연결된 컴퓨터 쌍을 찾아 union 수행
    for i in range(n):
        for j in range(n):
            if i == j:
                continue  # 자기 자신과의 연결은 무시
            if computers[i][j] == 1:  # 연결되어 있다면
                union(parent, i + 1, j + 1)
                print(f"Union: 컴퓨터 {i+1} - {j+1}")

    # 디버깅용: 최종 부모 테이블 확인
    print("최종 parent 배열:", parent)

    # 각 컴퓨터의 루트 노드를 찾아 고유 네트워크 수 계산
    maps = {}
    for idx in range(1, len(parent)):
        root = find(parent, parent[idx])  # 해당 노드의 루트 찾기
        if root not in maps:
            maps[root] = 1  # 새로운 네트워크로 등록

    print("각 컴퓨터의 루트:", [find(parent, i) for i in range(1, len(parent))])
    print("고유 네트워크 루트:", list(maps.keys()))

    # 네트워크 개수 반환
    return len(maps)

    print("연결 된 네트워크 수", solution(n, computers))
