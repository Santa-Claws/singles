
import os
import re
import json


def read_book(book_dict, rev_book_dict):
    if not os.path.exists('Contact_Book.json'):
        print('no current book to read')
        exit()
    phone_num_regex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')

    if not os.path.exists('Contact_Book.json'):
        print('no current book to read')

    while True:
        search_input = input('who do you want to search for\n(enter full name or number(no spaces))\nif you want to '
                             'display whole book '
                             'press enter\nwhen done then type done\n')
        phone_num = phone_num_regex.search(search_input)
        if search_input == 'done':
            break
        if phone_num:
            rev_book = open('Contact_Book_Rev.json', 'r')
            rev_book_dict = json.load(rev_book)
            rev_searched_item = rev_book_dict.get(search_input)
            print(f'The Name for {search_input} is {rev_searched_item}\n\n')
        else:
            if search_input:
                book = open('Contact_Book.json', 'r')
                book_dict = json.load(book)
                searched_item = book_dict.get(search_input)
                print(f'The Number for {search_input} is {searched_item}\n\n')
            else:
                book = open('Contact_Book.json', 'r')
                book_dict = json.load(book)
                print(json.dumps(book_dict, indent=2))







def write_book(book_dict, rev_book_dict):
    phone_num_regex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
    while True:
        num_list = []
        name_list = []
        print('when done giving name and number then press enter when asked whats the name')
        while True:
            name_input = input('whats the name\n')
            if not name_input:
                break
            number_input = input('whats the number\n(no spaces or dashes)\n')
            phone_num = phone_num_regex.search(number_input)
            if not phone_num:
                print('not a valid phone number')
                exit()
            num_list.append(number_input)
            name_list.append(name_input)
            if len(name_list) != len(num_list):
                print('error\nnot all names have a number')
                exit()
        if os.path.exists('Contact_Book.json'):
            if os.stat('Contact_Book.json').st_size == 0:
                book_dict = {}
                rev_book_dict = {}
            else:
                rev_book = open('Contact_Book_Rev.json', 'r')
                book = open('Contact_Book.json', 'r')
                book_dict = json.load(book)
                rev_book_dict = json.load(rev_book)
                rev_book.close()
                book.close()
            book = open('Contact_Book.json', 'w')
            rev_book = open('Contact_Book_Rev.json', 'w')
            name_num_list = zip(name_list,num_list)
            for name, num in name_num_list:
                book_dict[name] = num
                rev_book_dict[num] = name
            f = json.dumps(book_dict, indent=2)
            g = json.dumps(rev_book_dict, indent=2)
            book.write(f)
            rev_book.write(g)
            book.close()
            rev_book.close()
            break
        elif not os.path.exists('Contact_Book.json'):
            book = open('Contact_Book.json', 'w')
            rev_book = open('Contact_Book_Rev.json', 'w')
            name_num_list = zip(name_list, num_list)
            for name, num in name_num_list:
                book_dict[name] = num
                rev_book_dict[num] = name
            f = json.dumps(book_dict, indent=2)
            g = json.dumps(rev_book_dict, indent=2)
            rev_book.write(g)
            book.write(f)
            book.close()
            rev_book.close()
            break


rev_book_dic = {}
book_dic = {}
while True:
    read_write = input('do ya wanna read or write to the book\nr for read, w for write\n')
    if read_write == 'r':
        read_book(book_dic, rev_book_dic)
        break
    if read_write == 'w':
        write_book(book_dic, rev_book_dic)
        break
    else:
        print('not valid')


