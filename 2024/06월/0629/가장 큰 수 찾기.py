# 파이썬
def solution(array):
    # array 중 가장 큰 수
    max1 = max(array)
    # array 가장 큰 수의 인덱스
    max2 = array.index(max1)
    return [max1, max2]