from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # 이동 방향: 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문 여부 및 거리 기록용
    queue = deque()
    queue.append((0, 0, 1))  # (x좌표, y좌표, 시작거리)

    while queue:
        x, y, dist = queue.popleft()

        # 도착지점 도달 시
        if x == n - 1 and y == m - 1:
            return dist

        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    # 방문 처리 및 거리 증가
                    maps[nx][ny] = 0
                    queue.append((nx, ny, dist + 1))

    # 도달할 수 없는 경우
    return -1

n, m = map(int, input("지도 크기 (n m): ").split())
print("지도를 한 줄씩 입력하세요 (0 또는 1):")
maps = [list(map(int, input().split())) for _ in range(n)]

print("최단 거리:", solution(maps))