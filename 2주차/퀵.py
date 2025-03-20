# 퀵정렬
# 알고리즘
# 구현

array = [5, 7, 4, 6, 2, 1, 3, 0]  # 정렬할 배열

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개 이하이면 정렬할 필요 없음
        return

    pivot = start  # 피벗을 첫 번째 원소로 설정
    left = start + 1  # 왼쪽 포인터 (피벗 다음 위치)
    right = end  # 오른쪽 포인터 (배열 끝 위치)

    # 왼쪽과 오른쪽이 교차하기 전까지 반복
    while left <= right:
        # 피벗보다 큰 값을 찾을 때까지 left 이동
        while left <= end and array[left] <= array[pivot]:
            left += 1
            # 피벗보다 작은 값을 찾을 때까지 right 이동5
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 포인터가 엇갈린 경우 (작은 값과 피벗 교체)
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 값과 큰 값을 교체
            array[left], array[right] = array[right], array[left]

    # 분할 후, 왼쪽과 오른쪽을 각각 정렬
    quick_sort(array, start, right - 1)  # 왼쪽 부분 정렬
    quick_sort(array, right + 1, end)  # 오른쪽 부분 정렬
    print(right, left)
quick_sort(array,0, len(array) - 1)
print(array)