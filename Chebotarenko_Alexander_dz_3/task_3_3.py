# Написать функцию thesaurus(), принимающую в качестве аргументов имена
# сотрудников и возвращающую словарь, в котором ключи — первые буквы имён,
# а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#    "И": ["Иван", "Илья"],
#    "М": ["Мария"],
#    "П": ["Петр"]
# }

# Подумайте: полезен ли будет вам оператор распаковки? Как поступить,
# если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def thesaurus(*args):
    """input names - output dictionary with keys"""

    name_list = {}
    for name in args:
        first_letter = name[0]
        if name_list.get(first_letter):
            name_list[first_letter].append(name)
        else:
            name_list.setdefault(first_letter, [name])
    return name_list


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Егор", "Евгений"))
