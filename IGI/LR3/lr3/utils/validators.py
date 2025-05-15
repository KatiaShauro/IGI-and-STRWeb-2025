class MyError(ValueError):  # Custom error class
    pass


def epsilon_and_x_validator():
    """
    Validate 0 < epsilon < 1 and |x| > 1
    :return: epsilon, x
    """
    while True:
        try:
            epsilon = float(input("Enter epsilon: "))
            if not 1 > epsilon > 0:
                raise MyError("epsilon must be less than 1 and bigger than 0")
            x = float(input("Enter x: "))
            if abs(x) <= 1:
                raise MyError("the absolute value of x must be greater than 1")
            return {
                "epsilon": epsilon,
                "x": x
            }
        except MyError as e:
            print(f"[Error]: {e}")
        except ValueError:
            print("[Error]: input must be a number!")


def task_number_input_validator():
    """
    Validate input integer value
    :return: correct task number
    """
    while True:
        try:
            n = int(input())
            if n not in [1, 2, 3, 4, 5]:
                raise MyError("No task with such number")
            return n
        except MyError as e:
            print(f"[Error]: {e}")
        except ValueError:
            print("[Error]: input must be an integer!")
