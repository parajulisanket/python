#  hari = 82 ram = 65 shyam 55 rita 42

# name_score = {'hari': 82,'ram': 65,'shyam': 55,'rita': 42 }
# student =input("Enter the name of the students :").capitalize() 
# if name_score[student] >= 80 :
#     print(f'Congratulation! {student} You got distinction.')
#     #print("Congratulation!",student,"You got distinction.")
# elif name_score[student] >= 60 and name_score[student] < 80 :
#     print(f'Congratulation! {student} you got First division.')
#     # print("Congratulation!",student,"you got First division.")
# elif name_score[student] >=50 and name_score[student] <60 :
#     print(f'Congratulation! {student} you got Second division.')
#     # print("Congratulation!",student,"you got Second division.")
# elif name_score[student] < 50:
#     print(f"Congratulation! {student} you will receive Mom's flying chappel.")
#     #print("Congratulation!",student,"you will receive Moms flying chappel.")


student_grade = {'ram': 85, 'shyam': 65, 'hari':55,'rita': 42}
name = input('enter your name: ').lower()

if name not in student_grade:
    print('Name not found')
else:
    if student_grade[name]>= 80:
        print(f'hi {name.capitalize()},you grade is {student_grade[name]}')
    elif student_grade[name] >= 60:
        print(f'hi {name.capitalize()},you grade is {student_grade[name]}')
    elif student_grade[name] >= 50:
        print(f'hi {name.capitalize()},you grade is {student_grade[name]}')
    else:
        print(f"hi {name.capitalize()},Mom's flying chappel {student_grade[name]}")

