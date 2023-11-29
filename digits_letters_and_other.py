input_line = input()
digits = ''
letters = ''
others = ''

for ch in input_line:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        others += ch

print(f'{digits}\n{letters}\n{others}')
