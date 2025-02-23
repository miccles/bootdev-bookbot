
def sort_on(d):
    return d["num"]

def count_words(text):
    text_split = text.split()
    return len(text_split)


def chars_dict_to_sorted_list(chars):
    chars_list = [{'char': char, 'num': chars[char]} for char in chars]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list