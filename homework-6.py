class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

        # завершенные курсы
        self.finished_courses = []

        # на обучении
        self.courses_in_progress = []

        # оценки по курсам
        self.grades = {}
        self.average_rating = 0
        self.rating_scale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.ratings_sum = 0
        self.ratings_number = 0
        self.comparison = ''

    def average(self):
        for grade in self.grades:
            self.ratings_sum += sum(self.grades[grade])
            self.ratings_number += len(self.grades[grade])
            self.average_rating = round(self.ratings_sum / self.ratings_number, 2)
        return self.average_rating

    # оценка лекции преподавателя
    def rate_lecture(self, student, lecturer, course, grade_lecture):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in student.courses_in_progress and grade_lecture in self.rating_scale:
            if course in lecturer.grades_lecture:
                lecturer.grades_lecture[course] += [grade_lecture]
            else:
                lecturer.grades_lecture[course] = [grade_lecture]
        else:
            return print('Оценка лекции введена некорректно. Пожалуста, перепроверье')

    def __lt__(self, other):
        if not isinstance(other, Student):
            comparison = 'Имя студента введено некорректно'
        else:
            if self.average_rating > other.average_rating:
                comparison = f'{other.name} {other.surname} учится хуже, чем {self.name} {self.surname}'
            elif self.average_rating < other.average_rating:
                comparison = f'{other.name} {other.surname} учится лучше, чем {self.name} {self.surname}'
            else:
                comparison = f'Студенты {self.name} {self.surname} и {other.name} {other.surname} одинаково успешны'
        return comparison

    def __str__(self):
        return f'Имя студента: {self.name}\n' \
               f'Фамилия студента: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
               f'Курсы в процессе изучения: {str(self.courses_in_progress)[1:-1]}\n' \
               f'Завершенные курсы: {str(self.finished_courses)[1:-1]}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        # читаемый курс
        self.courses_attached = []

        # оценки за лекции
        self.grades_lecture = {}
        self.average_rating_lecture = 0
        self.ratings_sum_lecture = 0
        self.ratings_number_lecture = 0
        self.comparison_lec = ''

    def average_lecture(self):
        for grade in self.grades_lecture:
            self.ratings_sum_lecture += sum(self.grades_lecture[grade])
            self.ratings_number_lecture += len(self.grades_lecture[grade])
            self.average_rating_lecture = round(self.ratings_sum_lecture / self.ratings_number_lecture, 2)
        return self.average_rating_lecture

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            comparison_lec = 'Имя студента введено некорректно'
        else:
            if self.average_rating_lecture > other.average_rating_lecture:
                comparison_lec = f'{other.name} {other.surname} преподает хуже, чем {self.name} {self.surname}'
            elif self.average_rating_lecture < other.average_rating_lecture:
                comparison_lec = f'{other.name} {other.surname} преподает лучше, чем {self.name} {self.surname}'
            else:
                comparison_lec = f'Студенты {self.name} {self.surname} и {other.name} {other.surname} одинаково успешны'
        return comparison_lec

    def __str__(self):
        return f'Имя лектора: {self.name}\n' \
               f'Фамилия лектора: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_rating_lecture}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating_scale = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __str__(self):
        return f'Имя проверяющего: {self.name}\n' \
               f'Фамилия проверяющего: {self.surname}'

    # оценка ДЗ у студента
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and grade in self.rating_scale:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Оценка задания введена некорректно. Пожалуста, перепроверье')


def average_course(student1, student2, course):
    rate_list = []
    average_rate = 0
    if isinstance(student1, Student) and isinstance(student2, Student) \
            and course in student1.courses_in_progress and course in student2.courses_in_progress:
        rate_list += [course]
        average_rate += round((sum(student1.grades[course]) + sum(student2.grades[course])) /
                              (len(student1.grades[course]) + len(student2.grades[course])), 2)
    return print(f'Средняя оценка студентов на курсе {course} равна {average_rate}')


