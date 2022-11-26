def student():
    file = open('file.txt', 'a+')
    for i in range(0,3):
        name = input('what is your name?')
        grade = input('what is your grade?')
        file.write(f'{name.strip()} - {grade}\n')



student()

