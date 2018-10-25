aantal = 6

nr_ls = [0, 1]

counter = len(nr_ls)
while len(nr_ls) < aantal:
    nr_ls.append(nr_ls[counter - 1] + nr_ls[counter - 2])
    counter += 1
print(nr_ls)

# 0, 1, 1, 2, 3, 5,
ls = [0, 1]


def gen_seq_fib(n, ls=[0, 1]):
    if n == len(ls):
        return ls
    else:
        new_nr = ls[len(ls) - 1] + ls[len(ls) - 2]
        ls.append(new_nr)
        return gen_seq_fib(n, ls)


print(gen_seq_fib(6))
# def gen_fib(nr):
#     if nr <= 1:
#         return nr
#     t = gen_fib(nr - 1) + gen_fib(nr - 2)
#     return t
# print(gen_fib(6))
