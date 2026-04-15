--- Consecutive Numbers

select distinct first as ConsecutiveNums
from (
    select num as first, 
    lead(num, 1) over(order by id ) as next,
    lead(num, 2) over(order by id) as two_next
    from logs
) t
where first = next and first = two_next;
