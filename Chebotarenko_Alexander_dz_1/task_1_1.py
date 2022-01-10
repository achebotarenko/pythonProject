# Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах: до минуты:
# <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:

# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

MIN = 60
HOUR = MIN * 60
DAY = HOUR * 24
time_series = [53, 61, 153, 4153, 400153]
for duration in time_series:
    if duration < MIN:
        print(duration, 'сек')
    elif duration < HOUR:
        print(duration // MIN, 'мин', duration % MIN, 'сек')
    elif duration < DAY:
        print(duration // HOUR, 'час', duration % HOUR // MIN, 'мин',
              duration % MIN, 'сек')
    else:
        print(duration // DAY, 'дн', duration % DAY // HOUR, 'час',
              duration % HOUR // MIN, 'мин', duration % MIN, 'сек')
