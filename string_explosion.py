some_sting = input()
final_string = ''
strength = 0
for index in range(len(some_sting)):
    if strength > 0 and some_sting[index] != '>':
        strength -= 1
    elif some_sting[index] == '>':
        final_string += some_sting[index]
        strength += int(some_sting[index+1])
    else:
        final_string += some_sting[index]

print(final_string)