from utils import task_starter  # noqa


def count_words_starting_with_lowercase(text: str):
    """
    :param text: input string
    Returns count of words that start with lowercase
    """
    counter = 0
    words = text.split(" ")
    try:
        for word in words:
            if word[0].islower():  # Check the first symbol of each word.
                counter += 1
        return [counter]
    except IndexError:
        print(
            "Index error occurred! "
            "May be you have been pressed two spaces in a row?"
        )


#  task_starter(count_words_starting_with_lowercase,
#             message=["Number of words starting with lowercase:"])
