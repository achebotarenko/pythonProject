
def show_sales(argv):
    program, *args = argv

    try:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            prices = f.read().splitlines()
            if len(args) == 0:
                for price in prices:
                    print(price)
            elif len(args) == 1:
                for price in prices[int(args[0]) - 1:]:
                    print(price)
            elif len(args) == 2:
                for price in prices[int(args[0]) - 1:int(args[1])]:
                    print(price)
    except FileNotFoundError:
        print(f'Ошибка! Файл с данными отсутствует')

    return 0


if __name__ == '__main__':
    import sys

exit(show_sales(sys.argv))
