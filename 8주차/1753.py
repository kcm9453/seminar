import sys  # 표준 입력을 빠르게 받기 위해 sys 모듈을 임포트
import heapq  # 우선순위 큐(힙)를 사용하기 위해 heapq 모듈을 임포트

input = sys.stdin.readline  # 입력 속도를 빠르게 하기 위해 sys.stdin.readline을 사용

# 정점의 개수(V)와 간선의 개수(E)를 입력받음
V, E = map(int, input().split())
# 시작 정점 번호(K)를 입력받음
K = int(input())

# 각 정점마다 연결된 (목적지, 가중치) 정보를 담을 리스트를 초기화 (1번부터 V번까지)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())  # 간선 정보: 출발 정점 u, 도착 정점 v, 가중치 w
    graph[u].append((v, w))  # u 정점에서 v 정점으로 가는 가중치 w인 간선을 저장

# 무한대를 나타내는 값 (10억으로 설정, 최단 거리 초기화용)
INF = int(1e9)
# 최단 거리 테이블 (모든 정점까지의 최단거리를 무한대로 초기화)
distance = [INF] * (V + 1)


# 다익스트라 알고리즘 함수 정의 (시작 정점에서 출발)
def dijkstra(start):
    # 우선순위 큐(힙) 선언: (거리, 정점번호) 형태로 담을 예정
    heap = []

    # 시작 정점의 최단거리는 0으로 설정 (자기자신까지의 거리는 0)
    distance[start] = 0
    # 시작 정점을 힙에 삽입 (거리 0, 시작 정점번호)
    heapq.heappush(heap, (0, start))

    # 힙이 빌 때까지 반복 (힙에 있는 정점들은 아직 최단거리가 확정되지 않은 상태)
    while heap:
        # 힙에서 현재까지의 최단거리가 가장 짧은 정점 꺼내기
        dist, now = heapq.heappop(heap)

        # 이미 처리된 정점(더 짧은 경로로 갱신된 적이 있으면)이라면 무시
        if distance[now] < dist:
            continue  # 이 경우, 이미 더 짧은 경로로 방문했으므로 넘어감

        # 현재 정점(now)과 연결된 모든 인접 노드 탐색
        for next_node, weight in graph[now]:
            # 현재까지의 거리(dist) + 이 간선의 가중치(weight)를 더해 새로운 비용 계산
            new_cost = dist + weight

            # 만약 새로운 비용이 기존에 기록된 최단거리보다 짧으면 갱신
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost  # 최단거리 갱신
                # 갱신된 거리와 함께 인접 노드를 힙에 삽입
                heapq.heappush(heap, (new_cost, next_node))


# 시작 정점 K에서 다익스트라 알고리즘을 실행
dijkstra(K)

# 1번 정점부터 V번 정점까지 최단거리 출력
for i in range(1, V + 1):
    # 만약 최단거리가 무한대(INF)라면, 도달할 수 없는 정점이므로 "INF" 출력
    if distance[i] == INF:
        print("INF")
    else:
        # 도달할 수 있다면 최단거리 출력
        print(distance[i])
