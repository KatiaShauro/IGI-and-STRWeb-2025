import re

from tasks.task2 import FileManager


def load_default_text():
    return FileManager("task2").read()


class Regular:
    file_text = load_default_text()

    @staticmethod
    def get_sentence_count():
        """Returns sentence completion signs"""
        return re.findall('[.!?]+', Regular.file_text)

    @staticmethod
    def get_point_sentences():
        return re.findall('[.]{1,3}', Regular.file_text)

    @staticmethod
    def get_exclamation_sentences():
        return re.findall(r'!', Regular.file_text)

    @staticmethod
    def get_question_sentences(self):
        return re.findall(r'[?]', Regular.file_text)

    @staticmethod
    def get_sent_average_len():
        """Returns average sentence's length (in symbols)"""
        sentences = re.split(r'[.!?]', Regular.file_text)
        sentences = [s.strip() for s in sentences if s.strip()]
        lengths = []
        for sentence in sentences:
            words = re.findall(r'\w+', sentence)
            total_chars = sum(len(word) for word in words)
            lengths.append(total_chars)

        return sum(lengths) / len(lengths) if lengths else 0

    @staticmethod
    def get_word_average_len():
        """Returns average word's length (in symbols)"""
        words = re.findall(r'\w+', Regular.file_text)
        total_length = sum(len(word) for word in words)
        return total_length / len(words)

    @staticmethod
    def get_smiles():
        """Returns emoticons"""
        smiles = re.findall('([;:])(-*)([()\[\]])\3*', Regular.file_text)
        return [''.join(match) for match in smiles]

    @staticmethod
    def get_words_start_with_small_consonant():
        return re.findall(r'\b[^aeiou_A-Z\W\d]\w*', Regular.file_text)

    @staticmethod
    def check_is_valid_auto_number():
        number = input("\nEnter auto number: ")
        return (re.match('[0-9]{4}[ABEIKMHOPCTX]{2}-[1-7]', number)
                is not None and len(number) == 8)

    @staticmethod
    def get_minimal_len_word_count():
        words = re.findall(r'\w+', Regular.file_text)
        smallest = min(len(word) for word in words)
        return [word for word in words if len(word)==smallest]

    @staticmethod
    def get_words_with_commas():
        """Returns words followed by a comma"""
        return re.findall(r'\w+(?=,)', Regular.file_text)

    @staticmethod
    def get_the_longest_with_y():
        """Returns the longest word ending in y"""
        ys = re.findall(r'\w+y\b', Regular.file_text)
        return max(ys, key=len)

