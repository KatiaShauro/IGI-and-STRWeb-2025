from tasks.task4 import Rhombus
from utils import infinity_method
from utils.errors import InvalidAngleError, InvalidSideError, InvalidColorError


class Task4:

    def __init__(self):
        self.rhombus = Rhombus()


    @infinity_method
    def start(self):
        print("Choose action:\n"
              "1 - Use non-default rhombus\n"
              "2 - Show rhombus square\n"
              "3 - Show rhombus color\n"
              "4 - Show rhombus info\n"
              "5 - Show rhombus name\n"
              "6 - Show rhombus plot\n"
              )
        try:
            inp = int(input("Enter a num: "))
            if inp not in range(1, 7):
                raise ValueError("Please, choose value from 1 to 6!")
        except ValueError as e:
            print(f"\n---[ERROR]---\n{e}")
            return

        if inp == 1:
            try:
                a = float(input("Enter rhombus side: "))
                angle = int(input("Enter rhombus angle: "))
                color = input("Enter rhombus color: ")
                name = input("Enter rhombus name: ")
                self.rhombus = Rhombus(a, angle, color, name)

                print("HEY! You have been init your own rhombus! "
                      "Now we are gonna use your values to perform actions")

            except (InvalidAngleError, InvalidSideError, InvalidColorError, ValueError) as e:
                print(f"\n---[ERROR]---\n{e}")
                return
        elif inp == 2:
            print(f"{self.rhombus.get_name()} square: {self.rhombus.calc_square()}")
        elif inp == 3:
            print(f"{self.rhombus.get_name()} color: {self.rhombus.shape_color}")
        elif inp == 4:
            print(self.rhombus)
        elif inp == 5:
            print(f"Shape name - {self.rhombus.get_name()}")
        elif inp == 6:
            self.rhombus.plot()



if __name__ == '__main__':
    t = Task4()
    t.start()
