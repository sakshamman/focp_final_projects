# check this

num_students = int(input("How many students? "))
group_size = int(input("Required group size? "))

num_groups = num_students // group_size
students_left = num_students % group_size

if num_groups == 1:
    group_word = "group"
else:
    group_word = "groups"

if students_left == 1:
    leftover_word = "student"
else:
    leftover_word = "students"

print(f"There will be {num_groups} {group_word} with {students_left} {leftover_word} left over.")

