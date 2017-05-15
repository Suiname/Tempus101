def toonify(accent, sentence):
    result = ''
    if accent == 'daffy':
        for letter in sentence:
            if letter == 's':
                result += 'th'
            else:
                result += letter
    elif accent == 'elmer':
        for letter in sentence:
            if letter == 'r':
                result += 'w'
            else:
                result += letter
    else:
        result = sentence
    return result