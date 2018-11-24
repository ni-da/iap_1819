x1 = 1
y1 = 1

w1 = 2
h1 = 2

x2 = 1
y2 = 2

w2 = 1
h2 = 3


# def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
#     if x1 == x2 or y1 == y2 or w1 == w2 or h1 == h2:
#         return False
#     return True

def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 == x2 or y1 == y2 or w1 == w2 or h1 == h2:
        return False
    return True


print(does_intersect(1, 1, 2, 2, 1, 3, 2, 2))

SI = max(0, min(w1, w2) - max(x1, x2)) * max(0, min(h1, h2) - max(y1, y2))
print(SI)
