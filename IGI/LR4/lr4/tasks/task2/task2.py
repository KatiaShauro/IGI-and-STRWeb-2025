from tasks.task2 import Regular, FileManager
from utils.task_starter import infinity_method


class Task2(FileManager, Regular):
    def __init__(self, filename: str = "task2"):
        super().__init__(filename=filename)


    @infinity_method
    def start(self):
        print("Choose action:\n"
              "1 - Show text from file\n"
              "2 - Make archive\n"
              "3 - Show archive info\n"
              "4 - Show the number of sentences in the text\n"
              "5 - Show the number of sentences in each type of text separately\n"
              "6 - Show the average sentence length\n"
              "7 - Show the average word length\n"
              "8 - Show the number of smiles\n"
              "9 - Show all words starting with a lowercase consonant letter\n"
              "10 - Check the entered line for compliance with the auto number\n"
              "11 - Show number of words with the smallest length\n"
              "12 - Show all the words followed by a comma\n"
              "13 - Show the longest word that ends with 'y'")
        try:
            inp = int(input("Enter a num: "))
            if inp not in range(1, 14):
                raise ValueError("Please, choose value from 1 to 13!")
        except ValueError as e:
            print(f"\n---[ERROR]---\n{e}")
            return

        if inp == 1:
            self.read()
        elif inp == 2:
            self.archive()
        elif inp == 3:
            self.get_archive_info()
        elif inp == 4:
            res = self.get_sentence_count()
            print(f"\nThe resulting chunks: {res}\nTotal sentences count: {len(res)}")
            self.write(res.__str__())
        elif inp == 5:
            res1 = self.get_point_sentences()
            print(f"\nThe resulting chunks: {res1}\nTotal point's sentences count: {len(res1)}")

            res2 = self.get_question_sentences()
            print(f"\nThe resulting chunks: {res2}\nTotal exclamation's sentences count: {len(res2)}")

            res3 = self.get_exclamation_sentences()
            print(f"\nThe resulting chunks: {res3}\nTotal question's sentences count: {len(res3)}")
            res = res1+res2+res3
            self.write(res)
        elif inp == 6:
            res = self.get_sent_average_len()
            print(f"Average sentence length (in symbols): {round(res, 5)}")
            self.write(res)
        elif inp == 7:
            res = self.get_word_average_len()
            print(f"Average word length (in symbols): {round(res, 5)}")
            self.write(res)
        elif inp == 8:
            res = self.get_smiles()
            print(f"Smiles: {res}\nCount: {len(res)}")
            self.write(res)
        elif inp == 9:
            res = self.get_words_start_with_small_consonant()
            print(f"All words that start with a consonant letter: {res}")
            self.write(res)
        elif inp == 10:
            if Regular.check_is_valid_auto_number():
                print("Entered number is valid")
            else:
                print("Number doesn't match the format")
        elif inp == 11:
            res = self.get_minimal_len_word_count()
            print(f"Words with the smallest length: {res}\nCount: {len(res)}")
            self.write(res)
        elif inp == 12:
            res = self.get_words_with_commas()
            print(f"Words with commas after: {res}")
            self.write(res)
        elif inp == 13:
            res = self.get_the_longest_with_y()
            print(f"The longest word with 'y' at the end: {res}")
            self.write(res)


if __name__ == "__main__":
    Task2().start()