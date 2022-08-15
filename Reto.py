class Estudiantes():
    def __init__(self, nombre, id):
        self.name = nombre
        self.id = id
        self.enrCourses = []
   
    def _str_(self):
        txt = "Estudiante: {0} - id: {1} ({2})"
        return txt.format(self.name, self.id, self.enrCourses)

    def enr_C(self, curso):
        if curso == curso in self.enrCourses:
            print(f"Ya esta matriculado en {curso.name}, no puede matricular")
        else:
            self.enrCourses.append(curso)
            curso.students.append(self)
            print("Matriculado")

    def cancel_C(self,course):
        if course == course in self.enrCourses:
            self.enrCourses.remove(course)
        else:
            print("No esta matriculado")

class Profesor():
    def __init__(self, nombre, id):
        self.name = nombre
        self.id = id
        self.courses = []
        self.exams = []
       
    def _str_(self):
        txt = "Profesor: {0} - id: {1} ({2})"
        return txt.format(self.name, self.id, self.courses, self.exams)
   
    def createExam(self, tema, porcentaje, preguntas, curso):
        exam=Examen(tema, porcentaje, preguntas)
        exam.course=curso
        self.exams.append(exam)

    def teach(self, course):                
        if course == course in self.courses:
            print(f"Enseñando en el curso de {course.name}")
        else:
            self.courses.append(course)
            course.professor.append(self)
            print(f"El profesor {self.name} esta registrado en {course.name}")

class Materias():
    def __init__(self, nombre, grupo):
        self.name = nombre
        self.grupo = grupo
        self.students = []
        self.professor = []

    def _str_(self):
        txt = " Curso: {0} - Grupo: {1} - Estudiante{2}) - Profesor{3})"
        return txt.format(self.name, self.grupo, self.students, self.professor)

    def printList(self,y):
        studentsList=[]*y
        for x in range(y):
            studentsList.append(self.students[y].name)
        return print(studentsList)

    def remove_student(self, stud):
        if stud == stud in self.students:
            self.students.remove(stud)
            print(f"El estudiante {stud.name} removido del curso de {self.name}")
        else:
            print(f"El estudiante {stud.name} no esta matriculado en {self.name}")

    def get_student(self):
        list=[]*len(self.students)
        if len(self.students) >= 1:
            for i in range(len(self.students)):
                list.append(self.students[i].name)
            print(list)
        else:
            print(f"El curso de {self.name} no tiene estudiantes")


#RETO 3
class Examen():                                                             
    def __init__(self, tema , porcentaje, preguntas):
        self.topic = tema
        self.percent = porcentaje
        self.question = preguntas
        self.course = []
       
    def _str_(self):
        txt = "Examen de: {0} - valor: {1} - Preguntas: {2} - del {3} curso"
        return txt.format(self.topic, self.percent, self.question, self.course)




student1 = Estudiantes("Flavia", "1001")
student2 = Estudiantes("Tatiana", "1002")
student3 = Estudiantes("Jhon", "1003")
student4 = Estudiantes("Samuel", "1004")

teacher1 = Profesor("Jonathan", "2001")
teacher2 = Profesor("Gildardo", "2002")
teacher3 = Profesor("Hilda", "2003")
teacher4 = Profesor("Bayron", "2004")
teacher5 = Profesor("Mateus", "2005")

course1 = Materias("Calculo Diferencial", "70")
course2 = Materias("Algebra lineal", "69")
course3 = Materias("Matematicas discretas", "30")
course4 = Materias("Calculo integral", "23")
course5 = Materias("algoritmos y programacion orientada a objetos", "25")


student1.enr_C(course1)
student3.enr_C(course1)
student1.enr_C(course1)
student2.enr_C(course3)
student2.enr_C(course3)
student4.enr_C(course3)
student4.enr_C(course1)

teacher1.teach(course1)
teacher2.teach(course2)
teacher3.teach(course3)

course1.get_student()

student1.cancel_C(course1)
course1.remove_student(student1)

course1.get_student()

teacher1.createExam("Productos notables", "15%", "10", course1) 
print(teacher1.exams[0].topic)

teacher2.createExam("algebra booleana", "20%", "5", course2)
print(teacher2.exams[0].percent)