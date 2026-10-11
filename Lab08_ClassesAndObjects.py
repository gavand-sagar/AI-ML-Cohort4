# class Person:
#     # static
#     def display_information():
#         print("simple static method")

#     # instance method
#     def say_hello(self):
#         print("Hi there!")


# Person.display_information()

# p = Person()
# p.say_hello()


############################################
# # constructor
# class Person:
#     name = ""

#     # dunder methods
#     def __init__(self, name = ''):
#         self.name = name

#     def display_name(self):
#         print("Hi, my name is " + self.name)


# p = Person("Alice")
# p.display_name()


############################################
# class Animal:
#     def speak(self):
#         print("...")


# class Cat(Animal):
#     def speak(self):
#         print("Meow")


# class Dog(Animal):
#     def speak(self):
#         # call parent method too.
#         super().speak()
#         print("Woaf")



# d = Dog()
# d.speak()

# c= Cat()
# c.speak()



class Value:
    value = 0
    def __init__(self, value):
        self.value = value

    ## operator overloading for '+'
    def __add__(self, other):
        result = self.value + other.value
        return Value(result)

    # operator overloading for '-'
    def __sub__(self, other):
        result = self.value - other.value
        return Value(result)
        

    def __mul__(self, other):
        pass


a = Value(90)
b = Value(100)
c = Value(78)

r = a + b - c


print(r.value)