
class Student:
    def __init__(self, grades, is_punctual):
        self.grades = grades              
        self.is_punctual = is_punctual

    def get_highest(self, grades):
        """ Return the highest score based on student grades """
        highest_grade = 0

        for value in grades.values():
            if value > highest_grade:
                highest_grade = value
        
        return highest_grade
           
    


































