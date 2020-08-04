#!/usr/bin/env python
from __future__ import print_function
import doctest


"""

CANDIDATE NAME: (put your name here please)

Your task is to fill out the following two functions according to the
instructions found in their documentation strings.  Please don't forget
to put your name in the space above.

You may:
    * write any extra functions or classes you wish to use in order
      to implement these functions

You may not:
    * rename either of these functions
    * change the name of the parameter "some_integer_input"
    * add any additional parameters to either of the functions
    * import any functions not included in the python standard library
    * write any code in another python file (all of your code should
      be within this file that way it's easier for us to test your result)

Good Luck!
"""


def reverse(some_integer_input):
    """Returns the reverse of the integer provided as input.

    The "reverse" of a positive integer is found by reversing the order
    of the digits in the integer and removing any leading zeros after
    the reversal.

    For instance:

    >>> reverse(3210)
    123

    >>> reverse(321)
    123

    >>> reverse(5243)
    3425
    """
    pass


def next_higher_number(some_integer_input):
    """
    Given an integer, this function returns the next higher number which
    has the exact same set of digits. If no higher number exists, return
    the the integer provided as input.

    For instance:

    >>> next_higher_number(123)
    132

    >>> next_higher_number(1232)
    1322

    >>> next_higher_number(70)
    70
    """
    pass


if __name__ == '__main__':
    # test the functions using python's doctest module
    # https://docs.python.org/3.4/library/doctest.html
    doctest.testmod()


