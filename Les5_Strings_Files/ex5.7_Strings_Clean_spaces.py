def cleanup_spaces(ss):
    words = ""
    word = ""
    ss += "  "
    j = 0
    while j < len(ss):
        i = ss[j]
        if i != " ":
            word += i
        else:
            if word != "":
                words += word + " "
                word = ""
        j += 1

    return words[:len(words) - 1]


print(cleanup_spaces("    "))
