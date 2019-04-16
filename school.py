class School(object):
	def __init__(self, name, board, address):
		self.name = name
		self.board = board
		self.address = address
		self.teachers = []
		self.students = []
		self.classrooms = []

	def add_teacher(self, teacher_object):
		self.teachers.append(teacher_object)

	def add_student(self, student_object):
		self.students.append(student_object)

	def add_classroom(self, classroom_object):
		self.classrooms.append(classroom_object)

	def list_students(self):
		for student in self.students:
			print(student)

	def list_teachers(self):
		for teacher in self.teachers:
			print(teacher)

	def list_classrooms(self):
		for classroom in self.classrooms:
			print(classroom)

class Person(object):
	def __init__(self, name, dob):
		self.name = name
		self.dob = dob

	def __repr__(self):
		return str(self.name) 


class Teacher(Person):
	def __init__(self, name, dob, subject, experience):
		super().__init__(name, dob)
		self.subject = subject
		self.experience = experience
		self.classroom = None

	def assign_classroom(self , classroom_object):
		self.classroom = classroom_object
		classroom_object.class_teacher = self


class Student(Person):
	def __init__(self, name, dob, grade):
		super().__init__(name, dob)
		self.grade = grade
		self.classroom = None

	def assign_classroom(self, classroom_object):
		self.classroom = classroom_object
		classroom_object.students.append(self)


class Classroom(object):
	def __init__(self, grade, section):
		self.grade = grade
		self.section = section
		self.class_teacher = None
		self.students = []

	def list_students(self):
		for student in self.students:
			print(student)

	def __repr__(self):
		return str(self.grade) + str(self.section)





mms = School('Mercy Memorial School', 'ICSE', 'Kidwai Nagar, Kanpur')

sp = Teacher('sandeep', '12-03-1956', 'Physics', 6)
mms.add_teacher(sp)

mini = Teacher('Mini', '11-03-1951', 'Biology', 4)
mms.add_teacher(mini)


eleventh_c = Classroom(11, 'C')
mms.add_classroom(eleventh_c)

tenth_b = Classroom(10, 'B')
mms.add_classroom(tenth_b)

sp.assign_classroom(eleventh_c)
mini.assign_classroom(tenth_b)

saumy = Student('saumya', '15-08-1994', '11')
saumy.assign_classroom(eleventh_c)

rjt = Student('rajat', '5-10-1993', '11')
rjt.assign_classroom(eleventh_c)

rjs = Student('rajshree', '10-1-1994', '11')
rjs.assign_classroom(tenth_b)

mms.add_student(rjt)
mms.add_student(rjs)
mms.add_student(saumy)


