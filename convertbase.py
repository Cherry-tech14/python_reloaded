def convert_hexadecimal(sentence):
    words = sentence.split()

    for index, word in enumerate(words):
        if word == "(hex)":
            number = words[index - 1]
            converted = int(number, 16)
            words[index - 1] = str(converted)
            words.remove("(hex)")
    
    result = " ".join((words))
    return result



def convert_binary(sentence):
    words = sentence.split()
    for index, word in enumerate(words):
        if word == "(bin)":
            number = words[index - 1]
            converted = int(number, 2)
            words[index - 1] = str(converted)
            words.remove("(bin)")
    result = " ".join((words))
    return result
