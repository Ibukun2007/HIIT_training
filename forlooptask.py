from arithmetic import compute_grade

course_number = int(input(f"Enter the number of course: "))
course_list = []
for i in range(course_number):
    course_code = input(f"Enter course code {i+1}: ")
    course_score = float(input(f"Enter score {i+1}: "))
    print(" ")

    course = {"code": course_code, "score": course_score}
    course_list.append(course)

for course in course_list:
    score = course.get("score")
    print(f"{course.get('code')} - {score} - {compute_grade(score)}")