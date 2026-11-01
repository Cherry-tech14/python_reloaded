def fix_punctuation(sentence):
    punctuations = ".,!?:;"

    for mark in punctuations:
        sentence = sentence.replace(" " + mark, mark)
    
    i = 0

    while i < len(sentence):
        char = sentence[i]

        if char in punctuations and i + 1 < len(sentence):
            next_char = sentence[i + 1]
            
            if next_char.isalnum():
                sentence = sentence[:i + 1] + " " + sentence[i + 1:]
        i += 1
       

    return sentence


