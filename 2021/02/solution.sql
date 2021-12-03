create table aoc.input_2021.input_02 (
  direction text,
  units integer
);

with input as (
  select   row_number() over (order by 1) as row_num
         , *
    from aoc.input_2021.input_02
)

, part_1_step_1 as (
  select   case
           when direction in ('up', 'down') then 'depth'
           when direction in ('forward') then 'horizontal'
            end as net_direction
         , case
           when direction = 'up' then units * -1
           else units
            end as units
    from input
)

, part_1 as (
  select   net_direction
         , sum(units) as total
    from part_1_step_1
   group by 1
)

, part_2 as (
  select   direction
         , case
           when direction = 'down' then units
           when direction = 'up' then units * -1
            end as aim
         , case
           when direction = 'forward' then units
            end as horizontal_position
         , sum(aim) over (order by row_num) as current_aim
         , sum(horizontal_position) over (order by row_num) as current_horizontal_position
         , case
           when direction = 'forward' then current_aim * horizontal_position
            end as depth
    from input
)

, answer as (
  select   'part 1' as part
         , exp(sum(ln(total))) as answer /* why does SQL not have a product aggregate function!? */
    from part_1
   union all
  select   'part 2' as part
         , sum(depth) * max(current_horizontal_position) as answer
    from part_2
)

select *
  from answer
