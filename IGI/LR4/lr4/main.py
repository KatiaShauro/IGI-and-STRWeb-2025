from tasks import Task1, Task2, Task3, Task4, Task5
from utils import infinity_method


@infinity_method
def laboratory():
    try:
        inp = int(input("Select task number: "))
        if inp not in range(1, 6):
            raise ValueError("Select from range 1..5")
    except ValueError as e:
        print(f"Error: {e}")
        return
    if inp == 1:
        task1 = Task1()
        task1.start()
    elif inp == 2:
        task2 = Task2()
        task2.start()
    elif inp == 3:
        try:
            x = float(input("Before starting please init 'x' and 'epsilon' to Taylor's series\n"
                  "Enter x: "))
            eps = float(input("Enter epsilon: "))
        except ValueError as e:
            print(f"---[ERROR]---\n{e}")
            return
        task3 = Task3(x, eps)
        task3.start()
    elif inp == 4:
        task4 = Task4()
        task4.start()
    elif inp == 5:
        task5 = Task5()
        task5.start()


if __name__ == '__main__':
    print("STARTED")
    laboratory()
