def solution(array):

    answer = [] # 입력한 답을 초기화 해준다.
    answer.append(array[0]) # 입력 받을 스택구조를 활용하여 0부터 9까지 반환
    len = array[0]

    for i in array:
       if i != len:
           answer.append(i) # 입력 받은 데이터 i를 반환
           len = i
    return answer