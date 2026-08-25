
import random
import dictionaries

def get_avrg(grades):
    """ Returns the avearage of each students score """
    result = {}

    for subjects, students in grades.items():
        for student, assignments in students.items():
            avg = assignments["A1"] + assignments["A2"] // 2
        
            if student not in subjects:
                result[student] = []
            result[student].append(avg)
            
    return {student: sum(vals) // len(vals) for student, vals in result.items()}
        
print(get_avrg(dictionaries.grade_tracker))






























