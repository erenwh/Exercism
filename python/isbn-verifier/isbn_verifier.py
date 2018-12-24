import re


def verify(isbn):
    # formula:
    # (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 +
    #  1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0

    # Regex check for isbn
    if re.fullmatch("[0-9][-]?[0-9]{3}[-]?[0-9]{5}[-]?([0-9]|[X])", isbn) is None:
        return False
    else:
        # Trim dashes '-'
        isbn = isbn.replace('-', '')
        sum_of_times = 0
        for index, digit in enumerate(isbn):
            if digit is 'X' and index is 9:
                digit = 10
            else:
                digit = int(digit)
            sum_of_times += digit * (index + 1)
    if sum_of_times % 11 == 0:
        return True
    else:
        return False
