class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_grade(self):
        all_grades = []
        for grade in list(self.grades.values()):
             all_grades += grade
        if len(all_grades) == 0:
            a_gr = 0
        else:
            a_gr = round(float(sum(all_grades) / len(all_grades)), 2)
        return a_gr

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self._avg_grade()}\n' \
              f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n' \
              f'Завершённые курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._avg_grade() < other._avg_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grade(self):
        all_grades = []
        for id in list(self.grades.values()):
             all_grades += id
        if len(all_grades) == 0:
            a_gr = 0
            # print('Пока нет оценок')
        else:
            a_gr = round(float(sum(all_grades) / len(all_grades)), 2)
        return a_gr

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_grade()}'
        return res

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._avg_grade() > other._avg_grade()


class Rewierer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def students_avg_grade_course(list, course):
    all_grades = []
    for student in list:
        if isinstance(student, Student) and course in student.grades.keys():
            all_grades += student.grades[course]
    if len(all_grades) == 0:
        avg_grade = 0
    else:
        avg_grade = round(float(sum(all_grades)/len(all_grades)), 2)
    return avg_grade

def lecturer_avg_grade_course(list, course):
    all_grades = []
    for lecturer in list:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades.keys():
            all_grades += lecturer.grades[course]
    if len(all_grades) == 0:
        avg_grade = 0
    else:
        avg_grade = round(float(sum(all_grades)/len(all_grades)), 2)
    return avg_grade



student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ralf', 'Stone', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Any', 'Body')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Git', 10)
student_1.rate_hw(lecturer_2, 'Python', 7)
student_1.rate_hw(lecturer_2, 'Git', 8)

student_2.rate_hw(lecturer_1, 'Python', 10)
student_2.rate_hw(lecturer_1, 'Git', 9)
student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Git', 9)

rewierer_1 = Rewierer('Some', 'Buddy')
rewierer_1.courses_attached += ['Python']
rewierer_1.courses_attached += ['Git']
rewierer_1.rate_hw(student_1, 'Python', 10)
rewierer_1.rate_hw(student_1, 'Git', 10)
rewierer_1.rate_hw(student_2, 'Python', 10)
rewierer_1.rate_hw(student_2, 'Git',8)

rewierer_2 = Rewierer('Any', 'Body')
rewierer_2.courses_attached += ['Python']
rewierer_2.courses_attached += ['Git']
rewierer_2.rate_hw(student_1, 'Python', 10)
rewierer_2.rate_hw(student_1, 'Git', 10)
rewierer_2.rate_hw(student_2, 'Python', 10)
rewierer_2.rate_hw(student_2, 'Git', 9)

student_list = []
student_list.append(student_1)
student_list.append(student_2)

lecturer_list = []
lecturer_list.append(lecturer_1)
lecturer_list.append(lecturer_2)

print(rewierer_1)
print()
print(lecturer_1)
print()
print(student_1)
print()
print(student_1.__lt__(student_2))
print(lecturer_1.__gt__(lecturer_2))
print()
print(f"Средняя оценка за ДЗ по Git = {students_avg_grade_course(student_list, 'Git')}")
print(f"Средняя оценка за ДЗ по Python = {students_avg_grade_course(student_list, 'Python')}")
print(f"Средняя оценка за лекции по Git = {lecturer_avg_grade_course(lecturer_list, 'Git')}")
print(f"Средняя оценка за лекции по Python = {lecturer_avg_grade_course(lecturer_list, 'Python')}")






