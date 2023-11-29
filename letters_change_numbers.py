def first_letters_solving(letter, numbers):
    letter_position = 0
    result = 0

    if letter.isupper():
        for letter_as_int in range(65, 91):
            letter_position += 1
            if letter_as_int == ord(letter):
                break
        result = numbers / letter_position

    elif letter.islower():
        for letter_as_int in range(97, 123):
            letter_position += 1
            if letter_as_int == ord(letter):
                break
        result = numbers * letter_position
    return result


def second_letters_solving(letter, numbers):
    letter_position = 0
    result = 0

    if letter.isupper():
        for letter_as_int in range(65, 91):
            letter_position += 1
            if letter_as_int == ord(letter):
                break
        result = numbers - letter_position

    elif letter.islower():
        for letter_as_int in range(97, 123):
            letter_position += 1
            if letter_as_int == ord(letter):
                break
        result = numbers + letter_position
    return result


numbers = input().split()
letters = []
total_result = 0

for number in numbers:
    numbers_as_string = ''

    for char in number:
        if char.isdigit():
            numbers_as_string += char
        else:
           letters.append(char)
    numbers = int(numbers_as_string)

    first_result = first_letters_solving(letters[0], numbers)
    second_result = second_letters_solving(letters[1], first_result)
    letters = []
    total_result += second_result

print(f'{total_result:.02f}')
