name = input("Enter your name: ")
score = float(input("Enter your score: "))
course_title = input("Enter your course title: ")

if score >=70:
    print(f"hello user: {name}, Your grade in {course_title} is A")
elif score >=60:
    print(f"hello user: {name}, Your grade in {course_title} is B")
elif score >=50:
    print(f"hello user: {name}, Your grade in {course_title} is C")
elif score >=45:
    print(f"hello user: {name}, Your grade in {course_title} is D")
elif score >=40:
    print(f"hello user: {name}, Your grade in {course_title} is E")
else:
    print(f"hello user: {name}, Your grade in {course_title} is F")
    

    if course_score >= 70 and course_score <= 100:
        print(f"{course_name} - {course_score} - A")
    elif course_score >= 60 and course_score <= 69:
            print(f"{course_name} - {course_score} - B")
    elif course_score >= 50 and course_score <= 59:
        print(f"{course_name} - {course_score} - C")
    elif course_score >= 45 and course_score <= 49:
        print(f"{course_name} - {course_score} - D")
    elif course_score >= 40 and course_score <= 44:
        print(f"{course_name} - {course_score} - E")
    elif course_score >= 0 and course_score <= 39:
        print(f"{course_name} - {course_score} - F")
    elif course_score > 100 or course_score < 0:
        print("Score can only range from 0 - 100")
    else:
        print("Invalid Input")