#부모 클래스만들기
class Person :
    "부모 클래스"
    def __init__(self, name, phoneNumber) :
        self.Name = name
        self.PhoneNumber = phoneNumber
    
    def PrintInfo(self) :
        print("info(name={0}), phoneNumber={1}".format(self.Name, self.PhoneNumber))

    def PrintPersonData(self) :
        print("Person(name={0}), phoneNumber={1}".format(self.Name, self.PhoneNumber))

class Student(Person) :
    "자식클래스"
    def __init__(self, name, phoneNumber, subject, studentID):
        self.Name = name
        self.PhoneNumber = phoneNumber
        self.Subject = subject
        self.StudentId = studentID

p = Person("커트", "0504-0504")
s = Student("프란시스", "0505-0505", "actor", "1234")

print(p.__dict__)
print(s.__dict__)

