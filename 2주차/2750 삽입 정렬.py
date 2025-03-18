N = int(input()) # 정렬한 숫자의 개수를 입력받음
nums = [] # 숫자를 저장할 빈 리스트 생성

for _ in range(N): # 반복문을 통해 사용자로부터 n개의 숫자를 입력 받아 num 리스트에다가 저장
    nums.append(int(input()))

# Insert Sort
for i in range(1, len(nums)): # 두 번째 원소로부터 i = 1로 시작하여 리스트 끝까지 반복
    while (i > 0) and (nums[i] < nums[i - 1]): # 현재 숫자 num[i]가 이전 숫자 num[i-1]보다 작다면 자리를 교환함
        nums[i], nums[i - 1] = nums[i - 1], nums[i] # 이 부분이 실행되어 작은 숫자가 앞으로 이동하게됨

        i -= 1 # 실행되어 한 칸 더 왼쪽으로 이동하면서 계속 정렬 진행

for n in nums:
    print(n) # 정렬이 완료되면 리스트를 차례대로 출력해준다