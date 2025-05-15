from utils import task_starter  # noqa

task_text = (
    "So she was considering in her own mind, as well as she could,"
    " for the hot day made her feel very sleepy and stupid, whether"
    " the pleasure of making a daisy-chain would be worth the trouble"
    " of getting up and picking the daisies, when suddenly a White"
    " Rabbit with pink eyes ran close by her."
)


def get_task_text():
    return task_text


def sting_task(text: str):
    """
    Returns:
        a) number of words in a line
        b) the longest word and its sequence number
    Prints only non-even words
    """
    words = text.split(" ")
    words_counter = len(words)

    the_longest_word = max(words, key=len)
    the_longest_word_index = words.index(the_longest_word)

    print("NON-EVEN WORDS:", *(w for i, w in enumerate(words) if i % 2 == 0))
    return [words_counter, the_longest_word, the_longest_word_index]


task_starter(sting_task, get_task_text, message=[
    "Total words count:",
    "The longest word is ",
    "Its index is "
])
