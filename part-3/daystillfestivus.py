#!/usr/bin/env python3
#
# Ryan Lamb
# CPSC 223P-03
#2020-9-18
#rclamb27@cus.fullerton.edu
"""Takes a year and calculates the next time for festivus"""
import sys
import datetime
def main():
    """Takes an argument and calculates when festivus happens"""
    list = sys.argv
    if len(list) == 1 or not list[1].isdigit():
        print('Please proivde a year as an argument.')
        sys.exit()
    else:
        year = int(list[1])
    festivus = datetime.datetime(year, 12, 23)
    current = datetime.datetime.now()
    if festivus < current:
        print('Festivus {} has passed.'.format(year))
        sys.exit()
    elif festivus == current:
        print('Festivus {} is today!'.format(year))
    time_between = festivus - current
    print('There are {} days until Festivus {}!'.format(time_between.days, year))

if __name__ == '__main__':
    main()
