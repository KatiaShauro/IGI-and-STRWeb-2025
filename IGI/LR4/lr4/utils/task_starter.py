def infinity_method(func):
    def new_func(*args, **kwargs):
        cont = True
        while cont:
            func(*args, **kwargs)
            cont = (
                    input(f"Do you want to continue this task? "
                          f"It is '{func.__name__}()' running now [Y/N] ")
                    .strip().upper()
                    in ("Y", "YES", "Д", "ДА", 1)
            )
    return new_func
