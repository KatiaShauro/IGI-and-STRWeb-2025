from random import uniform


def my_generator(count=10, max_value=100):
    """
    Generates random floats from -max_value to max_value
    """
    num = 0
    while num < count:
        yield uniform(-max_value, max_value)
        num += 1


def user_input_init():
    """
    Validate input list of integers
    :return: list[int]
    """
    print("Enter the array. 1 - end of input\n")
    numbers = []
    while True:
        try:
            n = int(input())
            numbers.append(n)
            if n == 1:
                print(numbers)
                return numbers
        except ValueError:
            print("[Error]: input must be int!")
