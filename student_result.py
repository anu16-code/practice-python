name = input("enter student name")
marks =[1]
for i in range (3):
    mark = int(input("enter mark:"))
    marks.append(mark)
student_result ={
    "name": name,
    "marks": marks
}
total_marks = sum(marks)
average_marks = total_marks/3
print("student name:", student_result["name"])
print("total marks:", total_marks)
print("average marks:", average_marks)
if average_marks >= 90:
    print("grade:A", "pass")
elif average_marks >= 75:
    print("grade:B","pass")
elif average_marks >= 60:
    print("grade:C", "pass")
elif average_marks >= 50:
    print("grade:D", "fail")
