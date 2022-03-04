subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]

x = sorted(subject_marks, key=lambda x: x[1])

print(*[f'{i[0]} {i[1]}' for i in x], sep='\n')
