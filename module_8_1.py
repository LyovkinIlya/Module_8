def add_everything_up(a, b):
    try:
        ab = a + b
    except TypeError:
        return str(a) + str(b)
    return '{:.3f}'.format(ab)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))