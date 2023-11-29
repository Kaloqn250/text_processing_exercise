first_string, second_string = input().split()
total_sum = 0

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        current_first_char, current_second_char = ord(first_string[index]), ord(second_string[index])
        total_sum += current_first_char * current_second_char
    for index in range(len(second_string), len(first_string)):
        current_first_char = ord(first_string[index])
        total_sum += current_first_char
elif len(first_string) < len(second_string):
    for index in range(len(first_string)):
        current_first_char, current_second_char = ord(first_string[index]), ord(second_string[index])
        total_sum += current_first_char * current_second_char
    for index in range(len(first_string), len(second_string)):
        current_second_char = ord(second_string[index])
        total_sum += current_second_char
elif len(first_string) == len(second_string):
    for index in range(len(second_string)):
        current_first_char, current_second_char = ord(first_string[index]), ord(second_string[index])
        total_sum += current_first_char * current_second_char

print(total_sum)
