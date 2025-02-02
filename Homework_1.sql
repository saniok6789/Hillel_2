-- Создание базы данных
CREATE DATABASE StudentGradesDB;
USE StudentGradesDB;

-- Создание таблицы "Student_Grades"
CREATE TABLE Student_Grades (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Уникальный идентификатор
    full_name VARCHAR(255) NOT NULL,    -- Полное имя студента
    city VARCHAR(100) NOT NULL,         -- Город
    country VARCHAR(100) NOT NULL,      -- Страна
    birth_date DATE NOT NULL,           -- Дата рождения
    email VARCHAR(255) UNIQUE NOT NULL, -- Электронная почта
    phone VARCHAR(20) NOT NULL,         -- Контактный телефон
    group_name VARCHAR(100) NOT NULL,   -- Название группы
    avg_year_grade DECIMAL(4,2) NOT NULL,  -- Средняя оценка за год
    min_subject VARCHAR(100) NOT NULL,  -- Предмет с минимальной оценкой
    max_subject VARCHAR(100) NOT NULL   -- Предмет с максимальной оценкой
);

-- Добавление записей в таблицу
INSERT INTO Student_Grades (full_name, city, country, birth_date, email, phone, group_name, avg_year_grade, min_subject, max_subject)
VALUES 
('Alex Pupkin', 'Odessa', 'Ua', '2002-02-12', 'Alex.pupkin@gmail.com', '+380981300900', 'Group A', 3.8, 'History', 'Physics'),
('Artem Maksimenko', 'Odessa', 'Ua', '2007-09-20', 'Artem.Maksimenko@gmail.com', '+380983141011', 'Group B', 4.2, 'Mathematics', 'Chemistry'),
('Michael Guk', 'Odessa', 'Ua', '2010-10-05', 'Michael.Guk@gmail.com', '+46712422815', 'Group C', 3.5, 'Biology', 'English');

-- Проверка данных в таблице
SELECT * FROM Student_Grades;
