# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 08:36:12 2023

@author: DATA-JOHN
"""

my_dictionary={"name":"mark","school":"st james"}

for key in my_dictionary:
    print(key)
    print(my_dictionary[key])
    
student_scores={
    "harry":81,
    "ron":78,
    "hermione":99,
    "dramaco":74,
    "neville":62
    }
students_grades={}

for student in student_scores:
    score=student_scores[student]
    if score>90:
        students_grades[student]="outstanding"
    elif score>80:
        students_grades[student]="exceeds expectations"
    elif score>70:
        students_grades[student]="acceptable"
    else:
        students_grades[student]="fail"
    
print(students_grades)


teams={
       "france":["paris","lyon","lille"],
       "german":["bayern","dortmond","union barline"]
       }
print(teams)