def average_course_lecturers(lecturer1, lecturer2, course):
    rate_list = []
    average_rate = 0
    if isinstance(lecturer1, Lecturer) and isinstance(lecturer2, Lecturer) \
            and course in lecturer1.courses_attached and course in lecturer2.courses_attached:
        rate_list += [course]
        average_rate += round((sum(lecturer1.grades_lecture[course]) + sum(lecturer2.grades_lecture[course])) /
                              (len(lecturer1.grades_lecture[course]) + len(lecturer2.grades_lecture[course])), 2)
    return print(f'Средняя оценка лекторов на курсе {course} равна {average_rate}')


# информация о первом студенте
first_student = Student('Joe', 'Hill', 'male')
# текущие курсы первого студента
first_student.courses_in_progress += ['Git']
first_student.courses_in_progress += ['Python']
# завершенные курсы
first_student.finished_courses += ['Java']

# информация о втором студенте
second_student = Student('Mary', 'Shelley', 'female')
# текущие курсы второго студента
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Java']
# завершенные курсы
second_student.finished_courses += ['Git']

# информация о первом лекторе
first_lecturer = Lecturer('Bill', 'Gates')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

# информация о втором лекторе
second_lecturer = Lecturer('Steve', 'Jobs')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Java']

# информация о проверяющих
first_reviewer = Reviewer('Charles', 'Wayne')
second_reviewer = Reviewer('Henry', 'Morgan')

# выставление оценок первому студенту за первый курс
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 8)
# выставление оценок первому студенту за второй курс
first_reviewer.rate_hw(first_student, 'Git', 8)
first_reviewer.rate_hw(first_student, 'Git', 7)
first_reviewer.rate_hw(first_student, 'Git', 9)

# выставление оценок второму студенту за первый курс
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 7)
# выставление оценок второму студенту за второй курс
second_reviewer.rate_hw(second_student, 'Java', 7)
second_reviewer.rate_hw(second_student, 'Java', 6)
second_reviewer.rate_hw(second_student, 'Java', 8)

# выставление оценок первому лектору
first_student.rate_lecture(first_student, first_lecturer, 'Python', 10)
first_student.rate_lecture(first_student, first_lecturer, 'Python', 8)
first_student.rate_lecture(first_student, first_lecturer, 'Python', 9)
first_student.rate_lecture(first_student, first_lecturer, 'Python', 9)
first_student.rate_lecture(first_student, first_lecturer, 'Git', 7)
first_student.rate_lecture(first_student, first_lecturer, 'Git', 8)
first_student.rate_lecture(first_student, first_lecturer, 'Git', 6)

# выставление оценок второму лектору
second_student.rate_lecture(second_student, second_lecturer, 'Python', 9)
second_student.rate_lecture(second_student, second_lecturer, 'Python', 7)
second_student.rate_lecture(second_student, second_lecturer, 'Python', 10)
second_student.rate_lecture(second_student, second_lecturer, 'Python', 8)
second_student.rate_lecture(second_student, second_lecturer, 'Java', 7)
second_student.rate_lecture(second_student, second_lecturer, 'Java', 8)
second_student.rate_lecture(second_student, second_lecturer, 'Java', 6)

# подсчет средней оценки студента по всем курсам
first_student.average()
second_student.average()
# подсчет средней оценки лектора
first_lecturer.average_lecture()
second_lecturer.average_lecture()

# Задание № 3. Полиморфизм и магические методы
print(f'\n{first_student}')
print(f'\n{second_student}')
print(f'\n {first_student > second_student}')

print(f'\n{first_lecturer}')
print(f'\n{second_lecturer}')
print(f'\n {first_lecturer > second_lecturer}')

print(f'\n{first_reviewer}')
print(f'\n{second_reviewer}\n')

# Задание № 4. Полевые испытания
average_course(first_student, second_student, 'Python')
average_course_lecturers(first_lecturer, second_lecturer, 'Python')
