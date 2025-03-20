# 내가 야매로 푼 K번째 수
def solution(array, commands):
    answer = []  # 결과를 저장할 리스트를 생성

    for i, j, k in commands:  # commands 리스트에 있는 각 (i, j, k)에 대해 반복
        # i부터 j까지 슬라이싱하여 배열을 부분 배열로 만듦 (i는 1-based index이므로 1을 빼서 사용)
        array = array[i - 1 : j]

        # 배열을 정렬하는 부분인데 코드가 잘못됨. 여기서는 그냥 'sort'가 아닌 정렬을 해야 함
        array = sort  # 이 부분에서 오류가 있음. 'sort'는 잘못된 변수 참조. 정렬하려면 sorted(array)로 수정해야 함.

        # k번째 수를 찾는 부분 (k도 1-based index이므로 k - 1로 접근)
        answer.append(array[k - 1])  # k번째 수를 결과 리스트에 추가

    return answer  # 결과 리스트 반환


# 프로그래머스 K번째 수 문제 풀이
def solution(array, commands):
    answer = []  # 결과를 저장할 빈 리스트 생성

    for command in commands:  # commands 리스트에서 각 (i, j, k) 값을 하나씩 반복
        i, j, k = command  # command에서 i, j, k 값을 각각 추출

        # 배열을 슬라이싱하여 i부터 j까지의 부분 배열을 생성
        # i는 1-based index이므로 i - 1을 사용해 슬라이싱
        sliced_array = array[i - 1: j]

        # 슬라이싱한 배열을 정렬하여 sorted_array에 저장
        sorted_array = sorted(sliced_array)

        # 정렬된 배열에서 k번째 수를 찾고 answer 리스트에 추가
        # k도 1-based index이므로 k - 1로 접근
        answer.append(sorted_array[k - 1])

    return answer  # 결과 리스트를 반환