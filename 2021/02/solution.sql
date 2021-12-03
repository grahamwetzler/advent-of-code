create table aoc.input_2021.input_02 (
  direction text,
  units integer
);

with input as (
    select *
    from aoc.input_2021.input_02
)

, negated as (
  select   case
           when direction in ('up', 'down') then 'depth'
           when direction in ('forward') then 'horizontal'
            end as net_direction,
         , case
           when direction = 'up' then units * -1
           else units
            end as units
    from input
)

, agg as (
  select   net_direction
         , sum(units) as total
    from negated
   group by 1
)

, part_1 as (
  select exp(sum(ln(total))) as answer -- why does SQL not have a product aggregate function!?
    from agg
)

, answer as (
  select   'part 1' as part
         , answer
    from part_1
)

select *
  from answer
