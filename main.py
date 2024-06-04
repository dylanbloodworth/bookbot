#! /usr/bin/python3

def main():
#    print('What book?')
#    book : str = f"books/{input()}.txt"
    book = 'books/frankenstein.txt'
    content : str = get_book_contents(book)        
    
    words : int = len(split_content(content))
    count = count_chars(content)
    
    report(words, count)






def get_book_contents(path : str) -> str:
    with open(path) as f:
        return f.read()

def split_content(text : str) -> list:
    word_array : list = text.split()
    return word_array

def count_chars(words : list) -> dict:
    words = words.lower()
    counting = {}
    for letter in words:
        if letter in counting:
            counting[letter] += 1
        else:
            counting[letter] = 1
    return counting

def report(word_count : int, chars_count : dict):
    print(f"--- Begin report of books/frankenstein ---")
    print(f"{word_count} words found in the document")
    print("")
    
    temp_list = sort_chars(chars_count)

    for i in range(0, len(temp_list)):
        current_dict = temp_list[i]
        print(f"The '{current_dict['letter']}' character was found {current_dict['count']} times")

def sort_chars(chars_count):
    temp_list = []
    for key in chars_count:
        if key.isalpha():
            temp_list.append({'letter' : key, 'count' : chars_count[key]})
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list

def sort_on(e):
    return e['count']

main()
