from utils import infinity_method
from utils.errors import InvalidCArrayError
from tasks.task5 import NumPyClass


class Task5:

    def __init__(self):
        self.my_numpy = NumPyClass()


    @infinity_method
    def start(self):
        print("Choose action:\n"
              "1 - Use non-default NumPyClass\n"
              "2 - Show main array and c-array\n"
              "3 - Show all elements that bigger than entered value\n"
              "4 - Show statistic's median value\n"
              "5 - Show my median value\n"
              )
        try:
            inp = int(input("Enter a num: "))
            if inp not in range(1, 6):
                raise ValueError("Please, choose value from 1 to 5!")
        except ValueError as e:
            print(f"\n---[ERROR]---\n{e}")
            return

        try:
            if inp == 1:
                n = int(input("Enter n: "))
                m = int(input("Enter m: "))
                N = int(input("Enter max value: "))

                if n <= 0 or m <= 0 or N <= 0:
                    raise ValueError("Parameters must be positive values!")

                self.my_numpy = NumPyClass(n, m, N)
                print("HEY! You have been init your own Num Py! "
                      "Now we are gonna use your values to perform actions")

            elif inp == 2:
                self.my_numpy.print_arrays()
            elif inp == 3:
                element = int(input("Enter value: "))
                print(f"All elements bigger than {element}: "
                      f"{self.my_numpy.all_elements_greater_than_b(element)}")
            elif inp == 4:
                print(f"Statistic's median value: {self.my_numpy.calc_median()}")
            elif inp == 5:
                print(f"My median value: {self.my_numpy.my_median()}")

        except (ValueError, InvalidCArrayError) as e:
            print(f"\n---[ERROR]---\n{e}")
            return


if __name__ == '__main__':
    t = Task5()
    t.start()
