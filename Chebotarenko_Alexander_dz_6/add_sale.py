
def add_sale(argv):
    program, price = argv

    try:
        argv == float(price)
    except ValueError:
        print(f'Ошибка, должно быть введено число')

    try:
        with open('bakery.csv', 'a', encoding='utf-8') as f:
            f.writelines([str(price), '\n'])
    except FileNotFoundError:
        with open('bakery.csv', 'w', encoding='utf-8') as f:
            f.writelines([str(price), '\n'])

    return 0


if __name__ == '__main__':
    import sys

exit(add_sale(sys.argv))
