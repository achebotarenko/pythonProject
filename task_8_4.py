# Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и
# выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#    ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#   return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#  ...
#    raise ValueError(msg)
# ValueError: wrong val -5


def val_checker(func):
    def wrapped(x):
        if not x > 0:
            raise ValueError(f'wrong value: {x}')
        else:
            print(f'Result: {func(x)}')

    return wrapped


@val_checker
def calc_cube(x):
    return x ** 3


calc_cube(5)
calc_cube(-5)
