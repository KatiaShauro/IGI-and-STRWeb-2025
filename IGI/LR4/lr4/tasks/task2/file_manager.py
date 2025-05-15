import os
from datetime import datetime
from zipfile import ZipFile


class FileManager:
    def __init__(self, filename: str):

        project_dir = os.path.dirname(os.path.abspath(__file__))
        self.input_filename = os.path.join(project_dir, filename + "_input.txt")
        self.output_filename = os.path.join(project_dir, filename + "_output.txt")
        self.filename = filename + "_output.txt"


    def read(self):
        """Read text from file"""
        with open(self.input_filename, "r") as fh:
            a = fh.read()
            print(a)
            return a


    def write(self, obj):
        """Clears the file and writes the result"""
        st = obj.__str__()
        with open(self.output_filename, "w+") as fh:
            fh.write(st + "\n")


    def archive(self):
        """Make an archive"""
        with ZipFile("task2.zip", "w") as zipfile:
            zipfile.write( self.filename)
            print("Archive created!")


    def get_archive_info(self):
        """Get information (name, size, date) about the archive"""
        with ZipFile("task2.zip", "r") as zipfile:
            z = zipfile.getinfo(self.filename)
            print(f"File name: {z.filename}\nFile size: {z.file_size}\n"
                  f"Date: {datetime(*z.date_time).strftime("%Y-%m-%d %H:%M:%S")}")

