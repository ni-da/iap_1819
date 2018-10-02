def cleanup_spaces(ss):
    words = ""
    word = ""
    ss += "  "
    for i in ss:
        if i != " ":
            word += i
        else:
            if word != "":
                words += word + " "
                word = ""

    return (words)


print(cleanup_spaces("A  simple example  string !"))
