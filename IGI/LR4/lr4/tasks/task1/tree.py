from utils.errors import InvalidNameError, InvalidCountError, InvalidHealthyCountError, InvalidTreeError


class Tree:
    species_counter = 0
    def __init__(self, name: str, total_count: int = 0, healthy_count: int = 0):
        try:
            self.name = name
            self.total_count = total_count
            self.healthy_count = healthy_count
            Tree.species_counter += 1
        except (InvalidNameError, InvalidCountError, InvalidHealthyCountError) as e:
            raise InvalidTreeError(e)


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, new_name: str):
        if not new_name or new_name[0].isdigit():
            raise InvalidNameError(new_name)
        self.__name = new_name


    @property
    def total_count(self):
        return self.__total_count


    @total_count.setter
    def total_count(self, new_count: int):
        if not new_count or new_count < 0:
            raise InvalidCountError(new_count)
        self.__total_count = new_count


    @property
    def healthy_count(self):
        return self.__healthy_count


    @healthy_count.setter
    def healthy_count(self, new_count: int):
        # If healthy count is bigger than total
        if not new_count or new_count < 0 or self.__total_count < new_count:
            raise InvalidHealthyCountError(new_count)
        self.__healthy_count = new_count


    def get_sick_percentage(self):
        """Returns percents of sick trees of special kind"""
        return round(((self.__total_count - self.__healthy_count) / self.__total_count * 100), 5)


    def total_trees_species(self):
        return self.species_counter


    def __str__(self):
        return (f"Tree '{self.name}': total - {self.total_count}, healthy - {self.healthy_count}")


    def __repr__(self): # It's need for dictionary {str : Tree}
        return self.__str__()

