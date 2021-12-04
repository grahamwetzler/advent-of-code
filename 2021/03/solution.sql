create or replace function binary_to_number(a string)
  returns float
  language javascript
  as
  $$
    return parseInt(A, 2)
  $$
;

create table aoc.input_2021.day_03 (
    b1 integer
  , b2 integer
  , b3 integer
  , b4 integer
  , b5 integer
  , b6 integer
  , b7 integer
  , b8 integer
  , b9 integer
  , b10 integer
  , b11 integer
  , b12 integer
);

create table aoc.input_2021.day_03_sample (
    b1 integer
  , b2 integer
  , b3 integer
  , b4 integer
  , b5 integer
);


with input as (
  select *
    from aoc.input_2021.day_03
)

, gamma as (
  select binary_to_number(
              concat(
                (select b1  from input group by 1 order by count(*) desc limit 1)
              , (select b2  from input group by 1 order by count(*) desc limit 1)
              , (select b3  from input group by 1 order by count(*) desc limit 1)
              , (select b4  from input group by 1 order by count(*) desc limit 1)
              , (select b5  from input group by 1 order by count(*) desc limit 1)
              , (select b6  from input group by 1 order by count(*) desc limit 1)
              , (select b7  from input group by 1 order by count(*) desc limit 1)
              , (select b8  from input group by 1 order by count(*) desc limit 1)
              , (select b9  from input group by 1 order by count(*) desc limit 1)
              , (select b10 from input group by 1 order by count(*) desc limit 1)
              , (select b11 from input group by 1 order by count(*) desc limit 1)
              , (select b12 from input group by 1 order by count(*) desc limit 1)
                  )) as gamma
)

, epsilon as (
  select binary_to_number(
              concat(
                (select b1  from input group by 1 order by count(*) asc limit 1)
              , (select b2  from input group by 1 order by count(*) asc limit 1)
              , (select b3  from input group by 1 order by count(*) asc limit 1)
              , (select b4  from input group by 1 order by count(*) asc limit 1)
              , (select b5  from input group by 1 order by count(*) asc limit 1)
              , (select b6  from input group by 1 order by count(*) asc limit 1)
              , (select b7  from input group by 1 order by count(*) asc limit 1)
              , (select b8  from input group by 1 order by count(*) asc limit 1)
              , (select b9  from input group by 1 order by count(*) asc limit 1)
              , (select b10 from input group by 1 order by count(*) asc limit 1)
              , (select b11 from input group by 1 order by count(*) asc limit 1)
              , (select b12 from input group by 1 order by count(*) asc limit 1)
                  )) as epsilon
)

, part_1 as (
  select (select gamma
            from gamma) *
         (select epsilon
            from epsilon) as power_consumption
)

select *
  from part_1
