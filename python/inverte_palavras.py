def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

if __name__ == "__main__":
    input = "inverter palavras em uma determinada cadeia"
    print(rev_sentence(input))