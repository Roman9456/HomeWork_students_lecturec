# Educational System

## English

### Description
This project is a part of an educational system that includes functionality for managing students, mentors, and lecturers. It provides methods for rating homework, calculating average grades, and calculating average lecturer ratings.

### Features
- rate_hw(self, student, course, grade): Allows a mentor to rate a student's homework for a specific course.
- __str__(self): Provides a string representation of a mentor's name and the courses they teach.
- get_course_grades(students, course_name): Calculates the average grade for a given course across a list of students.
- get_course_lecturers_avg_rating(lecturers, course_name): Calculates the average rating for lecturers of a given course.

### Usage
1. Create a Student object.
2. Create a Mentor object and attach courses to it.
3. Create Lecturer objects and add ratings to them.
4. Use the provided functions to calculate the average grade and average rating for a specific course.

## Russian

### Описание
Этот проект является частью образовательной системы, которая включает в себя функциональность для управления студентами, наставниками и лекторами. Она предоставляет методы для оценки домашних заданий, расчета средних оценок и расчета средних рейтингов лекторов.

### Возможности
- rate_hw(self, student, course, grade): Позволяет наставнику оценить домашнее задание студента для определенного курса.
- __str__(self): Предоставляет строковое представление имени наставника и преподаваемых им курсов.
- get_course_grades(students, course_name): Рассчитывает среднюю оценку для данного курса среди списка студентов.
- get_course_lecturers_avg_rating(lecturers, course_name): Рассчитывает средний рейтинг лекторов данного курса.

### Использование
1. Создайте объект Student.
2. Создайте объект Mentor и прикрепите к нему курсы.
3. Создайте объекты Lecturer и добавьте к ним рейтинги.
4. Используйте предоставленные функции для расчета средней оценки и среднего рейтинга для определенного курса.
