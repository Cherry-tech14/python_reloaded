def convert_uppercase(sentence):
    words = sentence.split()
    for index, word in enumerate(words):
        if word == "(up)":
            upper = words[index - 1]
            converted = upper.upper()
            words[index - 1] = converted
            words.remove("(up)")
    result = " ".join((words))
    return result


def convert_lowercase(sentence):
    words = sentence.split()
    for index, word in enumerate(words):
        if word == "(low)":
            lower = words[index - 1]
            converted = lower.lower()
            words[index - 1] = converted
            words.remove("(low)")
    result = " ".join((words))
    return result

def convert_cap(sentence):
    words = sentence.split()
    for index, word in enumerate(words):
        if word == "(cap)":
            capitalize = words[index - 1]
            converted = capitalize.capitalize()
            words[index - 1] = converted
            words.remove("(cap)")
    result = " ".join((words))
    return result