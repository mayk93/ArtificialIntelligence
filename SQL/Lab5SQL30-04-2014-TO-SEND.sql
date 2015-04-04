/* Lab 5 Ex 2
select department_name, job_title, round(avg(salary),2),
grouping(department_name), grouping(job_title)
from departments join employees using(department_id)
join jobs using (job_id)
group by cube (department_name,job_title);
*/

/* Lab 5 Ex 2
select department_name, job_title, round(avg(salary),2),
grouping(department_name), grouping(job_title)
from departments join employees using(department_id)
join jobs using (job_id)
group by cube (department_name,job_title);
*/

/* Lab 5 Ex 1
select department_name, job_title, round(avg(salary),2),
grouping(department_name), grouping(job_title)
from departments join employees using(department_id)
join jobs using (job_id)
group by rollup (department_name,job_title);

select department_name, job_title, round(avg(salary),2)
from departments join employees using(department_id)
join jobs using (job_id)
group by rollup (department_name,job_title);

select department_name, job_title, round(avg(salary)), 2
from departments join employees using(department_id)
join jobs using (job_id)
group by rollup (department_name,job_title);
*/

/* Lab 5 Ex 3
select department_name, job_title, employees.manager_id, max(salary), sum(salary)
from departments join employees using (department_id)
join jobs using (job_id)
group by grouping sets ( (department_name, job_title) , (job_title, employees.manager_id) , () );
*/

/* Lab 5 Ex 4
select max(salary)
from employees
having max(salary)>15000
*/

/* Lab 5 Ex 5
select employee_id, salary, department_name, medie, ang
from employees e1 join departments on (departments.department_id = e1.department_id) join
(select avg(salary) medie , count(employee_id) ang, department_id
  from employees
  group by department_id) nume on (nume.department_id = e1.department_id)
where salary > (select round(avg(salary))
                from employees
                where department_id = e1.department_id)              
*/

/* Lab 5 Ex 6 V1
select last_name, salary
from employees
where salary > all( 
select round(avg(salary),2)
from employees
group by department_id
)
*/

/* Lab 5 Ex 6 V2
select last_name, salary
from employees
where salary > ( 
select max(round(avg(salary),2))
from employees
group by department_id
)
*/

/* Lab 5 Ex 7 V1
select last_name, salary
from employees join 
(
select department_id, min(salary) minSal
from employees
group by department_id
)
using (department_id)
where salary = minSal
*/

/* Lab 5 Ex 7 V2
select last_name, salary
from employees e1
where salary = ( select min(salary) from employees e2 where e1.department_id = e2.department_id )
*/

/* Lab 5 Ex 7 V3
select last_name, salary
from employees
where (salary,department_id) in ( select min(salary),department_id from employees group by department_id )
*/

/* Lab 6 Ex 4 - Mine, No work
select country_id , ang 
from employees e1 join departments d1 on (e1.department_id = d1.department_id) join locations l1 on ( d1.location_id = l1.location_id ) join 
( select count(employee_id) ang, country_id c1
from employees e2 join departments d2 on (e2.department_id = d2.department_id)
where d2.location_id = d1.location_id )
on (l1.country_id = c1)
*/

/* Lab 6 Ex 4 - Work
select country_id, count(employee_id)
from employees right join departments using (department_id) right join locations using (location_id) right join countries using (country_id)
group by country_id
*/

/* Lab 5 Ex 12 - In 5 words
select distinct location_id
from departments
*/

/* Lab 5 Ex 12 - Exists
select location_id
from locations l
where exists ( select 'x' from departments where location_id = l.location_id )
*/

/* Lab 5 Ex 8
select last_name, hire_date
from employees e join departments d on (e.department_id = d.department_id)
where hire_date  = ( select min(hire_date) from employees where department_id = d.department_id )
order by department_name
*/

/* Lab 5 Ex 9
select last_name, department_id
from employees e
where exists 
( 
  select employee_id
  from employees
  where department_id = e.department_id
  and
  salary = 
  (
    select max(salary)
    from employees
    where department_id = 30
  )
)
*/

/* Lab 5 Ex 10
select last_name, salary
from employees x
where (select count(employee_id) from employees where salary>x.salary ) < 3
*/

/* Exemplu rownum 1
select job_id, rownum
from jobs
*/

/* Exemplu rownum 2
select job_id, rownum
from jobs
where rownum < 5
*/

/* Lab 5 Ex 21 - Exemplu rezolvare gresita
select employee_id
from employees
where rownum < 11
order by salary
*/

/* Lab 5 Ex 22 - Corect
select employee_id
from 
(
  select *
  from employees
  order by salary desc
)
where rownum < 11
*/

/* Lab 5 Ex 22
select *
from 
(
  select job_id, avg(salary)
  from employees
  group by job_id
  order by 2
)
where rownum < 4
*/

/* Lab 5 Ex 11
select employee_id, last_name, first_name
from employees e
where 
( 
select count(employee_id)
from employees
where manager_id = e.employee_id
)>1
*/

/* Lab 5 Ex 14 Point A
select employee_id, last_name, first_name, hire_date, salary, manager_id
from employees
where manager_id = ( select employee_id from employees  where lower(last_name) = 'de haan' )
*/

/* Lab 5 Ex 14 Point B
select employee_id, last_name, first_name, hire_date, salary, manager_id, level
from employees
start with manager_id = ( select employee_id from employees  where lower(last_name) = 'de haan' )
connect by prior manager_id = employee_id 
*/

/* Lab 5 Ex 15
select employee_id, last_name, first_name, hire_date, salary, manager_id, level
from employees
start with manager_id = 114
connect by prior manager_id = prior employee_id
*/

/* Lab 5 Ex 16
select employee_id, last_name, first_name, hire_date, salary, manager_id, level
from employees
where level = 2
start with manager_id = ( select employee_id from employees  where lower(last_name) = 'de haan' )
connect by manager_id = prior employee_id 
*/

/* Lab 5 Ex 17
select employee_id, manager_id, level, last_name
from employees
connect by employee_id = prior manager_id
order by 1
*/

/* Lab 5 Ex 18
select employee_id, last_name, salary, level ,manager_id
from employees
where salary > 5000
start with salary=
(
  select max(salary)
  from employees
)
connect by manager_id = prior employee_id
*/

/* Lab 5 Ex 19
with 
dep_sum as
(
  select department_id, sum(salary) suma
  from employees
  group by department_id
),
sum_max as
(
  select avg(suma) maxim
  from dep_sum
)

select department_name, suma
from departments join dep_sum using (department_id)
where suma > ( select maxim from sum_max )
*/

/* Lab 5 Ex 20
with k_sub as
(
  select employee_id, hire_date
  from employees
  where manager_id = ( select employee_id
                       from employees
                       where lower(last_name||first_name)='kingsteven')),
k_old as ( select employee_id
           from k_sub
           where hire_date = (select min(hire_date) from k_sub))
           
select employee_id , last_name||first_name, job_id, hire_date
from employees
where to_char(hire_date,'yyyy')<>1970
start with employee_id in (select employee_id from k_old)
connect by prior employee_id = manager_id
*/

/*
TEMA

La 25 se facem cu decode
La 26 se poate rezolva doar cu case
*/