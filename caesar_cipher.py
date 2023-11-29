some_string = input()
new_string = ''

for character in some_string:
    current_character = ord(character)
    current_character += 3
    new_string += chr(current_character)

print(new_string)
