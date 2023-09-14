"""
Main cli or app entry point
"""

from mylib.calculator import add

def add_two_sum(a, b):
    add(a,b)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    print(add_two_sum(1,2))