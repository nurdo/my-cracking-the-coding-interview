# My answer to Problem 5.3

def flip_bit(num):
    zero1 = -1
    zero2 = None
    max_len = 1
    i = 0

    while num > 0:
        if num & 1 == 0:
            if not zero2:
                zero2 = i
            else:
                max_len = max(max_len, i - 1 - zero1)
                zero1 = zero2
                zero2 = i

        num >>= 1
        i += 1

    max_len = max(max_len, i - 1 - zero1)
    print(max_len)
    return max_len
