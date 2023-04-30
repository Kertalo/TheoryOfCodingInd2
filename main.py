import random


# Строим таблицу степеней
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


# Находим примитивный элемент
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


# Обратное дискретное преобразование Фурье
def coding_RS(message, excess, q):
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


# Делаем ошибку
def make_mistake(message, t, q):
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


# a / b
def division(a, b, q):
    if b == 1:
        return a % q
    for i in range(1, q):
        c = (a * i) % ((b * i) % q)
        if c == 0:
            return int((a * i) / ((b * i) % q)) % q


# Прямое преобразование Фурье
def decoding_RS(message, q):
    table = step_table(q)
    primitive = find_primitive(table)

    res_message = []

    for i in range(0, len(message)):
        element = 0
        for j in range(0, len(message)):
            element += division(message[j], primitive ** (i * j), q)
        #print(element)
        res_message.append(division(element, len(message), q))

    return res_message


rs = coding_RS([1, 2, 3], 4, 1031)
print(rs)

#rs = make_mistake(rs, 1, 1031)
#print(rs)

print(decoding_RS(rs, 1031))

#print(find_primitive(step_table(1031)))
