def verify(isbn):
    # Trim isbn string of dash
    isbn = isbn.replace('-', '')
    # Length check
    if len(isbn) != 10:
        return False
    # formula:
    # (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 +
    #  1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
    sum_of_times = 0
    for index, digit in enumerate(isbn):
        if digit.isalpha():
            if digit is 'X':
                if index is 0:
                    digit = 10
                else:
                    return False
            else:
                return False
        else:
            digit = int(digit)

        sum_of_times += digit * (index + 1)
        # print(digit, sum_of_times, index)

    return sum_of_times % 11 == 0


print(verify('3-598-2X507-9'))
