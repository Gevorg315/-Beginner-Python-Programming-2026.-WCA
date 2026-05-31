class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"Name: {self.name}, Age: {self.age}"


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"


member = SchoolMember("Mr.Snape", 40)
teacher = Teacher("Mr.Snape", 40, 3000)
student = Student("Harry", 16, 75)

if __name__ == "__main__":
    assert teacher.show() == "Name: Mr.Snape, Age: 40, Salary: 3000"
    assert student.show() == "Name: Harry, Age: 16, Grades: 75"
    assert member.show() == "Name: Mr.Snape, Age: 40"