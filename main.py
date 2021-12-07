def is_ever_increase(num) -> bool:
    numbers = str(num)
    numbers_1 = numbers[:-1]
    numbers_2 = numbers[1:]
    for i in range(len(numbers) - 1):
        if numbers_1[i] > numbers_2[i]:
            return False
    return True


def has_two_adjacent_digits(num) -> bool:
    numbers = str(num)
    numbers_1 = numbers[:-1]
    numbers_2 = numbers[1:]
    for i in range(len(numbers) - 1):
        if numbers_1[i] == numbers_2[i]:
            return True
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
