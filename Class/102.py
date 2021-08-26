class Person :
    Name = '\'default Name\''
    def Print(self):
        print("My name is {0}".format(self.Name))

Person.Name = '그롤'
p1 = Person()
p1.Print()

p1.Name = '커트코베인'
p1.Print()

p1.age = 27
print(p1.age)

