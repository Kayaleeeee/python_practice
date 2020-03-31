grades = [100, 92, 82, 80, 74, 70, 40]

for grade in grades:
    if grade >= 90 and grade < 100:
        print(str(grade) + '점의 학점은 A입니다.')

    elif grade >= 80 and grade < 90:
        print(str(grade) + '점의 학점은 B입니다.')

    elif grade >= 70 and grade < 80:
        print(str(grade) + '점의 학점은 C입니다.')

    else:
        print(str(grade) + '점의 학점은 D입니다.')
