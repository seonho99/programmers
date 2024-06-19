# 파이썬
def solution(n):
    # 3. 0으로 지정
    answer = 0
    # 1. n의 1:자신까지 i에 입력  
    for i in range(1,n+1):
        # 2. n을 i로 나눴을때 (곱했을때) 0일때
        if n % i == 0:
            # 3. 조건에 맞는 순서쌍을 하나씩 더한다
            answer = answer+1
    return answer