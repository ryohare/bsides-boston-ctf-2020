import random
from secret import flag

rounds = 5
block_size = 8
sa = {
    0: 13,
    1: 0,
    2: 11,
    3: 4,
    4: 7,
    5: 6,
    6: 5,
    7: 10,
    8: 8,
    9: 3,
    10: 9,
    11: 15,
    12: 12,
    13: 1,
    14: 2,
    15: 14,
}
sb = {
    0: 9,
    1: 5,
    2: 6,
    3: 0,
    4: 2,
    5: 14,
    6: 10,
    7: 11,
    8: 7,
    9: 4,
    10: 3,
    11: 1,
    12: 13,
    13: 8,
    14: 15,
    15: 12,
}
key = [random.randrange(255), random.randrange(255)] * 4

to_bin = lambda x, n=block_size: format(x, "b").zfill(n)
to_int = lambda x: int(x, 2)
to_chr = lambda x: "".join([chr(i) for i in x])
to_ord = lambda x: [ord(i) for i in x]
bin_join = lambda x, n=int(block_size / 2): (str(x[0]).zfill(n) + str(x[1]).zfill(n))
bin_split = lambda x: (x[0 : int(block_size / 2)], x[int(block_size / 2) :])
str_split = lambda x: [x[i : i + block_size] for i in range(0, len(x), block_size)]
xor = lambda x, y: x ^ y


def s(a, b):
    return sa[a], sb[b]


def p(a):
    return a[2] + a[4] + a[0] + a[7] + a[3] + a[1] + a[6] + a[5]


def ks(k):
    return [
        k[i : i + int(block_size)] + k[0 : (i + block_size) - len(k)]
        for i in range(rounds)
    ]


def kx(state, k):
    return [xor(state[i], k[i]) for i in range(len(state))]


def en(e):
    encrypted = []
    for i in e:
        a, b = bin_split(to_bin(ord(i)))
        sa, sb = s(to_int(a), to_int(b))
        pe = p(
            bin_join((to_bin(sa, int(block_size / 2)), to_bin(sb, int(block_size / 2))))
        )
        encrypted.append(to_int(pe))
    return encrypted


def r(p, k):
    keys = ks(k)
    state = str_split(p)
    for b in range(len(state)):
        for i in range(rounds):
            rk = kx(to_ord(state[b]), keys[i])
            state[b] = to_chr(en(to_chr(rk)))
    return [ord(e) for es in state for e in es]


encrypted = r(flag, key)
print("Encrypted flag => %s" % encrypted)
# Encrypted flag => [63, 253, 213, 105, 250, 191, 55, 105, 226, 221, 223, 55, 55, 56, 55, 82, 146, 243, 159, 55, 55, 135, 213, 55, 94, 243, 55, 221, 94, 57, 226, 105, 196, 30, 213, 240, 91, 221, 152, 30, 213, 253, 37, 128]
