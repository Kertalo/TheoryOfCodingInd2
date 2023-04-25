import random
import sympy


def step_table(f):
    table = []
    for i in range(0, f):
        new_step = 1
        if i == 0:
            new_step = 0
        a = []
        for j in range(0, f):
            a.append(new_step)
            new_step = new_step * i % f
        table.append(a)
    return table


def find_primitive(table):
    primitive_index = -1
    for i in range(len(table) - 1, -1, -1):
        now_values = []
        for j in range(0, len(table)):
            if table[i][j] == 0:
                break
            if not table[i][j] in now_values:
                now_values.append(table[i][j])
        if len(now_values) == len(table) - 1:
            primitive_index = i
            break
    return primitive_index


def coding_RS(message, q, excess):
    res_message = message.copy()
    for i in range(0, excess):
        res_message.append(0)
    table = step_table(q)
    primitive_element = table[find_primitive(table)]
    for i in range(0, len(res_message)):
        res_message[i] = 0
        for j in range(0, len(message)):
            res_message[i] += message[j] * (primitive_element[i] ** j)
        res_message[i] = res_message[i] % q
    return res_message

    # x = sympy.Symbol('x')
    # y = 1
    # for i in range(1, excess + 1):
    #     y *= (x + a**i)
    # y = sympy.expand(y)
    # return y


def make_mistake(message, q, t):
    if t > len(message):
        return message

    remain = len(message)
    mistake = []
    for i in range(0, remain):
        mistake.append(0)

    mistakes_indexes = []
    for i in range(0, t):
        mistakes_indexes.append(random.randrange(remain))
        remain -= 1

    for i in range(0, t):
        k = mistakes_indexes[i]
        for j in range(0, len(mistake)):
            if mistake[j] == 0:
                if k == 0:
                    mistake[j] = 1
                    break
                k -= 1

    for i in range(0, len(message)):
        message[i] += mistake[i]
        message[i] = message[i] % q

    return message


rs = coding_RS([1, 2, 3], 1031, 4)
print(rs)
print(make_mistake(rs, 1031, 2))
