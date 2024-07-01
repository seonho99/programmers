# MySQL
# 2. 판매 중인 상품 중 가장 높은 판매가 
# 2. 컬럼명은 MAX_PRICE
SELECT MAX(PRICE) MAX_PRICE
# 1. 테이블
FROM PRODUCT
# 3. 가장 높은 판매가 
LIMIT 1;