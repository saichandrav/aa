-- Run these queries after executing csv_to_sql_pandas.py

SELECT *
FROM students;

SELECT course, AVG(marks) AS avg_marks
FROM students
GROUP BY course
ORDER BY avg_marks DESC;

SELECT name, marks
FROM students
WHERE marks >= 90
ORDER BY marks DESC;
