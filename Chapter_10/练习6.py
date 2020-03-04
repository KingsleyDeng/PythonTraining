python_student = input('请输入学习python的学员编号，以逗号分隔：')
java_student = input('请输入学习java的学员编号，以逗号分隔：')
python_student = python_student.split(',')
java_student = java_student.split(',')
py_sd_set = set(python_student)
java_sd_set = set(java_student)
diff = py_sd_set - java_sd_set
print('只学python不学java的学员有：', diff)
print('只学python不学java的学员有%d人' % len(diff))