# 파이썬
def solution(start_num, end_num):
    answer = []
    # range end에 자신의 숫자 +1 을 해야함
    for i in range(start_num,end_num+1):
        answer.append(i)
    return answer