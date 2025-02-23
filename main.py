from stats import count_words, chars_dict_to_sorted_list
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
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

    


def count_characters(text):
    char_count = {}
    for char in text:
        char_low = char.lower()
        if char_low.isalpha():  # Only count letters
            if char_low in char_count:
                char_count[char_low] += 1
            else:
                char_count[char_low] = 1
    return char_count



def make_report(path, num_words, chars_list):
    print(f'--- Begin report of {path} ---')
    print(f'Found {num_words} total words')
    print('')
    for char in chars_list:
        character = char['char']
        if character.isalpha():
            print(f"{character}: {char['num']}")
    print('--- End report ---')


main()


