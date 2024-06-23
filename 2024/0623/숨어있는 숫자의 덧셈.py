# 파이썬 
def solution(my_string):
    answer = 0 
    for i in my_string:
        # 문자가 나오면 except로 pass 
        # 숫자가 나오면 answer에 더하기
        try:
            answer = answer + int(i)
        except:
            pass  
    return answer
    

