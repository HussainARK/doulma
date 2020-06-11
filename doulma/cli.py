from . import exceptions
from types import FunctionType


def ask_to_select(message: str, first_option: str, second_option: str) -> str:
    """
    ask_to_select
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A function that displays a mmessage and then asks the User to input ont of two values,
    it returns the selected value.
    in this format: "*question* [*first_option*/*second_option*] "


    :param messsage: A Message to Display
    :param first_option: A String Value for the First Option
    :param second_option: A String Value for the Second Option
    :return: A String that represents the Answer (one of the given options)
    """
    try:
        answer = input(f"{message} [{first_option}/{second_option}] ")
        while (answer != first_option) and (answer != second_option):
            answer = input(
                f'Please Enter either "{first_option}" or "{second_option}": ')
        return answer
    except TypeError:
        raise exceptions.InvalidArgument(
            ":message:/:first_option:/:second_option: must be a String")


def ask_to_select_then_run(message: str, first_option: str, second_option: str, first_callback: FunctionType, second_callback: FunctionType) -> None:
    """
    ask_to_select_then_run
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A function that displays a mmessage and then asks the User to input ont of two values.
    in this format: "*question* [*first_option*/*second_option*] "

    :param messsage: A Message to Display
    :param first_option: A String Value for the First Option
    :param second_option: A String Value for the Second Option
    :param first_callback: A Function that runs when the First Option is selected
    :param second_callback: A Function that runs when the Second Option is selected
    :return: Nothing "None"
    """
    try:
        answer = input(f"{message} [{first_option}/{second_option}] ")
        while (answer != first_option) and (answer != second_option):
            answer = input(
                f'Please Enter either "{first_option}" or "{second_option}": ')
        if answer == first_option:
            first_callback()
        else:
            second_callback()

    except TypeError:
        raise exceptions.InvalidArgument(
            ":message:/:first_option:/:second_option: must be a String")


def clear():
    import os
    import platform
    """
	clear
	~~~~~
	
	It clears the Terminal Screen
	
	:return: None!
	"""
    if platform.system() != "Windows":
        os.system('clear')
    else:
        os.system('cls')
