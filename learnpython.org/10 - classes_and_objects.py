print('--- Running classes_and_objects.py ---')


class MyClass:
    # Classes in Python lend concepts from many other programming languages where they are based on instances
    field = "fieldValue"

    def some_function(self):
        print("This is an output message from a MyClass instance")
        print("This instance field has a value of %s" % self.field)


# Now that we have an instance, we can modify it or run it separate from the rest
cls_1 = MyClass()
cls_2 = MyClass()
cls_2.field = "fieldValue2"
print(cls_1.field)
print(cls_2.field)
cls_2.some_function()

# Exercise


class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 6e4

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 1e4

print(car1.description())
print(car2.description())

print('--- Finished classes_and_objects.py ---')
