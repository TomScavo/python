import csv
from student import Student

students=[]
for i in range(3):
    name=input("name: ")
    dorm=input("dorm: ")
    
    students.append(Student(name,dorm))
    
file=open("student.csv","w")
writer=csv.writer(file)
for student in students:
    writer.writerow((student.name,student.dorm))
file.close
    