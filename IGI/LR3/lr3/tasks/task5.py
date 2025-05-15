from utils import my_generator, task_starter  # noqa


def float_list_task(numbers: list[float]):
    """
    Find the sum of the negative elements of the list
    and the product of the elements located between the
    maximum and minimum elements
    """
    print(numbers)
    summa = sum(x for x in numbers if x < 0)
    max_index = numbers.index(max(numbers))
    min_index = numbers.index(min(numbers))

    if max_index < min_index:  # If the maximum comes before the minimum.
        max_index, min_index = min_index, max_index

    between = numbers[min_index + 1: max_index]
    product = 1
    for b in between:
        product *= b

    return [summa, product]


# task_starter(float_list_task, my_generator, message=[
#     "The sum of the negative list items: ",
#     "The product of the elements located between "
#     "the maximum and minimum elements: "
# ])
