-- 코드를 입력하세요
SELECT hour(DATETIME), count(DATETIME)
FROM ANIMAL_OUTS
where hour(DATETIME) between 09 and 19
GROUP BY hour(DATETIME)
order by hour(DATETIME) asc