def to_hours(d):
    return d * 24


def to_min(h):
    return h * 60


d = int(input())
h = int(input())

hoursOfDays = to_hours(d)
totHours = hoursOfDays + h
totMin = to_min(totHours)

print(totMin)
