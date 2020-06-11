"""
doulma

A Light Weight Python Utility Library,
Created By HussainARK

GitHub: https://github.com/HussainARK/doulma
"""
from . import exceptions
from . import variables
from . import cli
from . import network
from . import hashing


def make_delay(seconds: int) -> None:
    import time
    """
	make_delay
	~~~~~~~~~~~~~~~~~~~
	
	"The First Function in the doulma Library".
	waits for some time
	
	
	:param seconds: how much seconds to wait.
	:return: Nothing "None"
	"""

    try:
        time.sleep(seconds)
    except TypeError:
        raise exceptions.InvalidArgument(':seconds: must be a Number')


def make_delay(seconds: float) -> None:
    import time
    """
	make_delay
	~~~~~~~~~~~~~~~~~~~
	
	"The First Function in the doulma Library".
	waits for some time
	
	
	:param seconds: how much seconds to wait.
	:return: Nothing "None"
	"""

    try:
        time.sleep(seconds)
    except TypeError:
        raise exceptions.InvalidArgument(':seconds: must be a Number')


def gen_password(strength_level: int = 87) -> str:
    import string
    import random

    """
	gen_password
	~~~~~~~~~~~~
	
	:param strength_level: the Strength Level of the Password, default is 87
	:return: A String that represents the Password
	"""

    used_letters = []
    used_capital_letters = []
    used_small_letters = []
    used_digits = []

    for _ in range(strength_level):
        used_letters.append(random.choice(string.ascii_letters))

    for _ in range(strength_level):
        used_capital_letters.append(random.choice(string.ascii_uppercase))

    for _ in range(strength_level):
        used_small_letters.append(random.choice(string.ascii_lowercase))

    for _ in range(strength_level):
        used_digits.append(random.choice(string.digits))

    mix = []

    for _ in range(strength_level):
        mix.append(
            random.choice(
                random.choice(
                    random.choice(
                        random.choice(
                            random.choice(
                                used_digits +
                                used_letters +
                                used_small_letters +
                                used_capital_letters +
                                used_digits +
                                used_capital_letters +
                                used_small_letters +
                                used_letters
                            )
                        )
                    )
                )
            )
        )

    return ''.join(mix)
