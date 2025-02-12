def wordcase(word):
    u=l=0
    for w in word:
        if w.isupper():
            u+=1
        else:
            l+=1
    if u>l:
        print(word.upper())
    else:
        print(word.lower())
word = input("")
wordcase(word)
