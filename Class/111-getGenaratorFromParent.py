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
    def __init__(self, name, phoneNumber, subject, studentID): # 이걸로도 충분하지만
        Person.__init__(self, name, phoneNumber) # 명시적으로 Person 생성자 호출
