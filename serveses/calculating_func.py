def first_calc(input_1):
    count = 0
    count_else = 0
    for i in input_1:
        count += int(i)
    if count >= 10:
        while count >= 10:
            count_else = count
        count = 0
        for i in str(count_else):
            count += int(i)
        return count
    else:
        return count


def second_calc(input_1):
    count = 0
    count_else = 0
    for i in input_1:
        count += int(i)
    if count >= 10:
        while count >= 10:
            count_else = count
            count = 0
            for i in str(count_else):
                count += int(i)
        return count
    else:
        return count


def third_calc(input_1):
    count = 0
    count_1 = 0
    for i in input_1:
        count += int(i)
    if count >= 10:
        while count >= 10:
            count_1 = count
            count = 0
            for i in str(count_1):
                count += int(i)
        return count
    else:
        return count


def fourth_calc(f, s, t):
    count = 0
    count_1 = 0
    sum_ = f + s + t
    for i in str(sum_):
        count += int(i)
    if count >= 10:
        while count >= 10:
            count_1 = count
            count = 0
            for i in str(count_1):
                count += int(i)
        return count
    else:
        return count

