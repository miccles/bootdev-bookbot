def main():
    path_to_file = 'books/frankenstein.txt'
    text = get_text(path_to_file)
    # print(text)
    num_words = count_words(text)
    print(f'Number of words found: {num_words}')
    letters = count_characters(text)
    print(letters)


def get_text(path):
    with open(path) as f:
        return f.read()
    

def count_words(text):
    text_split = text.split()
    return len(text_split)


def count_characters(text):
    letter_count = {}
    for char in text:
        char_low = char.lower()
        if char_low in letter_count:
            letter_count[char_low] +=1
        else:
            letter_count[char_low] = 1
    return letter_count


main()


