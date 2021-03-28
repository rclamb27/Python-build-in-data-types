#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-9-16
#rclamb27@cus.fullerton.edu
"""Ouputs the sum of all multiples of 3 or 5 below 10000000"""


def main():
    """Takes the multiples of 3 and 5 and sums them"""
    total_nums = input('Please input a range of numbers below 1000000: ')
    print('You chose {} as the range.'.format(total_nums))
    mult_3 = set(range(0, int(total_nums), 3))
    mult_5 = set(range(0, int(total_nums), 5))
    intersection = mult_3 | mult_5
    print('The sum of all the multiples of 3 or 5 below 1000000 is {}'.format(sum(intersection)))


if __name__ == '__main__':
    main()
