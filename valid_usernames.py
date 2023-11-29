def lenght(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def can_contain(name):
    for character in name:
        if not (character.isalnum() or character == '-' or character == '_'):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


def valid_username(name):
    if lenght(name) and can_contain(name) and no_redundant_symbols(name):
        return True
    return False


names = input().split(', ')
for some_name in names:
    if valid_username(some_name):
        print(some_name)
