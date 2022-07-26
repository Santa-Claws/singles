# still figureing it out
# not ready tp run
import os
import re
import json


def read_book(book_dict):
    search_input = input('who do you want to search for\n(enter full name)\nif you want to display whole book '
                         'press enter')


def write_book(book_dict):
    phone_num_regex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
    while True:
        name_input = input('whats the name\n')
        number_input = input('whats the number\n(no spaces or dashes)\n')
        phone_num = phone_num_regex.search(number_input)

        if phone_num:
            if os.path.exists('Contact_Book.json'):
                if os.stat('Contact_Book.json').st_size == 0:
                    book_dict = {}
                else:
                    book = open('Contact_Book.json', 'r')
                    book_dict = json.load(book)
                    book.close()
                book = open('Contact_Book.json', 'w')
                book_dict[name_input] = number_input
                f = json.dumps(book_dict, indent=2)
                book.write(f)
                book.close()
                break
            elif not os.path.exists('Contact_Book.json'):
                book = open('Contact_Book.json', 'w')
                book_dict[name_input] = number_input
                f = json.dumps(book_dict, indent=2)
                book.write(f)
                book.close()
                break
        elif not phone_num:
            print('not a valid number')
            continue


book_dic = {}
write_book(book_dic)

# use os to check excisting file and if no excisting file write if excisting file then append
