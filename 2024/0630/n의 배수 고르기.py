# 파이썬
def solution(n, numlist):
    answer = []
    # numlist을 i로 하나씩 
    for i in numlist:
        # 하나씩 빼온 i 중 n으로 나눴을때 
        # 나머지가 0 인수를 answer에 추가
        if i % n == 0:
            answer.append(i)
    return answer