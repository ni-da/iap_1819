import string


def count_words(ss):
    words = []
    word = ""
    # ss += " "
    inWord = False
    counter = 0
    for i in ss:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            # word += i
            inWord = True
        else:
            if (inWord):
                counter += 1
            inWord = False

        # if word != "":
        #     words.append(word)
        #     word = ""

    return counter


print(count_words("five 6 seven,eight!nine"))

# bij het beginnen van een word, boolean op True.
# Bij het einden van het word.
