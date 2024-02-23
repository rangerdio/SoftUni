# 10 SIMPLE TASK FROM OpenAI
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


introduction_objects = []

while True:
    data = input().split()
    if data[0] == "Stop":
        break
    person = Person(data[0], data[1])
    introduction_objects.append(person)

for element in introduction_objects:
    print(element.introduce())

#
# 1. Problem Description: Create a class called Person with attributes name and age.Write a method called introduce
# that prints out the person's name and age.
#
#
# PyCharm Test and Answers: python Copy code
# person = Person("Alice", 30)
# person.introduce()
#
# Expected output: My name is Alice and I am 30 years old.
#
# Solution: python Copy code
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")