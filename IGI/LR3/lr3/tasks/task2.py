from utils import user_input_init, task_starter  # noqa


def even_nums_average(numbers: list[int]):
    """
    Calculates the arithmetic mean of even numbers
    :param numbers: list of integers
    :return: average of even nums
    """
    even_nums = []
    summa = 0
    for n in numbers:
        if n % 2 == 0:
            even_nums.append(n)
            summa += n
    if not even_nums:  # If all numbers from list are non-even.
        print("No even elements")
        return 0
    return [summa/len(even_nums)]


# task_starter(even_nums_average, user_input_init, ["Average of even nums:"])
