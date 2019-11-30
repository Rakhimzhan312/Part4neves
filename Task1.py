class Student:
    name = 'Vasya'
    lastname = 'Pupkin'
    department = 'Programmirovanie'
    year_of_entrance = '2019'

    def get_student_info(self):
        print(self.name, self.lastname, 'postupil v', self.year_of_entrance, 'na fakultet', self.department,)     

Student0 = Student()
Student0.get_student_info()                 
