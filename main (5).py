class student:
  def __init__   (self,name,roll_number,cgpa):           
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def Sort_student(student_list):       
  sorted_student =sorted(student_list,key=lambda student: student.cgpa, reverse=True)
  return sorted_student
student=[
  student("stephen","A123",7.8),
  student("karthik","A124",8.9),         student("santhosh","A125",9.1),        student("komban","A126",9.9),
]
sorted_student=Sort_student(student)
for student in sorted_student:
  print("Name:{}, Rollnumber:{}.CGPA{} ".format(student.name,student.roll_number,student.cgpa))
                  

  