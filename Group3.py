# Consider throwing exceptions when input is out of range in later programs
# (It save time as the program does not need to iterate over the input string twice
#  to check for validity and then changing bases)


# Convert 1 digit from input base to an integer
def hex_to_digit(k):
    if "0" <= k <= "9":
        return int(k)
    else:
        return ord(k) - 65 + 10


# Convert 1 digit from an integer to output base
def digit_to_hex(k):
    if 0 <= k <= 9:
        return str(k)
    else:
        return chr(k - 10 + 65)


# Convert number from input base to an integer
def inp_base_to_dec(n, inputBase):
    n = str(n)
    power = 1
    res = 0
    for i in range(len(n) - 1, -1, -1):
        res += hex_to_digit(n[i]) * power
        power *= inputBase
    return res


# Convert number from an integer to output base
def dec_to_out_base(n: int, outputBase: int):
    res = ""
    while n > 0:
        res = digit_to_hex(n % outputBase) + res
        n //= outputBase
    return res


# Convert fractional part of number from input base to float
def inp_base_to_dec_float(n: str, inputBase: int):
    power = 1 / inputBase
    res = 0
    for i in range(0, len(n)):
        res += hex_to_digit(n[i]) * power
        power /= inputBase
    return res


# Add two number a and b in base inputBase
def add(a, b, inputBase):
    while len(a) > len(b):
        b = "0" + b
    while len(a) < len(b):
        a = "0" + a

    temp = 0
    res = ""
    for i in range(len(a) - 1, -1, -1):
        value_a = int(hex_to_digit(a[i]))
        value_b = int(hex_to_digit(b[i]))
        sum_ = value_a + value_b + temp
        temp = sum_ // inputBase
        res = str(digit_to_hex(sum_ % inputBase)) + res

    if temp > 0:
        res = str(digit_to_hex(temp)) + res

    return res


# Multiply number st with digit a in base inputBase
def multi_digit(st, a, inputBase):
    temp = 0
    res = ""
    for i in range(len(st) - 1, -1, -1):
        multi = int(hex_to_digit(st[i])) * a + temp
        temp = multi // inputBase
        res = str(digit_to_hex(multi % inputBase)) + res
    if temp > 0:
        res = str(digit_to_hex(temp)) + res
    return res


# Multiply number a with number b in base inputBase
def multi(a, b, inputBase):
    zeros = ""
    res = ""
    for i in range(len(b) - 1, -1, -1):
        temp = multi_digit(a, hex_to_digit(b[i]), inputBase) + zeros

        res = add(res, temp, inputBase)
        zeros += "0"
    return res


#
def minus(a, b, inputBase):
    while len(a) > len(b):
        b = "0" + b
    while len(a) < len(b):
        a = "0" + a

    if a < b:
        temp = a
        a = b
        b = temp

    temp = 0
    res = ""
    for i in range(len(a) - 1, -1, -1):
        value_a = int(hex_to_digit(a[i]))
        value_b = int(hex_to_digit(b[i]))
        value_a = value_a - temp

        if value_a < value_b:
            minus = value_a + inputBase - value_b
            temp = 1
        else:
            minus = value_a - value_b
            temp = 0
        res = str(digit_to_hex(minus % inputBase)) + res
    while res[0] == "0":
        res = res[1:]
    return res


def div(st, a, inputBase):
    number = 0
    res = ""
    a = hex_to_digit(a)
    for i in range(0, len(st)):
        number = number * inputBase + int(hex_to_digit(st[i]))
        res = res + str(digit_to_hex(number // a))
        number = number % a
    while res[0] == "0":
        res = res[1:]
    return res


def mod(st, a, inputBase):
    number = 0
    a = hex_to_digit(a)

    for i in range(0, len(st)):
        number = number * inputBase + int(hex_to_digit(st[i]))
        number = number % a

    return dec_to_out_base(number, inputBase)


if "__main__" == __name__:
    print(multi("50", "50", 16))
    print(multi("50", "50", 10))
    print(multi("FA", "CE", 16))
    print(mod("FA", "E", 16))
