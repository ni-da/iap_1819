# Write a function that counts the number of words in a string.

def count_words(s):
    counter = 1
    for i in s:
        if i == " ":
            counter += 1
    return counter


s = "This is it. What are you doing?"
print(count_words(s))


print(len(s.split()))