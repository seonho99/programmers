
# 높은 금액부터 할인
def solution(price):
    if price >= 500000:
        return price * 0.8 // 1
    # 할인 받는 금액이 소수점이 나올수 있으므로 // 1 로 소수점 이하는 버림 
    elif price >= 300000:
        return price * 0.9 // 1
    elif price >= 100000:
        return price * 0.95 // 1
    else:
        return price 
    