class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.lecturers = []

    def add_student(self, student):
        self.students.append(student)

    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def get_students_avg_rating(self):
        ratings = []
        for student in self.students:
            ratings.extend(student.grades)
        return sum(ratings) / len(ratings)

    def get_lecturers_avg_rating(self):
        ratings = []
        for lecturer in self.lecturers:
            ratings.extend(lecturer.rating)
        return sum(ratings) / len(ratings)


class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        def add_course(self, course_name):
            self.courses_in_progress.append(course_name)

            def add_grade(self, course_name, grade):
                if course_name in self.courses_in_progress and isinstance(grade, int) and 1 <= grade <= 10:
                    if course_name in self.grades:
                        self.grades[course_name].append(grade)
                    else:
                        self.grades[course_name] = [grade]
                else:
                    return 'Ошибка'

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            lecturer.rate_lecture(self, course, grade)
        else:
            return 'Ошибка'

    def __str__(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        if len(grades) > 0:
            average_grade = round(sum(grades) / len(grades), 1)
        else:
            average_grade = 0
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'{super().__str__()}\nСредняя оценка за домашние задания: {average_grade}\n' \
               f'Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        else:
            return "Нельзя сравнить студента с объектом другого класса!"

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() <= other.get_average_grade()
        else:
            return "Нельзя сравнить студента с объектом другого класса!"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        else:
            return "Нельзя сравнить студента с объектом другого класса!"

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() != other.get_average_grade()
        else:
            return "Нельзя сравнить студента с объектом другого класса!"

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() > other.get_average_grade()
        else:
            return "Нельзя сравнить студента с объектом другого класса!"

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() >= other.get_average_grade()
        else:
            return "Нельзя сравнить студента с объектом другого класса!"

    def get_average_grade(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        if len(grades) > 0:
            return round(sum(grades) / len(grades), 1)
        else:
            return 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            lecturer.rate_lecture(self, course, grade)
        else:
            return 'Ошибка'

    def __str__(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        if len(grades) > 0:
            average_grade = round(sum(grades) / len(grades), 1)
        else:
            average_grade = 0
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'{super().__str__()}\nСредняя оценка за домашние задания: {average_grade}\n' \
               f'Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__() + '\nУчебные курсы: ' + ', '.join(self.courses_attached)


class Lecturer(Mentor):
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.rating = []

    def __str__(self):
        return f'Лектор {self.name} {self.surname} ({self.course})'

    def __lt__(self, other):
        return sum(self.rating) < sum(other.rating)

    def add_rating(self, rating):
        self.rating.append(rating)

    def get_avg_rating(self):
        return sum(self.rating) / len(self.rating)

    def __str__(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        if len(grades) > 0:
            average_grade = round(sum(grades) / len(grades), 1)
        else:
            average_grade = 0
        return f'{super().__str__()}\nСредняя оценка за лекции: {average_grade}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise ValueError('Нельзя сравнить Лектора с объектом другого класса!')
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise ValueError('Нельзя сравнить Лектора с объектом другого класса!')
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise ValueError('Нельзя сравнить Лектора с объектом другого класса!')
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise ValueError('Нельзя сравнить Лектора с объектом другого класса!')
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise ValueError('Нельзя сравнить Лектора с объектом другого класса!')
        return self.get_average_grade() > other.get_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise ValueError('Нельзя сравнить Лектора с объектом другого класса!')
        return self.get_average_grade() >= other.get_average_grade()

    def get_average_grade(self):
        grades = []
        for grade in self.grades.values():
            grades += grade
        if len(grades) > 0:
            return round(sum(grades) / len(grades), 1)
        else:
            return 0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses = ', '.join(self.courses_attached)
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Преподаватель курсов: {courses}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
def get_course_grades(students, course_name):
    print(f"Средняя оценка за домашние задания по курсу '{course_name}':")
    hw_grades = []
    for student in students:
        if course_name in student.grades:
            hw_grades += student.grades[course_name]
    if len(hw_grades) == 0:
        print('Нет оценок за домашние задания на данном курсе')
    else:
        avg_hw_grade = sum(hw_grades) / len(hw_grades)
        print(f'{avg_hw_grade:.2f}')
def get_course_lecturers_avg_rating(lecturers, course_name):
    print(f"Средняя оценка за лекции по курсу '{course_name}':")
    ratings = []
    for lecturer in lecturers:
        if course_name == lecturer.course:
            ratings.append(lecturer.get_avg_rating())
    if len(ratings) == 0:
        print('Нет лекторов на данном курсе')
    else:
        avg_rating = sum(ratings) / len(ratings)
        print(f'{avg_rating:.2f}')


lecturer1 = Lecturer('Lector', 'One', 'Python')
lecturer2 = Lecturer('Lector', 'Two', 'Python')

lecturer1.add_rating(9) #Добавил для проверки действительно среднего числа
lecturer1.add_rating(10)
lecturer2.add_rating(8)
lecturer2.add_rating(9)




get_course_lecturers_avg_rating([lecturer1, lecturer2], 'Python')


get_course_grades([best_student], 'Python')





