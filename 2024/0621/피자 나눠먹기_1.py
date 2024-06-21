# 피자 한판에 7 조각
def solution(n):
    answer = 0
    # n이 7의 배수라면
    if n % 7 == 0:
        # 7로 나눈 n의 값을 answer로 반환
        answer = n // 7
    # 7의 배수가 아닐때
    elif n % 7 != 0:
        # 연산자 //는 정수만 반환
        answer = n // 7 + 1
    return answer