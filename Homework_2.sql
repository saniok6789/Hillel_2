-- SQL-скрипт для вибірки даних з таблиці Student_Grades

-- Встановлюємо використання бази даних
USE StudentGradesDB;

-- Відображення всієї інформації з таблиці Student_Grades
SELECT * FROM Student_Grades;

-- Відображення ПІБ усіх студентів
SELECT full_name FROM Student_Grades;

-- Відображення усіх середніх оцінок
SELECT avg_year_grade FROM Student_Grades;

-- Показати країни студентів (унікальні значення)
SELECT DISTINCT country FROM Student_Grades;

-- Показати міста студентів (унікальні значення)
SELECT DISTINCT city FROM Student_Grades;

-- Показати назви груп (унікальні значення)
SELECT DISTINCT group_name FROM Student_Grades;

-- Кінець SQL-скрипта
