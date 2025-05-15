import types


def infinity_method(func):
    def new_func(*args, **kwargs):
        cont = True
        while cont:
            func(*args, **kwargs)
            cont = (
                    input(f"Do you want to continue this task? "
                          f"It is {func.__name__} running now [Y/N] ")
                    .strip().upper()
                    in ("Y", "YES", "Д", "ДА", 1)
            )
    return new_func


@infinity_method
def task_starter(task, generator_func=input, message=None):
    """
    Executes task function with data from generator function
    :param task: laboratory work task
    :param message: result information
    :param generator_func: generator function
    """
    if generator_func == input:
        print("Enter the string...")

    data = generator_func()
    if type(data) is types.GeneratorType:
        data = list(data)

    result = task(data)

    if result is not None:
        for r in result:
            print(message[result.index(r)], r)
