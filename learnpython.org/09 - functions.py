print('--- Running functions.py ---')

# Functions are prepended with the 'def' keyword


def hello_world():
    print("Hello world!")


# Parameters can be set inside the parentheses
def say_hello(name):
    print("Hello %s!" % name)


# You can return values for assigning later on
def sum(num1, num2):
    return num1 + num2


hello_world()
say_hello("Jacob")
my_sum = sum(12, 40)
print(my_sum)


# Exercise
def list_benefits():
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together"
    ]


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()

print('--- Finished functions.py ---')
