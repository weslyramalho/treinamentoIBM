
with open("arquivo.txt") as fh:
    count = 0
text = fh.read()
for caracter in text:
    if caracter.isupper():
        count += 1