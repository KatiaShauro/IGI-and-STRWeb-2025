from typing import Dict

from tasks.task1 import Tree
from utils.errors import InvalidTreeError

init_forest = {
    "fir" : Tree("Fir", 150, 146),
    "pine_tree": Tree("Pine tree", 124, 100),
    "oak" : Tree("Oak", 54, 52),
    "maple": Tree("Maple", 25, 17),
    "birch": Tree("Birch", 28, 25)
}

class Forest:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.forest: Dict[str, Tree] = init_forest


    @property
    def forest(self):
        return self.__forest


    @forest.setter
    def forest(self, frst: Dict[str, Tree]):
        if not isinstance(frst, dict):
            raise TypeError("The dictionary must be passed")
        if not all(isinstance(v, Tree) for v in frst.values()):
            raise TypeError("All values must be of the 'Tree' type.")
        self.__forest = frst.copy()


    def add_tree_from_input(self):
        """Added new type of tree to the forest from input"""
        name = input("Enter new tree name: ")
        try:
            total = int(input("Enter total tree count: "))
            healthy = int(input("Enter healthy trees count: "))
            tree = Tree(name, total, healthy)
        except ValueError:
            print(
                "\n---[INPUT ERROR]---\n"
                "Tree count must be int! Failed to add tree"
                )
            return
        except InvalidTreeError as e:
            print(f"\n---[ERROR]---\n{e}\nFailed to add tree\n")
            return

        tree_name = name.lower().replace(' ', '_')
        self.forest[tree_name] = tree
        print("Tree successfully added!")


    def total_trees_species(self):
        return self.forest['fir'].total_trees_species()


    def total_trees_count(self):
        count = 0
        for tree in self.forest.values():
            count += tree.total_count
        return count


    def total_healthy_trees_count(self):
        count = 0
        for tree in self.forest.values():
            count += tree.healthy_count
        return count


    def sick_percentage(self):
        return round((self.total_trees_count() - self.total_healthy_trees_count())
                     / self.total_trees_count() * 100, 5)


    def find_tree_from_input(self):
        name = input("Enter tree name: ")
        tree = next((inst for inst in self.forest.values() if inst.name == name), None)
        if tree:
            print(f"Tree {name} is here.\n{tree}")
        else:
            print("Tree is not found")


    def show_all_forest(self):
        """Displays all trees in forest"""
        for tree in self.forest.values():
            print(tree)


    def specific_info(self):
        """Shows information about specific type's percentage of tree"""
        total = self.total_trees_count()
        for tree in self.forest.values():
            print(f"{tree}. {tree.get_sick_percentage()}% - sick percentage. "
                  f"Makes up {round((tree.total_count / total * 100), 5)}% of all species")


    def sort_by_sick(self):
        """Sorts trees in descending order of the number of diseased trees"""
        fst = sorted(
            self.forest.values(),
            key=lambda tree: tree.total_count - tree.healthy_count,
            reverse=True
        )
        print("\nTREES ACCORDING TO SICKNESS:")
        for tree in fst:
            print(tree)

