create table aoc.input_2021.input_01 (
  measurement integer
);

with input as (
  select   row_number() over (order by 1) as row_num
         , measurement
    from aoc.input_2021.input_01
)

, input_sample as (
select   row_number() over (order by 1) as row_num
       , value as measurement
  from table(flatten(array_construct(  199
                                     , 200
                                     , 208
                                     , 210
                                     , 200
                                     , 207
                                     , 240
                                     , 269
                                     , 260
                                     , 263)))
)

, part_1 as (
  select   measurement
         , lag(measurement) over (order by row_num) as previous_measurement
         , iff(measurement > previous_measurement, 1, 0) as increases
    from input
)

, part_2_step_1 as (
  select   row_num
         , measurement
         , sum(measurement) over (order by row_num
                                   rows between 2 preceding
                                    and current row) as previous_three_measurements
    from input
 qualify row_num >= 3
)

, part_2_step_2 as (
  select   *
         , lag(previous_three_measurements) over (order by row_num) as previous_group
         , iff(previous_three_measurements > previous_group, 1, 0) as increases
    from part_2_step_1
)

, answer as (
  select  'part 1' as part
         , sum(increases)
    from part_1
   union all
  select  'part 2' as part
         , sum(increases)
    from part_2_step_2
)

select *
  from answer
