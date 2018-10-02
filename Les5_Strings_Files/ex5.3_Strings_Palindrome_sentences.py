import string


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def get_only_alpha(s):
    only_alpha = ""
    for letter in s:
        if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
            only_alpha += letter
    return only_alpha


def is_palindrome_sentence(sentence):
    is_palindrome = True
    sentence = get_only_alpha(sentence)

    sentence = sentence.lower()
    print(sentence)
    # sentence = sentence.replace(" ", "")
    senLen = len(sentence)
    counter = -1
    for i in range(senLen - 1):
        if sentence[i] != sentence[counter]:
            is_palindrome = False
            break
        else:
            counter -= 1

    return is_palindrome


sentence = "Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era."
# sentence = remove_punctuation(sentence)
print(is_palindrome_sentence(sentence))
