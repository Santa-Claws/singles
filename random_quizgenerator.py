from random import choice, choices
import random
from typing import List
import subprocess

capital_dic={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}


def quiz_maker(capitols_question,capitols_dict):
    for q in range(0,35):
        quiz = open(f'quiz{q}.txt', 'w')
        anwsers = open(f'anwser-key{q}.txt', 'w')
        list_capitols_quiz = list(capitols_question)
        random.shuffle(list_capitols_quiz)
        quiz.write(f'Quiz Number {q}\nName\nTeacher\nPeriod\n')
        quiz.write('\n')
        anwsers.write(f'Quiz Number {q}\n')
        anwsers.write('\n')
        for num, capitol in enumerate(list_capitols_quiz):
            quiz.write(f'{num + 1}. {capitol}\n')
            anwser = capitols_dict.get(capitol)
            anwsers.write(f'{num + 1}. {anwser}\n')
        quiz.close()
        anwsers.close()



quiz_maker(capital_dic.keys(),capital_dic)