-- 코드를 입력하세요
SELECT      CART_ID
FROM        CART_PRODUCTS
WHERE       CART_ID in (    SELECT  CART_ID
                            FROM    CART_PRODUCTS
                            WHERE   NAME = 'Yogurt'
            ) and NAME = 'Milk'
ORDER BY    CART_ID asc