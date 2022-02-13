# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...


def odd_generator(num):
    for item in range(1, num + 1, 2):
        yield item


odd_num = odd_generator(16)
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
