def solution(money):
    # money // 5500 으로 나눴을때 횟수
    # money % 5500 나머지 값이 조건 맞을때까지
    # 반복적으로 나누고 나머지값 출력
    return [money // 5500, money % 5500]