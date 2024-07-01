# 파이썬
def solution(num_list, n):
    for i in num_list:
        # 맞으면 1 틀리면 0 바로 출력
        if i == n:
            return 1
    return 0