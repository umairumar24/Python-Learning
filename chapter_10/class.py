class Employee:
    language = "Py" # This is a class attribute
    salary = 12000000

harry = Employee()
harry.name = "harry" # This is an instance attribute
print(harry.name, harry.language, harry.salary)

Ahmad = Employee()
Ahmad.name = "Ahmad"
print(Ahmad.name, Ahmad.salary, Ahmad.language)