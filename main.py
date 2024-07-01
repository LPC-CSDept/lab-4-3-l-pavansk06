def main():
    total = 0

    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input('Enter a value: '))

    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[0]

    # total = sum(numbers)
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total, numbers


if __name__ == '__main__':
    main()
