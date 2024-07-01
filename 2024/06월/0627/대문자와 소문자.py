# 파이썬 

def solution(my_string):
    answer = ''
    for i in my_string:
        # i가 대문자일때
        if i.isupper():
            # 소문자 출력
            answer += i.lower()
        else:
            # 대문자 출력
            answer += i.upper()
    return answer