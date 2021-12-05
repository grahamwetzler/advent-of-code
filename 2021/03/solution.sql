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
  , b1 integer
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

, input_sample as (
  select *
    from aoc.input_2021.day_03_sample
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

, counts as (
  select    count_if(b1 = 1) as b1_1
          , count_if(b1 = 0) as b1_0
          , count_if(b2 = 1) as b2_1
          , count_if(b2 = 0) as b2_0
          , count_if(b3 = 1) as b3_1
          , count_if(b3 = 0) as b3_0
          , count_if(b4 = 1) as b4_1
          , count_if(b4 = 0) as b4_0
          , count_if(b5 = 1) as b5_1
          , count_if(b5 = 0) as b5_0
    from input_sample
)

, bit_ranks as (
  select 1
)

, oxygen_generator_rating as (
  select   *
    from input_sample
   where b1 = (select b1  from input group by 1 order by count(*) desc limit 1)
)

select *
  from oxygen_generator_rating
