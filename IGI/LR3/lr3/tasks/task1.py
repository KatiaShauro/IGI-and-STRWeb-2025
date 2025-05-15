import math


from utils import epsilon_and_x_validator, task_starter  # noqa


def taylor_series(input_data):
    """
    Decomposes the logarithm ln((x+1)/(x-1)) into a Taylor series
    :param input_data: dictionary of precision and x
    :return: dictionary from x, n, resulting sum, system sum, accuracy
    """
    epsilon = input_data["epsilon"]
    x = input_data["x"]
    cur_eps = 1
    summa = 0
    n = -1
    system_solution = math.log(  # Counting using built-in functions.
        (x+1) / (x-1),
        math.exp(1)
    )
    try:
        while cur_eps > epsilon and n < 500:
            n += 1
            summa += 2 / ((2*n + 1) * x**(2*n + 1))  # Taylor series expansion.
            cur_eps = abs(summa - system_solution)   # Error calculation.
    except OverflowError:
        print("Oh-oh, your chosen precision and base led to overflow :(")

    print(  # Writing the result into columns.
        f"x\t\t\t\tn\t\t\tF(x)\t\t\tMath F(x)\t\t\tepsilon\n"
        f"{x}\t\t\t{n}\t{summa}\t{system_solution}\t\t{epsilon}"
    )


#  task_starter(taylor_series, epsilon_and_x_validator)
