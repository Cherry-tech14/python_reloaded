def fix_punctuation(sentence):
    punctuations = ".,!?:;"

    for mark in punctuations:
        sentence = sentence.replace(" " + mark, mark)
    return sentence