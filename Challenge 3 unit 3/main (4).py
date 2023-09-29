
#Let implement a function sort_students
#with each student attributes of name,rollnumber and cgpa
#And sort The students using CGPA in Descending Order
#Check the function with different Input

class student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # let sort the list of students in descending order of cgpa
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students

# lets check the example for the code :
students = [
  student("Keerthu","CSC106",8.8),
  student("Jesu","CSC111",9.3),
  student("Silviya","CSC128",9.1),
  student("Valan","CSC124",8.9)
]

sorted_students = sort_students(students)

#lets print the sorted students
print("List of Sorted Students in descending order \n")

for student in sorted_students:
  print("Name: {},Roll Number: {},CGPA: {}".format(student.name,
                                            student.roll_number,
                                            student.cgpa))