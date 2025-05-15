from tasks.task3 import Graphics
from utils import infinity_method


class Task3(Graphics):
    def __init__(self, x: float, eps: float):
        super().__init__(x, eps)


    @infinity_method
    def start(self):
        print("Choose action:\n"
              "1 - Show taylor series\n"
              "2 - Show average\n"
              "3 - Show median\n"
              "4 - Show mode\n"
              "5 - Show variance\n"
              "6 - Show SKO\n"
              "7 - Show graphics\n"
              )
        try:
            inp = int(input("Enter a num: "))
            if inp not in range(1, 8):
                raise ValueError("Please, choose value from 1 to 7!")
        except ValueError as e:
            print(f"\n---[ERROR]---\n{e}")
            return

        if inp == 1:
            print(f"\nTaylor series:\n{self.taylor_series()}")
        elif inp == 2:
            print(f"\nThe average of taylor series is {round(self.evolve_average(), 5)}")
        elif inp == 3:
            print(f"\nThe median of taylor series is {round(self.evolve_median(), 5)}")
        elif inp == 4:
            res = self.evolve_mode()
            if not res:
                print("All values are unique --> no mode!")
            else:
                print(f"\nThe mode of taylor series is {round(res, 5)}")
        elif inp == 5:
            print(f"\nThe variance of taylor series is {round(self.evolve_variance(), 5)}")
        elif inp == 6:
            print(f"\nThe SKO of taylor series is {round(self.evolve_sko(), 5)}")
        elif inp == 7:
            print("Plots: ")
            self.plot()


if __name__ == "__main__":
    Task3(2, 0.01).start()