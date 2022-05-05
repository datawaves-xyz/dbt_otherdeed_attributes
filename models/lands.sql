
select * from
{{ ref("lands_0_10000")}}

union all

select * from
{{ ref("lands_10000_20000")}}

union all

select * from
{{ ref("lands_20000_30000")}}

union all

select * from
{{ ref("lands_30000_40000")}}

union all

select * from
{{ ref("lands_40000_50000")}}

union all

select * from
{{ ref("lands_50000_60000")}}

union all

select * from
{{ ref("lands_60000_70000")}}

union all

select * from
{{ ref("lands_70000_80000")}}

union all

select * from
{{ ref("lands_80000_90000")}}

union all

select * from
{{ ref("lands_90000_100000")}}
