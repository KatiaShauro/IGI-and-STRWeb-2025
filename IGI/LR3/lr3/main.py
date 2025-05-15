from tasks import (taylor_series, even_nums_average,
                   count_words_starting_with_lowercase,
                   sting_task, float_list_task, get_task_text)
from utils import (task_number_input_validator, task_starter,
                   epsilon_and_x_validator, user_input_init,
                   my_generator, infinity_method)


@infinity_method
def main():
    """
    Main func of lab work №3 was developed by
    student gr.353502 Shauro Ekaterina, 01.04.2025
    """
    print("Select task number: ")
    i = task_number_input_validator()

    print(f"\tSTARTING TASK {i}")
    if i == 1:
        task_starter(taylor_series, epsilon_and_x_validator)
    elif i == 2:
        task_starter(even_nums_average, user_input_init,
                     ["Average of even nums:"])
    elif i == 3:
        task_starter(count_words_starting_with_lowercase,
                     message=["Number of words starting with lowercase:"])
    elif i == 4:
        task_starter(sting_task, get_task_text, message=[
            "Total words count:",
            "The longest word is ",
            "Its index is "
        ])
    elif i == 5:
        task_starter(float_list_task, my_generator, message=[
            "The sum of the negative list items: ",
            "The product of the elements located between "
            "the maximum and minimum elements: "
        ])
    print(f"\tEND OF TASK {i}")


if __name__ == "__main__":
    main()
