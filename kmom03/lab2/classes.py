""" Classes for lab2"""

class Person:
    """ Person class for lab2 """

    def __init__(self, name, ssn, address = ""):
        """ Constructor for Person class """
        self.name = name
        self._ssn = ssn
        self._address = address

    @property
    def ssn(self):
        """ SSN getter """
        return self._ssn

    @property
    def address(self):
        """ Address getter """
        return self._address

    @address.setter
    def address(self, address):
        """ Adress setter """
        self._address = address

    def __str__(self):
        """ Overwrite str() """
        return f'Name: {self.name} SSN: {self.ssn} {str(self.address)}'

class Address:
    """ Address class for lab2 """

    def __init__(self, city, state, country):
        """ Constructor for Address class """
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        """ Overwrite str() """
        return f'Address: {self.city} {self.state} {self.country}'

class Teacher(Person):
    """ Teacher class for lab2 """

    def __init__(self, name, ssn, address = ""):
        """ Constructor for Teacher class """
        super().__init__(name, ssn, address)
        self.courses = []

    def add_course(self, course):
        """ Add a course """
        self.courses.append(course)

    def __str__(self):
        """ Overwrite str() """
        return f'{super().__str__()}Courses: {", ".join(self.courses)}'

class Student(Person):
    """ Student class for lab2 """

    def __init__(self, name, ssn, address = ""):
        """ Constructor for student class """
        super().__init__(name, ssn, address)
        self.courses_grades = []

    def add_course_grade(self, course, grade):
        """ Add a grade """
        self.courses_grades.append((course, grade))

    def average_grade(self):
        """ Get average grade """
        total = 0
        length = 0
        for grade in self.courses_grades:
            if grade[1] != "-":
                total += int(grade[1])
                length += 1
        return total/length if length > 0 else 0
