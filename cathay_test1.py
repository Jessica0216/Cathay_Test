students = {'德瑞克':33, '尚恩':73, '傑夫':63, '馬基':39}
for student in students:
  cnt = 0
  for i in range(1, 4, 1):
    new = students[student] + i
    if new % 5 == 0:
      if new > 40:
        print(student, new)
      else:
        print(student, students[student])
    else:
      cnt = cnt + 1
    if cnt == 3:
      print(student, students[student])
