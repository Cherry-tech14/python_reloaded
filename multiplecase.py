def convert_multiple_upper(sentence):
    words = sentence.split()

    for index, word in enumerate(words):
        if word == "(up,":
            count = words[index + 1]
            count = int(count.replace(")", ""))

            for i in range(index - count, index):
                upper = words[i]
                converted = upper.upper()
                words[i] = converted
            words.remove(words[index + 1])
            words.remove("(up,")
           
    result = " ".join(words)
    return result

def convert_multiple_lower(sentence):
    words = sentence.split()

    for index, word in enumerate(words):
        if word == "(low,":
            count = words[index + 1]
            count = int(count.replace(")", ""))

            for i in range(index - count, index):
                lower = words[i]
                converted = lower.lower()
                words[i] = converted
            words.remove(words[index + 1])
            words.remove("(low,")
    result = " ".join(words)
    return result

def convert_multiple_cap(sentence):
    words = sentence.split()

    for index, word in enumerate(words):
        if word == "(cap,":
            count = words[index + 1]
            count = int(count.replace(")", ""))

            for i in range(index - count, index):
                capitalize = words[i]
                converted = capitalize.capitalize()
                words[i] = converted
            words.remove(words[index + 1])
            words.remove("(cap,")
    result = " ".join(words)
    return result