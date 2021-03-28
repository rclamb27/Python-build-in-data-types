#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-9-16
#rclamb27@cus.fullerton.edu
"""Ouputs the sum of all multiples of 3 or 5 below 10000000"""


def main():
    """Takes the multiples of 3 and 5 and sums them"""
    total_nums = int(input('Please input a range of numbers below 1000000: '))
    print('You chose {} as the range.'.format(total_nums))
    lst_3 = range(3, total_nums, 3)
    lst_5 = range(5, total_nums, 5)
    final_list = []
    for i in lst_3:
        final_list.append(i)
    for i in lst_5:
        if not i in lst_3:
            final_list.append(i)


    print('The sum of all the multiples of 3 or 5 below 1000000 is {}'.format(sum(final_list)))


if __name__ == '__main__':
    main()
