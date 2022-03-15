select s1.id as "id",
case when mod(s1.id, 2) = 0 then s3.student
      when (mod(s1.id, 2) = 1 and s2.student is not null) then s2.student
      else s1.student
      end as "student"
from seat s1 left join seat s2
on(s1.id = s2.id-1)
left join seat s3
on(s1.id = s3.id+1)
order by 1;