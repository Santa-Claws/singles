from random import choice
from typing import List

print('this is a probabilty sim')
what_to_calc = input('you can calculate d for dice or c for coins\n')


def dice(event_nums: List[int]):
    amount_input = input('how many time do you want to roll\n')
    numbers_rolled = []
    number_of_rolls = []
    suceeded_rolls = []

    for i in range(0, int(amount_input)):
        dice_numbers = [1, 2, 3, 4, 5, 6]
        number = choice(dice_numbers)
        numbers_rolled.append(number)
        if numbers_rolled[0] in event_nums:
            suceeded_rolls.append('suceeded')
        number_of_rolls.append('roll')
        numbers_rolled = []

    print(f'the amount of suceeded rolls are {len(suceeded_rolls)}')
    print(f'the fraction representing for the roles is {len(suceeded_rolls)}/{len(number_of_rolls)}')


def coin(heads_tails: List[str]):
    num_of_flips = input('how many times do you want to flip\n')
    list_of_flips = []
    flips_list = []
    sucessful_flips = []
    for i in range(0, int(num_of_flips)):
        possible_flips = ['h','t']
        flip = choice(possible_flips)
        list_of_flips.append(flip)
        flips_list.append(flip)
        if flips_list[0] in heads_tails:
            sucessful_flips.append('sucess!')
        flips_list = []
    print(f'the amount of suceeded flips are {len(sucessful_flips)}')
    print(f'the fraction resemblence of flips is {len(sucessful_flips)}/{len(list_of_flips)}')
    if heads_tails == 'h':
        print(f'the number of heads is {len(sucessful_flips)}')
        print(f'the number of tails is {(int(num_of_flips) - len(sucessful_flips))}')
    else:
        print(f'the number of tails is {len(sucessful_flips)}')
        print(f'the number of heads is {(int(num_of_flips) - len(sucessful_flips))}')


event_numbers = []
event_flips = []
if what_to_calc == 'd':
    for i in range(0, 7):
        event_number = input('what numbers do you want to track\n(press enter when done)\n')
        if event_number == '':
            break
        else:
            event_numbers.append(int(event_number))
    dice(event_numbers)
elif what_to_calc == 'c':
    event_flip = input('what do you want to track\n(h for heads and t for tails)\n')
    event_flips.append(event_flip)
    coin(event_flips)
