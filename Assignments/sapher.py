import sys


def validate_input(s):
    if len(s) < 5:
        return False
    else:
        return True


def convert_to_code(s):
    code = (ord(s) - 97) % 26
    return code


def convert_to_char(code):
    char = (code + 97)
    return chr(char)


def process_input(s):
    if validate_input(s):
        if s[1] == "encode":
            return encode_msg(s)
        else:
            return decode_msg(s)


def encode_msg(s):
    encoded_msg = ""
    n = int(s[2])  # the base shift for each character.
    prev_code = int(s[3])  # m
    msg = s[4]
    for i in msg:
        if ord('a') <= ord(i) <= ord('z'):
            char_code = (convert_to_code(i) + n + prev_code) % 26
            char_chr = convert_to_char(char_code)
            prev_code = char_code
            encoded_msg += char_chr
        else:
            encoded_msg += i

    print(encoded_msg)


def decode_msg(s):
    decoded_msg = ""
    n = int(s[2])  # the base shift for each character.
    prev_code = int(s[3])  # m
    msg = s[4]

    for i in msg:
        if ord('a') <= ord(i) <= ord('z'):
            char_code = ((convert_to_code(i) - n) - prev_code) % 26
            prev_code = convert_to_code(i)  # ord(i) - 97
            char_chr = convert_to_char(char_code)
            decoded_msg += char_chr
        else:
            decoded_msg += i

    print(decoded_msg)


process_input(sys.argv)
