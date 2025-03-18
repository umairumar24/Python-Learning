class Employee:
    language = "Python" # This is a class attribute
    salary = 12000000

harry = Employee()
harry.language = "javascripte" # This is an instance attribute
print(harry.name, harry.language, harry.salary)
