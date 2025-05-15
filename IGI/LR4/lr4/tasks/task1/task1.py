from tasks.task1 import SerializerMixin, Forest
from utils.task_starter import infinity_method


class Task1(SerializerMixin, Forest):
    def __init__(self, filename: str = "task1"):
        super().__init__(filename=filename)


    @infinity_method
    def start(self):
        print("Choose action:\n"
              "1 - Show forest\n"
              "2 - Add tree to forest\n"
              "3 - Find tree by name\n"
              "4 - Show total tree's count\n"
              "5 - Show healthy tree's count\n"
              "6 - Show sickness percentage\n"
              "7 - Show specific info about each type\n"
              "8 - Save to file with serialization\n"
              "9 - Read from serialized file\n")
        try:
            inp = int(input("Enter a num: "))
            if inp not in range(1, 10):
                raise ValueError("Please, choose value from 1 to 9!")
        except ValueError as e:
            print(f"\n---[ERROR]---\n{e}")
            return

        if inp == 1:
            self.show_all_forest()
        elif inp == 2:
            self.add_tree_from_input()
        elif inp == 3:
            self.find_tree_from_input()
        elif inp == 4:
            print(f"Total tree's count: {self.total_trees_count()}")
        elif inp == 5:
            print(f"Total healthy tree's count: {self.total_healthy_trees_count()}")
        elif inp == 6:
            print(f"Sickness percentage: {self.sick_percentage()}%")
            print(self.sort_by_sick())
        elif inp == 7:
            print("Specific info:\n")
            self.specific_info()
        elif inp == 8:
            self.pickle_dump(self.forest)
            self.csv_writer(self.forest)
        elif inp == 9:
            print("Pickle result: ")
            print(f"{self.pickle_load()}\n\n")
            print("CSV result: ")
            self.csv_reader()


if __name__ == "__main__":
    Task1().start()