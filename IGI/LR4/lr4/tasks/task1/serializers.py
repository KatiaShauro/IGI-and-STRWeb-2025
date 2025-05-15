import csv
import os
import pickle

from tasks.task1 import Forest


class SerializerMixin:
    def __init__(self, filename: str = "task1", *args, **kwargs):
        super().__init__(*args, **kwargs)
        project_dir = os.path.dirname(os.path.abspath(__file__)) # Getting current directory
        self.pickle_name = os.path.join(project_dir, filename + "_pickle.txt")
        self.csv_name = os.path.join(project_dir, filename + "_csv.txt")


    def pickle_dump(self, forest : Forest):
        """Write a forest into file using pickle"""
        with open(self.pickle_name, "wb") as fh:
            pickle.dump(forest, fh)


    def pickle_load(self):
        """Load a forest from file using pickle"""
        with open(self.pickle_name, "rb") as fh:
            return pickle.load(fh)


    def csv_writer(self, forest: Forest):
        """Write a forest into file using csv"""
        with open(self.csv_name, "w") as fh:
            writer = csv.DictWriter(fh,
                                    fieldnames=["dict_name", "real_name", "total_count", "healthy_count"],
                                    quoting=csv.QUOTE_ALL
                                    )
            writer.writeheader()
            for key, value in forest.items():
                writer.writerow(dict(dict_name=key, real_name=value.name,
                                     total_count=value.total_count,
                                     healthy_count= value.healthy_count))


    def csv_reader(self):
        """Load a forest from file using csv"""
        with open(self.csv_name, "r") as fh:
            reader = csv.DictReader(fh)
            rows = list(reader)
        for r in rows:
            print(r, '\n')
        return rows