import random

random = random.Random()


def generate_random(a, b):
    random_numbers = []
    for i in range(100):
        random_number = random.randrange(a, b)
        random_numbers.append(random_number)
    return random_numbers


def calculate_occurrences(randoms, a):
    counter = 0
    for i in randoms:
        if i == a:
            counter += 1
    return counter


def calculate_occurrences_inPercentage(randoms):
    occurrences = []
    for i in range(10):
        som = calculate_occurrences(randoms, i)
        percentage = int(((som / 100) * 100))
        occurrences.append(percentage)
        som = 0
        percentage = 0
    return occurrences


def generate_countOccurrences(a, b):
    randoms = generate_random(a, b)
    return (calculate_occurrences_inPercentage(randoms))


print(generate_countOccurrences(3,7+1))