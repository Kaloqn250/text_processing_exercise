some_string = input()
new_message = ''
last_added = ''

for character in some_string:
    if character != last_added:
        new_message += character
        last_added = character

print(new_message)
