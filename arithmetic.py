def add(a, b):
    return a+b

def minus(a, b):
     return a-b

def divide(a, b):
     return a/b

def multiply(a, b):
     return a*b


name = "ibkk"

def compute_grade(course_score):
    if course_score >= 70 and course_score <= 100:
       return "A"
    elif course_score >= 60 and course_score <= 69:
        return "B"
    elif course_score >= 50 and course_score <= 59:
        return "C"
    elif course_score >= 45 and course_score <= 49:
        return "D"
    elif course_score >= 40 and course_score <= 44:
        return "E"
    elif course_score >= 0 and course_score <= 39:
        return "F"
    elif course_score > 100 or course_score < 0:
        return "Score can only range from 0 - 100"
    else:
        return "Invalid Input"