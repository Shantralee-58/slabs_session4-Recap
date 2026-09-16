# Author: SE Class


def greet_user():
    """
    This greets the user and welcomes them

    :param x: the name of the person to greet
    :return: None
    """
    print("Hello, Engineers")
    print("Welcome to session 4!")

greet_user()


def student_info():
    full_name = input("Please enter your name: ")
    print("Hello", full_name)

student_info()


def say_hello(name,last_name):
    print("Hello", name, last_name)
    print("How are you", name, last_name)

say_hello("Idah", "Khumalo")
#say_hello("Pearl")
#say_hello("Vusi")


def sum_numbers(x):
    return 3 * x

numbers = sum_numbers(5)
print(numbers)


def divide_numbers(x):
    return x / 2

div_numbers = divide_numbers(8)
print(div_numbers)


def user_name():
    pass
