sequence_of_strings = input().split()
repeat_string = ''

for text in sequence_of_strings:
    repeat_string += text * len(text)

print(repeat_string)