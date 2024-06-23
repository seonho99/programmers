# MySQL
# 3. COUNT(*) 조건에 맞는 행의 수
SELECT COUNT(*) AS USERS
# 1. 테이블
FROM USER_INFO
# 2. 나이 정보가 없는 회원
WHERE AGE IS NULL;