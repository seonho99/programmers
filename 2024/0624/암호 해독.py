def solution(cipher, code):
    answer = ''
    # 입력값의 길이 
    for i in range(len(cipher)):
        # range가 0부터 시작하므로 +1
        # code로 나눴을때 나머지가 0
        if (i + 1) % code == 0:
            # 조건에 맞는 ciper[i]를 answer에 더함
            answer += cipher[i] 
    return answer