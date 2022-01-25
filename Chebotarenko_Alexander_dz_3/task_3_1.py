# Написать функцию num_translate(), переводящую числительные от 0 до 10
# c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше
# хранить информацию, необходимую для перевода: какой тип данных выбрать,
# в теле функции или снаружи.

def num_translate(dict_items):
    """
    translate input english numbers into russian

    :param dict_items: items of dictionary
    :return: translation of items
    """


    dict_eng_ru = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'}
    return print(f'Число на русском: {dict_eng_ru.get(dict_items)}')


num_translate(input('Введите прописью число на английском: '))
