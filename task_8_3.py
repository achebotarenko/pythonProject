# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#    ...
#
#
# @type_logger
# def calc_cube(x):
#   return x ** 3
#
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


# позиционные аргументы

def type_logger(func):
    def type_arguments(x, y):
        print(f'{x} : {type(x)} , {y} : {type(y)}')
        print(f'Result: {func(x, y)}')
    return type_arguments


@type_logger
def calc_summ(x, y):
    return x + y


calc_summ(10, 5)


@type_logger
def calc_cube(x, y):
    return x ** 3


calc_cube(10, 5)


# именованные аргументы

def type_logger(func):
    def type_arguments(*args):
        print(f'{args} : {type(args)}')
        print(f'Result: {func(*args)}')
    return type_arguments


@type_logger
def calc_summ(x, y):
    return x + y


calc_summ(10, 5)


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(10)
