def main():
    students = {}
    for i in range(0, 5):
        name = input('what is your name?')
        grade = int(input('what is you grade'))
        students[name] = grade
    print(get_average_grade(students))
    print(get_highest_grade(students))


def get_average_grade(students: dict):
    x = list(students.values())
    return (x[0] + x[1] + x[2] + x[3] + x[4]) / 5


def get_highest_grade(students: dict):
    max_grade = max(students.values())
    index_max = list(students.values()).index(max_grade)
    student = list(students.keys())[index_max]
    return f"{student}: {max_grade}"

main()
