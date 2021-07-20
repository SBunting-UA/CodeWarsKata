def caesar_encode(phrase, shift):
    key = shift
    input = phrase.lower()
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if key > 26:
        key = key % 26
        
    for char in input:
        if char == ' ':
            key += 1
            result = result + ' '
        else:
            position = alphabet.find(char)
            counter = (position + key) % 26
            result = result + alphabet[counter]
    
    return result