------------------------task1--------------------------------------
SELECT
  COUNT(job_id)
FROM
  pds.employees;
-------------------------------------------------------------------

------------------------task2--------------------------------------
SELECT
  AVG(salary),
  COUNT(first_name)
FROM
  pds.employees
WHERE
  department_id = 90;
-------------------------------------------------------------------

------------------------task3--------------------------------------
SELECT
  COUNT(DISTINCT job_id)
FROM
  pds.employees
-------------------------------------------------------------------

------------------------task4--------------------------------------
SELECT
  first_name,
  last_name,
  department_id
FROM
  pds.employees;
-------------------------------------------------------------------

------------------------task5--------------------------------------
SELECT
  first_name,
  last_name,
  job_id,
  department_id
FROM
  pds.employees
  JOIN pds.departments USING (department_id)
  JOIN pds.locations USING (location_id)
WHERE
  city = 'London';
-------------------------------------------------------------------