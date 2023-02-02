''' ЛЕКЦІЯ 17

Завдання 1. Запит, щоб перерахувати кількість вакансій у таблиці employees.

SELECT COUNT(DISTINCT job_id)
FROM employees;

Відповідь MySQL:
19


Завдання 2. Запит, щоб отримати середню заробітну плату та
кількість працівників відділу 90.

SELECT ROUND(AVG(SALARY), 1), COUNT(*) JOB_ID
FROM employees WHERE DEPARTMENT_ID = 90
;

Відповідь MySQL:
19333.3	3


Завдання 3. Запит, щоб отримати кількість працівників з однаковою роботою.

SELECT JOB_ID, COUNT(*)
FROM employees
GROUP BY JOB_ID
;

Відповідь MySQL:
'AC_ACCOUNT	1
AC_MGR	1
AD_ASST	1
AD_PRES	1
AD_VP	2


Завдання 4. Запит, щоб знайти назву і код відділу, а також імена
та прізвища працівників цього відділу.

SELECT  D.DEPARTMENT_NAME, E.DEPARTMENT_ID,
E.FIRST_NAME, E.LAST_NAME
FROM employees E
JOIN departments D
ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
;

Відповідь MySQL:
'24000.00', '2100.00'


Завдання 5. Запит, щоб знайти імена та прізвища, роботу, ідентифікатор
відділу та імена співробітників, що працюють у Лондоні.

SELECT E.FIRST_NAME, E.LAST_NAME, E.JOB_ID, E.DEPARTMENT_ID, D.DEPARTMENT_NAME
FROM employees E
JOIN departments D
ON (E.DEPARTMENT_ID = D.DEPARTMENT_ID)
JOIN locations L ON
(D.LOCATION_ID = L.LOCATION_ID)
WHERE LOWER(L.City) = 'London'
;

Відповідь MySQL:
Susan	Mavris	HR_REP	40	Human Resources
'''
