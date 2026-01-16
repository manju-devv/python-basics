list_to_strip = ["apple", "app", "bananaapp", "pineapple", "grape"]


def strip_list(list, word):
    new_list = []
    for item in list:
        if not (item == word):
            new_list.append(item.strip(word))
    return new_list


print(strip_list(list_to_strip, "app"))
