from stats import count_words
import sys

def main():
    if len(sys.argv) < 2:
        print('Please provide a path to a file. Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_text(path_to_file)
    num_words = count_words(text)
    chars = count_characters(text)
    make_report(path_to_file, num_words, chars_dict_to_sorted_list(chars))


def get_text(path):
    with open(path) as f:
        return f.read()
    



def count_characters(text):
    char_count = {}
    for char in text:
        char_low = char.lower()
        if char_low in char_count:
            char_count[char_low] +=1
        else:
            char_count[char_low] = 1
    return char_count


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(chars):
    chars_list = [{'char': char, 'num': chars[char]} for char in chars]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


def make_report(path, num_words, chars_list):
    print(f'--- Begin report of {path} ---')
    print(f'{num_words} words found in the document')
    print('')
    for char in chars_list:
        character = char['char']
        if character.isalpha():
            print(f"Character '{character}' was found {char['num']} times")
    print('--- End report ---')


main()


