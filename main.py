import re


def is_ever_increase(num) -> bool:
    numbers = str(num)
    numbers_1 = numbers[:-1]
    numbers_2 = numbers[1:]
    for i in range(len(numbers) - 1):
        if numbers_1[i] > numbers_2[i]:
            return False
    return True


def is_part_of_larger(x, three_adj_digits):
    for item in three_adj_digits:
        if item.find(x) > -1:
            return True
    return False


def has_two_adjacent_digits(num) -> bool:
    numbers = str(num)
    two_adj_regex = '[1]{2}|[2]{2}|[3]{2}|[4]{2}|[5]{2}|[6]{2}|[7]{2}|[8]{2}|[9]{2}'
    three_adj_regex = '[1]{3}|[2]{3}|[3]{3}|[4]{3}|[5]{3}|[6]{3}|[7]{3}|[8]{3}|[9]{3}'

    two_adj_digits = re.findall(two_adj_regex, numbers)
    three_adj_digits = re.findall(three_adj_regex, numbers)

    part_of = True
    for x in two_adj_digits:
        if not is_part_of_larger(x, three_adj_digits):
            part_of = False

    if len(two_adj_digits) > 0 and not part_of:
        return True
    else:
        return False


def main(input='372037-905157'):
    split = input.split('-')
    counter = 0
    for i in range(int(split[0]), int(split[1])):
        if is_ever_increase(i) and has_two_adjacent_digits(i):
            counter += 1
    return counter


if __name__ == '__main__':
    print(main())
