FIVE_NAMES = ["John", "James", "Jack", "Jill", "Jenny"]
AGES = [20, 21, 22, 23, 24]

MAP_NAME_TO_AGE = {name: age for name, age in zip(FIVE_NAMES, AGES)}


def average_age():
    return sum(AGES) / len(AGES)


print(average_age())
