-- 코드를 입력하세요
WITH RECURSIVE TIMES as (
    SELECT  0 as HOUR
    UNION ALL
    SELECT  HOUR + 1
    FROM    TIMES
    WHERE   HOUR < 23
)

SELECT      TIMES.HOUR, IFNULL(ANIMAL.count, 0) as count
FROM        TIMES 
LEFT OUTER JOIN (
            SELECT      hour(DATETIME) as HOUR, count(DATETIME) as count
            FROM        ANIMAL_OUTS 
            GROUP BY    hour(DATETIME)
            ) as ANIMAL
ON          TIMES.HOUR = ANIMAL.HOUR
GROUP BY    TIMES.HOUR
order by    TIMES.HOUR asc