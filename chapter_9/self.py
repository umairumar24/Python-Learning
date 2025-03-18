class Employee:
    language = "Python" # This is a class attribute
    salary = 12000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet(self):
        print("Good morning")

harry = Employee()
harry.language = "javascripte" # This is an instance attribute
# attribute
harry.getInfo()
harry.greet()
# Employee.getInfo(harry)