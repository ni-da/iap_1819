prefixes = "JKLMNOPQ"
suffix = "ack"
for p in prefixes:
    if p == "Q" or p == "O":
        print(p + "u" + suffix)
    else:
        print(p + suffix)
