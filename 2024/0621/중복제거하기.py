# MySQL
# 출력값 
# 5. 서브쿼리의 행의 갯수 
SELECT COUNT(*) AS count
FROM(
    # 2. 동물의 이름
    SELECT NAME
    # 1. 테이블 이름
    FROM ANIMAL_INS
    # 3. 이름이 없는 경우는 제외
    WHERE NAME IS NOT NULL
    # 4. 이름 그룹화
    GROUP BY NAME
# 참조 할수 있는 쿼리 지정
) AS UNIQUE_NAME;